from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, URL, Optional
from flask_ckeditor import CKEditorField


# WTForm
class CreateProjectForm(FlaskForm):
    title = StringField("Project Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    type = SelectField("Type", choices=[("data science", "Data Science"), ("python", "Python")], validators=[DataRequired()])
    img_url = StringField("Project Image URL", validators=[DataRequired(), URL()])
    project_url = StringField("Project Git URL", validators=[Optional(), URL()])
    date = StringField("Date", validators=[DataRequired()], render_kw={"placeholder": "March 2022 or Sept 2022 - Janvier 2023"})
    client = StringField("Client", validators=[DataRequired()])
    body = CKEditorField("Project Content", validators=[DataRequired()])
    submit = SubmitField("Submit Project")


class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField("Let Me In!!")




# class AddForm(FlaskForm):
#     title = StringField("Blog Post Title", validators=[DataRequired()])
#     subtitle = StringField("Subtitle", validators=[DataRequired()])
#     img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
#     body = CKEditorField("Blog Content", validators=[DataRequired()])
#     submit = SubmitField("Submit Post")
#
#
# class RegisterForm(FlaskForm):
#     email = StringField(validators=[DataRequired()])
#     password = PasswordField(validators=[DataRequired()])
#     name = StringField(validators=[DataRequired()])
#     submit = SubmitField("Sign Me Up!")
#
#

#
#
# class ContactForm(FlaskForm):
#     # contact_name =
#     # contact_email=
#     # subject =
#     message = CKEditorField("Comment", validators=[DataRequired()])
#     submit = SubmitField("Submit Comment")
