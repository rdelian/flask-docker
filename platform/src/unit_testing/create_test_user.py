from sys import path

path.append('/platform/src/')

from app.routes import *


# noinspection PyArgumentList
def create_keywords():
    d = Data(name="first_name")
    d.submit()
    d = Data(name="last_name")
    d.submit()
    d = Data(name="profile_pic")
    d.submit()


# noinspection PyArgumentList
def create_test_user():
    create_keywords()

    u = User(email="asd", access_level=1)
    u.set_password('asd')

    u.data.append(UserData(data=Data.get_data("first_name"), value="DELETE"))
    u.data.append(UserData(data=Data.get_data("last_name"), value="ME"))
    u.data.append(UserData(data=Data.get_data("profile_pic"),
                           value="http://theasianherald.com/wp-content/uploads/2017/02/16583841_243568769423759_7297710697935273984_n.jpg"))

    u.submit()
    print('User created')


if __name__ == '__main__':
    create_test_user()  # create 1 user
    pass
