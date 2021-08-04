from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def greeting(name):
    return f'Hello {name}'

@app.route('/repeat/<int:number>/<string:phrase>')
def repeater(number, phrase):
    return f"{phrase * number}"

@app.errorhandler(404)
def my_error(err_no):
    return "Sorry! No response.  Try again. (404)"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.