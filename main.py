from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, SelectField
# from wtforms.validators import DataRequired, URL, Optional
from flask_ckeditor import CKEditor, CKEditorField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship
from datetime import date
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from form import LoginForm, CreateProjectForm
# from functools import wraps

current_year = date.today().year

# create the app
app = Flask(__name__)
db = SQLAlchemy()

# Creating the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Create the Project Table
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=True)
    img_url = db.Column(db.String(250), nullable=True)
    project_url = db.Column(db.String(250), nullable=True)
    date = db.Column(db.String(250), nullable=True)
    client = db.Column(db.String(250), nullable=True)


# Create the User Table
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))






# all_projects = []

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_projects = db.session.query(Project).all()
    return render_template("index.html", projects=all_projects)


@app.route('/projects')
def get_all_projects():
    selected_type = request.args.get('type') # get the selected project type from the URL
    if selected_type:
        projects = Project.query.filter_by(type=selected_type).all()
        count = len(projects)
        project_string = f"{selected_type.capitalize()} ({count} project{'s' if count > 1 else ''})"
    else:
        projects = Project.query.all()
        project_string = "All Projects"
    return render_template("gallery.html", all_projects=projects, project_string=project_string)


# RENDER POST USING DB
@app.route("/project-single/<int:post_id>")
def project_single(post_id):
    requested_post = Project.query.get(post_id)
    return render_template("gallery-single.html", project=requested_post)


@app.route("/new-project", methods=["GET", "POST"])
def add_new_project():
    form = CreateProjectForm()
    if form.validate_on_submit():
        new_post = Project(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            type=form.type.data,
            project_url=form.project_url.data,
            date=form.date.data,
            client=form.client.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_projects"))
    return render_template("make-project.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = Project.query.get(post_id)
    edit_form = CreateProjectForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body,
        type=post.type,
        project_url=post.project_url,
        date=post.date,
        client=post.client
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        post.type = edit_form.type.data
        post.project_url = edit_form.project_url.data
        post.date = edit_form.date.data
        post.client = edit_form.client.data
        db.session.commit()
        return redirect(url_for("project_single", post_id=post.id))

    return render_template("make-project.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
def delete_project(post_id):
    project_to_delete = Project.query.get(post_id)
    db.session.delete(project_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_projects'))


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        # Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_projects'))

    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_projects'))


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         email = form.email.data
#         password = form.password.data
#
#         user = User.query.filter_by(email=email).first()
#         # Email doesn't exist
#         if not user:
#             flash("That email does not exist, please try again.")
#             return redirect(url_for('login'))
#         # Password incorrect
#         elif not check_password_hash(user.password, password):
#             flash('Password incorrect, please try again.')
#             return redirect(url_for('login'))
#         else:
#             login_user(user)
#             return redirect(url_for('get_all_posts'))
#
#     return render_template("login.html", form=form, current_user=current_user)


if __name__ == '__main__':
    app.run(debug=True)


# print(generate_password_hash('', method='pbkdf2:sha256', salt_length=8))