from flask import Flask, request, render_template, abort

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the registration form
    return render_template("index.html")

@app.route('/Register', methods=["POST"])
def Register():
    if request.method == "POST":
        data = request.form
        infos = {
            "Name": data.get("Name"),
            "Age": data.get("Age"),
            "Phonenumber": data.get("Number"),
            "Email": data.get("Email"),
            "Gender": "Male" if data.get("Male", 'off') == "on" else ("Female" if data.get("Female", 'off') == "on" else None)
        }
        # Render results page with collected information
        return render_template("results.html", infos=infos)
    else:
        # If the wrong request method is used, return 405 Method Not Allowed
        abort(405)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5678, debug=True)
