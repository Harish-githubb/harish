from flask import *

app = Flask(__name__)

@app.route('/')

def index():
    return render_template ("index.html")


@app.route('/Register', methods=["POST"])

def Register():
    data=request.form
    Name=data["Name"]
    Age=data["Age"]
    phonenumber=data["Number"]
    Email=data["Email"]
    #Gender = "Male" if data.get("Male", 'off') == "on" else ("Female" if data.get("Female", 'off') == "on" else None)

    infos= {
       "Name":data.get("Name"),
       "Age":data.get("Age"),
       "Phonenumber":data.get("Number"),
       "Email":data.get("Email"),
       "Gender":"Male" if data.get("Male", 'off') == "on" else ("Female" if data.get("Female", 'off') == "on" else None)
          }
    # if data.get("Male","off")=="on":
    #    Gender="Male"
    # else:
    #    Gender="Female"


    # details = {
    #         "Name": data.get("Name"),
    #         "Age": data.get("Age"),
    #         "PhoneNumber": data.get("Number"),
    #         "Email": data.get("Email"),
    #         "Gender": "Male" if data.get("Male", 'off') == "on" else ("Female" if data.get("Female", 'off') == "on" else None)
    #     }
    # details=[Name,Age,phonenumber,Email,Gender]
    

    return render_template("results.html", infos=infos)






if __name__ == "__main__":
  app.run(host='127.0.0.1',port=5001,debug=True)



