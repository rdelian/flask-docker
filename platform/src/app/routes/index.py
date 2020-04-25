from app.routes import *
import datetime as dt
import numpy as np
import json


@app.route("/", methods=['GET'])
@login_required
def index():
    return render_template("index.html", user=current_user)