import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')

@bp_auth.route('/register', methods=('GET', 'POST'))
def register():
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
    #     error = None
    #
    #     if not username:
    #         error = 'Username is required.'
    #     elif not password:
    #         error = 'Password is required.'
    #     elif
    #
    #         #     db.execute(
    #         # 'SELECT id FROM user WHERE username = ?', (username,)
    #     # ).fetchone() is not None:
    #         error = 'User {} is already registered.'.format(username)
    #
    #     if error is None:
    #         db.execute(
    #             'INSERT INTO user (username, password) VALUES (?, ?)',
    #             (username, generate_password_hash(password))
    #         )
    #         db.commit()
    #         return redirect(url_for('auth.login'))
    #
    #     flash(error)
    #
    return render_template('auth/register.html')

@bp_auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # db = get_db()
        # error = None
        # user = db.execute(
        #     'SELECT * FROM user WHERE username = ?', (username,)
        # ).fetchone()

        # if user is None:
        #     error = 'Incorrect username.'
        # elif not check_password_hash(user['password'], password):
        #     error = 'Incorrect password.'

        if username == "admin" and password == "123":
            session.clear()
            session['user_id'] = username
            return redirect(url_for('home'))
        # flash(error)
    return render_template('auth/login.html')

@bp_auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user=user_id
        # g.user = get_db().execute(
        #     'SELECT * FROM user WHERE id = ?', (user_id,)
        # ).fetchone()

@bp_auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view