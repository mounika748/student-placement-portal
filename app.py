from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        name = request.form["name"]
        skills = request.form["skills"]
        cgpa = float(request.form["cgpa"])
        company = request.form["company"]

        if company == "Hashira":
            result = "Eligible for Hashira" if cgpa >= 7 else "Not Eligible for Hashira"

        elif company == "TCS":
            result = "Eligible for TCS" if cgpa >= 6.5 else "Not Eligible for TCS"

        elif company == "Infosys":
            result = "Eligible for Infosys" if cgpa >= 6 else "Not Eligible for Infosys"

        elif company == "Wipro":
            result = "Eligible for Wipro" if cgpa >= 6 else "Not Eligible for Wipro"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)