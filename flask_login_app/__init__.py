from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
import os
from datetime import timedelta

app = Flask(__name__)

app.config['BASE_DIR'] = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "dontstealmysecretkey"
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=30)
# app.config['REMEMBER_COOKIE_SECURE'] = "HTTPS"


db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))


admin = Admin(app, index_view=MyAdminIndexView())
admin.add_view(MyModelView(User, db.session))


@app.route('/login')
def login():
    user = User.query.filter_by(username='rshende').first()
    login_user(user, remember=True)
    return 'You are now logged in!'


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "You are now logged out!"


@app.route('/home')
@login_required
def home():
    return "The current user is " + current_user.username


if __name__ == '__main__':
    app.run(debug=True)
