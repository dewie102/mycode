#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   A simple Flask server. Responds to HTTP 'GET /' requests
   with a 'Hello World' attached to a 200 response"""


# An object of Flask class is our WSGI application
from flask import Flask, redirect, url_for

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function


# aux1.com/characters/zack romasz

@app.route("/characters/<somename>")
def alpha(somename):
    return f"You know nothing, {somename}"

# lazy people often write "char" instead of "characters"abs(

@app.route("/char/<somename>")
def bravo(somename):
    #return redirect(f"/characters/{somename}")
    # url_for will look up the "url for" a given FUNCTION NAME
    return redirect(url_for("alpha", somename = somename))

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=2224) # runs the application
    app.run(host="0.0.0.0", port=2224, debug=True)  # DEBUG MODE
