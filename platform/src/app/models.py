from app import db, login_mng
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class BaseMixin(object):
    def submit(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        try:
            db.session.add(obj)
            db.session.commit()
        except:
            db.session.rollback()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()


class User(BaseMixin, db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64, collation='utf8mb4_romanian_ci'), index=True, unique=True)
    password = db.Column(db.String(128))
    access_level = db.Column(db.Integer, default=0)

    data = db.relationship("UserData")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User id={}, email={}, access_level={}>' \
            .format(self.id, self.email, self.access_level)


class UserData(BaseMixin, db.Model, UserMixin):
    __tablename__ = 'user_data'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    data_id = db.Column(db.Integer, db.ForeignKey('data.id'))
    value = db.Column(db.String(512, collation='utf8mb4_romanian_ci'))

    user = db.relationship("User", uselist=False)
    data = db.relationship("Data")

    def __repr__(self):
        return '<id={}, user_id={}, data={}, value={}>' \
            .format(self.id, self.user_id, self.data.name, self.value)


class Data(BaseMixin, db.Model, UserMixin):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def get_data(data_name):
        data = Data.query.filter(Data.name == data_name).first()
        if not data:
            data = Data(name=data_name)
        return data


# ##############
# Flask-Login  ######
# var: current_user #
# ###################
@login_mng.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    if user:
        user.custom_data = {}
        for ud in user.data:
            user.custom_data[ud.data.name] = ud.value
    return user
