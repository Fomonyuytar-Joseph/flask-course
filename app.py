from flask import Flask , request , make_response , render_template , redirect , url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 








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