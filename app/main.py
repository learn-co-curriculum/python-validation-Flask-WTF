from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)

# For CSRF token
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

# Create a Form Class
class NameForm(FlaskForm):
    name = StringField('What is your name', validators=[InputRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
def index():
    name = None
    form = NameForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('index.html', name= name, form = form )


if __name__ == '__main__':
    app.run(port=5555)
