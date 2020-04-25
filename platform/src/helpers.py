from functools import wraps
from flask import g, request, redirect, url_for
from flask_login import current_user
from subprocess import check_output
import sys


def dprint(*args):  # debug print
    print(*args, file=sys.stderr)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.access_level < 1:
            return redirect(url_for('index'))
        return f(*args, **kwargs)

    return decorated_function


def get_container_ip(cont_name):
    out = check_output(["dig", "+short", cont_name])
    out = out.decode("utf-8")
    out = out.split('\n', 1)[0]
    return out if out is not "" else None
