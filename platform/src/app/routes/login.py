from app.routes import *
from app.forms import LoginForm, RegisterForm


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm(csrf_enabled=False)

    if request.method == 'POST':
        user_id = request.form.get('user_id')

        if form.validate_on_submit:
            u = User(email=form.email.data.lower())
            u.set_password(form.password.data)
            u.submit()

            login_user(u, remember=True)

            return redirect(url_for('login'))
        else:
            for field_name, error_message in form.errors.items():
                flash(error_message[0])
                break

        return render_template("default/register.html", title='Register', form=form, register_key=register_key)
    return render_template("default/register.html", title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm(csrf_enabled=False)
    if request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/')
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('default/login.html', title='Sign In', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
