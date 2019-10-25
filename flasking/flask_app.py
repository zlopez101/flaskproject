#import necessary functions
from flask import Flask, render_template, url_for

#instantiate a Flask class and set to 'app' variable
app = Flask(__name__)     

#dummy data
posts = [
    {
        'author':'Zach Lopez',
        'title':'My First Post',
        'content':'This is what I want to say',
        'date_posted': 'October 22, 2019'
    },
    {
        'author':'Jessica Spence',
        'title':'Responding  to First Post',
        'content':'I think you should have said it this way',
        'date_posted': 'October 23, 2019'
    }
]

#decorators for the home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='about')


if __name__ == '__main__':
    app.run(debug=True)