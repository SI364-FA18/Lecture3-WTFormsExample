from flask import Flask, request, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you will never guess this'

class MyForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    address = StringField('Mailing Address', validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/showform')
def show_form():
  form_var = MyForm()
  return render_template('formdisplay.html',form=form_var)
  
@app.route('/seeresult', methods = ['POST'])
def see_result():
  form = MyForm()
  if form.validate_on_submit(): # If the form worked to submit 
      # We know we want data from form saved in vars name and address
      first_name = form.name.data
      the_address = form.address.data # right from the form
      # NOTE: Consider...what template would you want to write to render this data?
      # What should be in the file results.html?
      return render_template('results.html', name=first_name, addr=the_address)
  
  # We'll only get here if the if statement about the form being OK didn't evaluate to True
  return "Sorry, no data available."

if __name__ == "__main__":
    app.run(debug=True)
