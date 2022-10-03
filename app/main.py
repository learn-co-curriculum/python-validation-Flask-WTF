from wsgiref.validate import validator
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# For CRSF token
app.config['SECRET_KEY'] = 'secret-key'

# Create a Form Class
class NameForm(FlaskForm):
    name = StringField('What is your name', validators=[DataRequired()])
    # Length input validator
    submit = SubmitField('Submit')
# custom validator

@app.route('/', methods=['GET','POST'])
def index():
    name = None
    form = NameForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('index.html', name= name, form = form )


if __name__ == '__main__':
    app.run()