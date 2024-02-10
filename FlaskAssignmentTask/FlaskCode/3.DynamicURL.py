#importing the flask Module
from flask import Flask
 
# Flask constructor takes the name of
# current module (__name__) as argument
app = Flask(__name__)
 
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
    return 'You are at home page.'
 
# Use of <converter: variable name> in the 
# route() decorator.
@app.route('/allow/<int:Number>')
def allow(Number):
    if Number < 25:
        return f'You have been allowed to enter because your number is {str(Number)}'
    else:
       return f'You are not allowed'
 
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()