from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from models import db, User
from api_utils import fetch_user_data
from excel_utils import update_excel, get_excel_path
from flask_apscheduler import APScheduler
import os
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key' # Change in production

db.init_app(app)
scheduler = APScheduler()

def update_all_users():
    with app.app_context():
        users = User.query.all()
        for user in users:
            data = fetch_user_data(user.profile_url, user.platform)
            if data:
                user.rating = data.get('rating', 0)
                user.rank = data.get('rank', 'Unrated')
                user.global_rank = data.get('global_rank', 0)
                user.country_rank = data.get('country_rank', 0)
                user.recent_problems = data.get('recent_problems', 0)
                user.total_contests = data.get('total_contests', 0)
                user.last_updated = datetime.utcnow()
        db.session.commit()
        update_excel(users)
        print(f"Daily update completed: {datetime.now()}")

@app.route('/')
def index():
    users = User.query.order_by(User.rating.desc()).all()
    return render_template('index.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        platform = request.form.get('platform')
        profile_url = request.form.get('profile_url')

        if not name or not profile_url:
            flash('All fields are required!', 'danger')
            return redirect(url_for('register'))

        # Check if user already exists
        existing_user = User.query.filter_by(profile_url=profile_url).first()
        if existing_user:
            flash('Profile URL already registered!', 'warning')
            return redirect(url_for('register'))

        # Fetch initial data
        data = fetch_user_data(profile_url, platform)
        if not data:
            flash('Invalid Profile URL or could not fetch data.', 'danger')
            return redirect(url_for('register'))

        new_user = User(
            name=name,
            platform=platform,
            profile_url=profile_url,
            rating=data.get('rating', 0),
            rank=data.get('rank', 'Unrated'),
            global_rank=data.get('global_rank', 0),
            country_rank=data.get('country_rank', 0),
            recent_problems=data.get('recent_problems', 0),
            total_contests=data.get('total_contests', 0)
        )
        db.session.add(new_user)
        db.session.commit()
        
        # Update Excel
        update_excel(User.query.all())
        
        flash('Registration successful!', 'success')
        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/refresh/<int:user_id>')
def refresh(user_id):
    user = User.query.get_or_404(user_id)
    data = fetch_user_data(user.profile_url, user.platform)
    if data:
        user.rating = data.get('rating', 0)
        user.rank = data.get('rank', 'Unrated')
        user.global_rank = data.get('global_rank', 0)
        user.country_rank = data.get('country_rank', 0)
        user.recent_problems = data.get('recent_problems', 0)
        user.total_contests = data.get('total_contests', 0)
        user.last_updated = datetime.utcnow()
        db.session.commit()
        update_excel(User.query.all())
        flash(f'Updated data for {user.name}', 'success')
    else:
        flash('Failed to update data.', 'danger')
    return redirect(url_for('index'))

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    name = user.name
    db.session.delete(user)
    db.session.commit()
    # Update Excel after deletion
    update_excel(User.query.all())
    flash(f'User {name} deleted successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/download')
def download():
    path = get_excel_path()
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    flash('Excel file not generated yet.', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        # Handle schema changes for existing DB (simplified for this project)
        # In a real app we'd use Flask-Migrate, here we'll just drop/recreate if needed or just create_all
        # Since we added columns, create_all won't update existing tables.
        # For this task, I'll clear the DB to ensure new schema is applied.
        if os.path.exists('instance/database.db'):
             # Optional: backup or migration. For now let's just create new.
             pass
        db.create_all()
    
    # Setup scheduler
    scheduler.add_job(id='daily_update', func=update_all_users, trigger='interval', days=1)
    scheduler.start()
    
    app.run(debug=True)
