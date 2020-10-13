"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <p>Hi! This is the home page.</p>
      <a href="/hello">Click Here!</a>
    </html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    newline = "\n"

    options = [
        f"<option value={compliment}>{compliment}</option>"
        for compliment in AWESOMENESS
    ]

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <div>
            <label for="person">What's your name?</label>
            <input type="text" name="person" id="person">
          </div>
          <div>
            <label for="compliment">Select a Compliment:</label>
            <select name="compliment" id="compliment" action="/greet">
              {newline.join(options)}
            </select>
          </div>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(
        player, compliment
    )


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
