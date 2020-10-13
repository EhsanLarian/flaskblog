from flask import Flask,render_template
from forms import RegistrationForm , LoginnForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a6bf1a009bb50d02e0e5d6af0bc72d89'
posts = [
    {
        'author'  : 'Ehsan Larian',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : '7/30/2020'

    },
    {
        'author'  : 'Ali Larian',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : '7/31/2020'

    }
]
@app.route('/')
@app.route('/home')
def Home():
    return render_template('home.html',posts=posts)
@app.route('/about')
def about():
    return render_template('about.html',title='About')
@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register',form=form)
@app.route('/login')
def login():
    form = LoginnForm()
    return render_template('login.html',title='Login',form=form)
if __name__ == '__main__':
    app.run(debug=True)