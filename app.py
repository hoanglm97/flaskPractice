from flask import Flask, render_template

app = Flask(__name__)

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


@app.route('/content')
def content_page():
    return render_template("content.html", demo=demo, title='About')


if __name__ == '__main__':
    app.run(debug=True)  # set debug mode = true, auto reload code without ctrl + C
