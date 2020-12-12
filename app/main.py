from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/create_owner")
def create_owner():
    return render_template("create_owner.html")

@app.route("/create_business")
def create_business():
    return render_template("create_business.html")

@app.route("/personal_business")
def personal_business():
    return render_template("personal_business.html")

@app.route("/create_password")
def create_password():
    return render_template("create_password.html")

@app.route("/confirmation_page")
def confirmation_page():
    return render_template("confirmation_page.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)