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
    },
    {
        "src":"https://cdn.shopify.com/s/files/1/0025/1373/1702/files/Cat_lying_on_its_back_with_tail_in_the_air_medium.gif?v=1537362532",
        "id":"Lie on Back",
        "description":["Trusting: ", "If your cat shows its tummy to you, it means that he/she really trusts you. BUT, it  IS NOT a tummy rub request. Some cats don't like tummy rubs."]
    }
]

tails_data=[
    {
        "src": "https://c.tenor.com/34emVVQvzPMAAAAM/cat-white-cat.gif",
        "id":"Friendly",
        "description":["Hight","Vibrating"]
    },
    {
        "src":"https://i.chzbgr.com/full/5410093568/hC859EDE5/scared-cat",
        "id":"Anxious, Terrified",
        "description":["Low/Down","Tucked - small target"]
    },
    {
        "src":"https://p1-tt.byteimg.com/origin/tos-cn-i-qvj2lq49k0/32b24969f9c64ed08c14fc549478e9b4",
        "id":"Irritated, Upset",
        "description":["Flicking/Agitation", "Lack of receptivity - back off"]
    }
]
ears_eyes_data=[
    {
        "src":"https://c.tenor.com/aZMOFP1N5TEAAAAM/angry-cat-triggered.gif",
        "id": "Angery, Fearful",
        "description":{"Ears": "Flatten Down", "Eyes": "Large and Dilated"}
    },
    {
        "src":"https://thumbs.gfycat.com/ImmediateCleanAmericankestrel-size_restricted.gif",
        "id": "Curious, Excited (Hunting)",
        "description":{"Ears": "Hight and Erect", "Eyes": "Large and Dilated"}
    },
    {
        "src":"https://i.gifer.com/ziH.gif",
        "id": "Attentive",
        "description":{"Ears": "Hight and Erect", "Eyes": "Narrow and Constricted"}
    },
    {
        "src":"https://c.tenor.com/BjPLwhBwD1oAAAAM/ryuzcn.gif",
        "id": "Content, Relaxed, Comfortable",
        "description":{"Ears": "Forwards", "Eyes": "Slow Blink"}
    }
]
body_quiz_data=[
    {
        "question":"When a cat lie on its back like the video below, it definitely means that it requests a tummy rub.",
        "material":"https://cdn.shopify.com/s/files/1/0025/1373/1702/files/Cat_lying_on_its_back_with_tail_in_the_air_medium.gif?v=1537362532",
        "answer":"False",
        "type": "TF"
    }
]
progress=[]
score=1




# ROUTES

@app.route('/')
def homepage():
    global progress

    progress.append("home")
    return render_template('homepage.html')   

@app.route('/body')
def body():
    global body_data
    global progress

    progress.append("body")
    return render_template('body.html', data=body_data)

@app.route('/quiz/body')
def bodyQuiz():
    global body_quiz_data
    global progress
    global score

    progress.append("quiz/body")
    return render_template('bodyQuiz.html', data=body_quiz_data, score=score)  

@app.route('/tails')
def tails():
    global tails_data
    global progress

    progress.append("")
    return render_template('tails.html', data=tails_data) 

@app.route('/earsandeyes')
def earsAndeyes():
    global ears_eyes_data
    global progress

    progress.append("earsandeyes")
    return render_template('earsAndeyes.html', data=ears_eyes_data)

@app.route('/result')
def result():
    global score
    global progress

    progress.append("result")
    return render_template('result.html', data=score) 

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




