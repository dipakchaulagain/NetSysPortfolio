from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=2, max=200)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Send Message')

class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=200)])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = StringField('Image URL', validators=[Optional(), Length(max=255)])
    technologies = StringField('Technologies (comma-separated)', validators=[Optional(), Length(max=500)])
    link = StringField('Project Link', validators=[Optional(), Length(max=255)])
    order = IntegerField('Display Order', validators=[Optional(), NumberRange(min=0)], default=0)
    submit = SubmitField('Save Project')

class SkillForm(FlaskForm):
    name = StringField('Skill Name', validators=[DataRequired(), Length(min=2, max=100)])
    category = StringField('Category', validators=[Optional(), Length(max=100)])
    proficiency = IntegerField('Proficiency (0-100)', validators=[DataRequired(), NumberRange(min=0, max=100)])
    order = IntegerField('Display Order', validators=[Optional(), NumberRange(min=0)], default=0)
    submit = SubmitField('Save Skill')

class TestimonialForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    role = StringField('Role/Position', validators=[Optional(), Length(max=150)])
    company = StringField('Company', validators=[Optional(), Length(max=150)])
    message = TextAreaField('Testimonial', validators=[DataRequired()])
    order = IntegerField('Display Order', validators=[Optional(), NumberRange(min=0)], default=0)
    submit = SubmitField('Save Testimonial')

class ExperienceForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired(), Length(min=2, max=200)])
    company = StringField('Company', validators=[DataRequired(), Length(min=2, max=200)])
    location = StringField('Location', validators=[Optional(), Length(max=200)])
    start_date = StringField('Start Date (e.g., Jan 2020)', validators=[DataRequired(), Length(max=50)])
    end_date = StringField('End Date (e.g., Dec 2022 or "Present")', validators=[Optional(), Length(max=50)])
    description = TextAreaField('Description', validators=[DataRequired()])
    order = IntegerField('Display Order', validators=[Optional(), NumberRange(min=0)], default=0)
    submit = SubmitField('Save Experience')

class SiteSettingsForm(FlaskForm):
    profile_name = StringField('Profile Name', validators=[DataRequired(), Length(min=2, max=100)])
    profile_image = FileField('Upload Profile Image', validators=[Optional(), FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'webp'], 'Images only (jpg, png, gif, webp)')])
    current_image = StringField('Current Image Path')
    tagline = StringField('Tagline', validators=[DataRequired(), Length(max=200)])
    cv_file = FileField('Upload CV (PDF)', validators=[Optional(), FileAllowed(['pdf'], 'PDF files only')])
    current_cv = StringField('Current CV Filename')
    submit = SubmitField('Save Settings')

class SocialLinkForm(FlaskForm):
    platform = StringField('Platform Name', validators=[DataRequired(), Length(min=2, max=50)])
    url = StringField('URL', validators=[DataRequired(), Length(max=500)])
    icon_class = StringField('Icon Class (e.g., fab fa-linkedin)', validators=[DataRequired(), Length(max=100)])
    order = IntegerField('Display Order', validators=[Optional(), NumberRange(min=0)], default=0)
    submit = SubmitField('Save Social Link')
