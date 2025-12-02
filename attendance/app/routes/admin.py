from flask import Blueprint, render_template, redirect, url_for, session


admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html')
    
    return redirect(url_for('auth.login'))
    
    
    
    

