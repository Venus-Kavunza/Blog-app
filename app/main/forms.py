from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired, Email

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    post = TextAreaField('Your Blog', validators=[InputRequired()])
    submit = SubmitField('Submit Blog')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [InputRequired()])
    submit = SubmitField('Save')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Add a comment',validators=[InputRequired()])
    submit = SubmitField('Comment')

class UpdateBlog(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    post = TextAreaField('Your Blog', validators=[InputRequired()])
    submit = SubmitField('Submit Blog')

class SubscribeForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(),Email()], render_kw={'placeHolder':'Enter email address here....'})
    submit = SubmitField('Subscribe')