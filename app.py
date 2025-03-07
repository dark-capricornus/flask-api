from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

# default routing
@app.route("/developer")
def devName():
    return "Harish"

# dynamic routing
@app.route("/ageCalculator/<int:curr_year>/<int:birth_year>",methods=["POST"])
def age_calculate(curr_year,birth_year):
    return f'Your current age as per  {curr_year} is {curr_year - birth_year} years.'

# payload routing
@app.route("/user",methods=["POST"])
def fetchUser():
    payload = request.json
    name = payload["name"]
    age = payload["age"]
    return  f'Hello {name} your age is {age}'

# routing with body
@app.route("/login",methods=['GET','POST'])
def userdata():
  name = request.args.get("name")
  pwd =  request.args.get("pwd")
  msg =  f'Welcome, {name}'
  res = {
      "message":msg,
      "status":200
  }     
  return jsonify(res)
 
if __name__ == "__main__":
     app.run(port=8080,debug=True)
