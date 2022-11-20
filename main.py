from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

#Formularios
class Form1(FlaskForm):
  email1 = StringField('Email:', validators=[Email()])
  botao1 = SubmitField('Enviar1')

class Form2(FlaskForm):
  email2 = StringField('Email:', validators=[Email()])
  botao2 = SubmitField('Enviar2')

@app.route('/', methods=['GET', 'POST'])
def index():
  form1 = Form1()
  form2 = Form2()
  if form1.validate_on_submit() and 'botao1' in request.form:
    return 'Enviou 1'
  if form2.validate_on_submit() and 'botao2' in request.form:
    return 'Enviou 2'
  return render_template('index.html', form1=form1, form2=form2)

app.run(host='0.0.0.0', port=81)
