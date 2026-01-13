from flask import Flask, render_template, redirect, url_for,flash

from forms import RegistrationForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "my-secret-key"


@app.route('/', methods=['GET', 'POST'])

def register():
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        flash(f"Account created for {name} with email {email}!", "success")
        return redirect(url_for('sucess'))
    
    return render_template('register.html', form=form)

@app.route('/sucess')
def sucess():
    return render_template('sucess.html') 

if __name__=="__main__":
    app.run(debug=True)

