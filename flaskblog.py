from flask import Flask,render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app=Flask(__name__)

app.config["SECRET_KEY"] = "ed21a83d34400e0244f8bfe689692b5f"

post = [
    {
        "author":"Daniel Estrada",
        "title":"Blog post 1",
        "content":"First post ouyea",
        "date_posted":"April 1 2024"
    },
    {
        "author":"Daniel Espinoza",
        "title":"Blog post 2",
        "content":"Second post ouyea",
        "date_posted":"April 2 2024"
    }

]

@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html", posts=post)

@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!","success") #Needs to be added to the template so it can be displayed
        return redirect(url_for("home"))
    return render_template('register.html', title='Register',form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login',form=form)

if __name__=="__main__":
    app.run(debug=True)