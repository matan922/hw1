import json
from flask import Flask


app = Flask(__name__,static_url_path='/static')

contacts=[]
DATA="contacts.json"
def load():
    with open(DATA, "r") as f:
        return json.load(f)

def save():
    with open(DATA,"w") as f:
        return json.dump(contacts,f,indent=4)


@app.route("/", methods=['GET','POST'])
def hello_world():
    return """<p>hello world</p>
    <a href='/about/'>About</a>
    <a href='/search/'>Search</a>
    <a href='/add-json'>Add json</a>
    <a href='/remove-json/'>Remove json</a>
    """

@app.route("/about/<int:id>")
@app.route("/about/")
def about(id=0):
    if id == 0:
        return contacts
    elif 0 < id <len(contacts)+1:
        return contacts[id-1]
    else:
        return "ID not found"


@app.route("/add-json")
@app.route("/add-json/<name>/<int:age>")
def add_json(name,age):
    contacts.append({"name":name, "age":age})
    save()
    return contacts


@app.route("/search")
@app.route("/search/<name>")
def search(name):
    for contact in contacts:
        if contact["name"] == name:
            return contacts
    


@app.route("/remove-json")
@app.route("/remove-json/<name>")
def remove_json(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            save()
            return contacts


app.run(debug=True)
