from flask import Flask, render_template, request
import salary as sal

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def hello():
    salary_pred=0
    if request.method == "POST":
        hours = request.form["yrs"]
        salary_pred =  sal.salary_prediction(int(hours))
        
    sl = salary_pred
    
    return render_template("index.html", my_salary=sl)

# @app.route('/sub', methods = ["POST"])
# def submit():
#     if request.method == "POST":
#         first_name = request.form["username"]
    
#     return render_template("sub.html",n = first_name)


if __name__ == "__main__":
    app.run(debug=True)