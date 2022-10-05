# Create Forms and filter input with Flask-WTF

## Learning Goals

- Learn how to create forms with Flask-WTF and WTForms.
- Use validators to validate form data

***

## Key Vocab

- **Validation**: Validation is an automatic check to ensure that data entered is sensible and feasible.
- **Form**: An HTML form is used to collect user input. The user input is most often sent to a server for processing.

***

## Introduction

What is WTFroms?

WTForms is a flexible forms validation and rendering library for Python web development. It can work with whatever web framework and template engine you choose. It supports data validation, CSRF protection and more.

What is Flask-WTF?

Flask-WTF is a library that integrates WTForms with Flask. It adds some extra things to
WTForms that help us with rendering and security.

***

## Creating a Form class

First we need to import

```py
from flask_wtf import FlaskForm
```

Lets create a class that will inherit from FlaskForm.

```py
class NameForm(FlaskForm):
    pass

```

Now we need to add form fields using wtforms.

The NameForm will have a textbox and a submit button.
We will use the StringField and SubmitField classes from wtform.

```py
from wtforms import StringField, SubmitField
```

Now we can use these classes to instantiate instance variables for the NameForm class.

```py
class NameForm(FlaskForm):
    name = StringField('What is your name')
    submit = SubmitField('Submit')
```

***

## Validators

Validators allow us to add rules that we want to apply to the fields. Lets look into some validators provided by wtforms. We can import the validators we need using

```py
from wtforms.validators import InputRequired
```

```py
class NameForm(FlaskForm):
    name = StringField('What is your name', validators=[InputRequired()])
    submit = SubmitField('Submit')
```

The `InputRequired()` validator makes the name StringField required. There are many more validators that
wtforms has for us like the `Email()` and `length()` validator.

 To see the full list go to [wtforms validators](https://wtforms.readthedocs.io/en/stable/validators/#built-in-validators)

## CSRF token

The FlaskForm class that we inherited NameForm from, gives us a hidden field for csrf_token. The csrf_token prevents against Cross-Site Request Forgery. We can include this token in our template `index.html` file using `{{ form.csrf_token }}`.

```py
app.config['SECRET_KEY'] = 'key'

```

## Form validation

The following functions are inherited from `WTForms` module

### form.is_submitted()

This function returns true if all fields of a form have been filled completely by the user. It does not check if the inputs are valid.

### form.validate()

This function returns true if all the conditions specified in the validators have been met.

### form.validate_on_submit()

Unlike the previous functions this function belongs to `Flask-WTF`. It returns true if both `form.is_submitted()` and
`form.validate()` return true.

## Error handling

### form.errors

If there are validation errors in the form. The errors can be found in the `forms.errors` dictionary

Here is an example of how we can use form.erros.

```py
    if form.validate_on_submit():
       print("Validation passed and submitted.")
    elif form.errors:
        print(form.errors.items())

```

## Conclusion

Flask-WTF can help us create and validate form data before pushing it to the backend for processing. Validating data can prevent
data type errors and help us create a more robust and error free program.

***

## Final Code

### app/main.py

```py
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)

# For CSRF token
app.config['SECRET_KEY'] = 'key'

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
```

### Template file `app/templates/index.html`

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
        {{ form.csrf_token }}
        {{ form.name() }}
        <br/>
        {{ form.submit()}}

    </form>
{% endif %}
</body>
</html>

```

***

## Resources

- [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)
