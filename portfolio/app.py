from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "defaultsecret")

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
mail = Mail(app)

# splash page
@app.route('/', methods=['GET'])
def splash():
    return render_template('splash.html')

# portfolio page + contact form
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(
            subject=f"New Contact from {name}",
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']],
            body=f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        )
        try:
            mail.send(msg)
            flash("Your message has been sent successfully!", "success")
        except Exception as e:
            flash(f"Error sending message: {e}", "danger")
        return redirect('/home#contact')

    return render_template('index.html')

# FAQ page
@app.route('/faq')
def faq():
    return render_template('faq.html')

# Only needed when running locally
if __name__ == '__main__':
    app.run()
