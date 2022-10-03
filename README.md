# Create Forms and filter input with Flask-WTF

## Learning Goals

- Learn how to create forms with Flask-WTF
- Use validators to validate form data

***

## Key Vocab

- **Validation**: Validation is an automatic check to ensure that data entered is sensible and feasible.
- **Form**: An HTML form is used to collect user input. The user input is most often sent to a server for processing.

***

## Introduction

Flask-WTF forms is an integration of Flask and WTForms. WTForms is a forms validation and rendering library for Python Web Development.

***

## CRSF token

## Different Validators

Email validator
```py

```

Password 
```py
class ChangePassword(Form):
    password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')

```


***

## Final Code 
```py
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
    app.run()
```

```html
<html>
<head>
<title>WTForms</title>
</head>
<body>

{% if name %}
    <h1>Hello {{name}}</h1>

{% else %}
    <h1>What is your name?</h1>
    <br/>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }}
        {{ form.name() }}
        <br/>
        {{ form.submit()}}

    </form>
{% endif %}
</body>
</html>

```

## Conclusion

Flask-WTF can help us create and validate form data before pushing it to the backend for processing. Validating data can prevent
data type errors and help us create a more robust and error free program.

***

## Resources

- [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)
