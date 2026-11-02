from flask import Flask, request, make_response, render_template, redirect, url_for, session ,flash

app = Flask(__name__)
app.secret_key = "SECRET KEY"


@app.route("/", )
def index():
    return render_template("index.html", message="Index")


@app.route("/set_data")
def set_data():
    session["name"] = "Mike"
    session["other"] = "Hello World"
    return render_template("index.html", message="Session data Set")


@app.route("/get_data")
def get_data():
    if "name" in session.keys() or "other" in session.keys():
        name = session["name"]
        other = session["other"]
        return render_template("index.html", message=f"name = {name} other: {other}")
    else:
        return render_template("index.html", message="No session data found")


@app.route("/clear_session")
def clear_session():
    session.clear()
    session.pop("name")
    return render_template("index.html", message="session cleared")

@app.route("/set_cookie")
def set_cookie():
    response = make_response(render_template("index.html", message="Set Cookie"))
    response.set_cookie("cookie_name" , "cookie_value")
    return response

@app.route("/get_cookie")
def get_cookie():
    cookie_value = request.cookies["cookie_name"]
    return render_template("index.html", message=f"Cookie Value: {cookie_value}")

@app.route("/remove_cookie")
def remove_cookie():
    response = make_response(render_template("index.html", message="Remove Cookie"))
    response.set_cookie("cookie_name" , expires=0)
    return response

@app.route("/login" , methods =["GET" , "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "joe" or password == "123":
            flash("Logged in Successfully")
            return render_template("index.html", message="")
        else:
            flash("Login Failed!")
            return render_template("index.html", message="")






# def index():
#     myValue = "Joe"
#     result = 10 * 6
#     myList = [1,2,3,4,5,6,7,8]
#     return render_template("index.html" , myValue=myValue , result=result , myList=myList)

# @app.route("/other")
# def other():
#     some_text = "Some Text"
#     return render_template("other.html" , some_text=some_text)


# @app.route("/hello" , methods=["GET", "POST"])
# def hello():
#     return "Hello World\n" , 200

# @app.template_filter("reverse_string")
# def reverse(s:str):
#     return s[::-1]

# @app.route("/redirect_endpoint")
# def redirect_endpoint():
#     return redirect(url_for("other"))
    # if request.method == "GET":
    #     return "You made a GET request\n"
    # elif request.method == "POST":
    #     return "You made a POST request\n"
    # else:
    #     return "You will never see this message"
# @app.route("/greet/<name>")
# def greet(name):
#     return f"Hello {name}"
# @app.route("/add/<int:number1>/<int:number2>")
# def add(number1 , number2):
#     sum = number1 + number2
#     return f"The sum of {number1} and {number2} is {sum}"
# @app.route("/handle_params")
# def handle_params():
#     if "greeting" in request.args.keys() and "name" in request.args.keys():
#         greeting = request.args["greeting"]
#         name = request.args["name"]
#         return f"{greeting} {name}"
#     else:
#         return "Some parameters are missing."
if __name__ == '__main__':
    app.run(debug=True)
