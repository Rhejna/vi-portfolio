# login_manager = LoginManager()
# login_manager.init_app(app)
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
#
#
class Projects(db.Model):
    __tablename__ = "project_posts"
    id = db.Column(db.Integer, primary_key=True)
    # ***************Child Relationship*************#
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    # author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # # Create reference to the User object, the "posts" refers to the posts protperty in the User class.
    # author = relationship("User", back_populates="project")

    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
#
#
# class User(UserMixin, db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(1000))
#     # ***************Parent Relationship*************#
#     project = relationship("Projects", back_populates="author")
#
#
# class Contact(db.Model):
#     __tablename__ = "contact"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(1000), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     subject = db.Column(db.String(1000))
#     date = db.Column(db.DateTime, nullable=False)
#     text = db.Column(db.Text, nullable=False)


db.create_all()

# admin-only decorator
# def admin_only(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if current_user.id != 1:
#             abort(403, description="Not authorised")
#         return f(*args, **kwargs)
#
#     return decorated_function