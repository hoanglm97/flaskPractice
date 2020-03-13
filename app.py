from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc5692d5a1204f21b4bcd49d30d2637b'
demo = [
    {
        'name': 'Le Minh Hoang',
        'age': '23',
        'date_of_birth': 'November 28, 1997',
        'job': 'Python Developer',
        'company': 'VCCloud'
    }
]


@app.route('/home')
def my_home():
    return render_template("home.html")


@app.route('/about')
def content_page():
    return render_template("about.html", demo=demo, title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)  # set debug mode = true, auto reload code without ctrl + C
