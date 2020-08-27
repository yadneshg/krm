

#for login session
from functools import wraps

from flask import session, render_template


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        message=""
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            message = "You need to login first"
            return render_template('login.html', message=message)
    return wrap
