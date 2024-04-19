from flask import Flask
app=Flask(__name__)

@app.route('/') #Home
def hello():
    return """<html>
    <head>
    <title>HELLO</title>
    </head>
    <body>
    <h1>Hello World!</h1>
    <a href="/about">About</a>
    </body>
    </html>
 """

@app.route("/about") #about page

def about():
    return """<html>
    <head>
    <title>About this page</title>
    </head>
    <body>
    <h1>About</h1>
     <a href="/">Hello World</a>
    <p>Everything about Hello world!</p>
    </body>
    </html>
"""
if __name__=="__main__":
    app.run(debug=True)