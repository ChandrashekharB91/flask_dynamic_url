from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return f"Welcome to the Flak app with the dynamic content"

@app.route("/greet")
def greet():
    user_name = request.args.get('name', 'Guest')

    return  render_template("greet.html", user_name = user_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)