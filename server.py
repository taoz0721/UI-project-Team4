from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 2
data = [
    {
        "id": 1,
        "name": "michael scott"
    },
    {
        "id": 2,
        "name": "jim halpert"
    },
]
body_data=[
    {
        "src": "https://cdn-fastly.petguide.com/media/2022/02/16/8259958/what-does-a-cat-s-arched-back-mean.jpg",
        "id":"Arched body",
        "description":["Aggression: ","When a cat is FEARFUL or ANGRY, they will often make themselves as big as possible."]
    },
    {
        "src":"https://www.treehugger.com/thmb/QIn7TRcupWFqir0DCIYLTaqrZ3Q=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/tabby-cat-on-a-bed-862512230-2d351b8055254269aab1381e7c077f1e.jpg",
        "id":"Normal Posture",
        "description":["Confidence: ","If a cat is pointing its head or body to you, they might be RECEPTIVE to your advances."]
    },
    {
        "src":"https://www.nutravet.co.uk/sites/default/files/user/calm-cat.jpg",
        "id":"Ball Shaped",
        "description":["Anxiety/Fear: ", "The crouched down body position enables cat to spring off, should they feel the need."]
    }
]

# ROUTES

@app.route('/')
def homepage():
   return render_template('homepage.html')   

@app.route('/body')
def body():
    global body_data
    return render_template('body.html', data=body_data) 

@app.route('/hello/<name>')
def hello_name(name=None):
    return render_template('hello_name.html', name=name) 


@app.route('/people')
def people():
    return render_template('people.html', data=data)  


# AJAX FUNCTIONS

# ajax for people.js
@app.route('/add_name', methods=['GET', 'POST'])
def add_name():
    global data 
    global current_id 

    json_data = request.get_json()   
    name = json_data["name"] 
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    current_id += 1
    new_id = current_id 
    new_name_entry = {
        "name": name,
        "id":  current_id
    }
    data.append(new_name_entry)

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data = data)
 


if __name__ == '__main__':
   app.run(debug = True)




