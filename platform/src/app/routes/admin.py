from app.routes import *
import string
import random
import json


@app.route("/admin", methods=['GET', 'POST'])
@login_required
@admin_required
def admin():
    if request.method == 'GET':
        return render_template("admin.html", user=current_user)