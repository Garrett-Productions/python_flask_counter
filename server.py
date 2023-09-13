from flask import Flask,render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = "Coding for the winnnnnn"


@app.route("/")
def index():
    if 'visit' in session:
        session['visit'] +=1
    else:
        session['visit'] = 1
    return render_template("index.html")


@app.route("/newRoute")
def byTwo():
    if 'visit' in session:
        session['visit'] +=2
    else:
        session['visit'] = 1
    return render_template("index.html")


@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port = 5001)