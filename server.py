from flask import Flask, g
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
quiz_data={
    "1": {
        "type": "Drag",
        "area":"body",
        "question":"Drag to match the image with the corresponding emotion according to the body shape.",
        "material": {
            "https://cdn-fastly.petguide.com/media/2022/02/16/8259958/what-does-a-cat-s-arched-back-mean.jpg": "Aggression",
            "https://www.nutravet.co.uk/sites/default/files/user/calm-cat.jpg": "Anxiety/Fear",
            "https://www.treehugger.com/thmb/QIn7TRcupWFqir0DCIYLTaqrZ3Q=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/tabby-cat-on-a-bed-862512230-2d351b8055254269aab1381e7c077f1e.jpg": "Confident"
        },
        "tags":[
            "Confident",
            "Anxiety/Fear",
            "Aggression"    
        ]
    },
    "2":{
        "type": "TF",
        "area":"body",
        "question":"When a cat lie on its back like the video below, it definitely means that it requests a tummy rub.",
        "material":"https://cdn.shopify.com/s/files/1/0025/1373/1702/files/Cat_lying_on_its_back_with_tail_in_the_air_medium.gif?v=1537362532",
        "answer":"False"
    },
    "3":{
        "type": "Drag",
        "area": "tails",
        "question":"Drag to match the image with the corresponding emotion according to the hints of tails.",
        "material":{
            "https://c.tenor.com/34emVVQvzPMAAAAM/cat-white-cat.gif": "Friendly",
            "https://i.chzbgr.com/full/5410093568/hC859EDE5/scared-cat": "Anxious",
            "https://p1-tt.byteimg.com/origin/tos-cn-i-qvj2lq49k0/32b24969f9c64ed08c14fc549478e9b4": "Irritated/Upset"
        },
        "tags":[
            "Irritated/Upset",
            "Friendly",
            "Anxious"
        ]
    },
    "4":{
        "type": "Drag",
        "area": "earsandeyes",
        "question":"Drag to match the image with the corresponding emotion according to the hints of ears and eyes.",
         "material":{
            "https://c.tenor.com/aZMOFP1N5TEAAAAM/angry-cat-triggered.gif": "Angery/Fearful",
            "https://i.gifer.com/ziH.gif": "Attentive",
            "https://c.tenor.com/BjPLwhBwD1oAAAAM/ryuzcn.gif": "Comfortable"
        },
        "tags":[
            "Attentive",
            "Comfortable",
            "Angery/Fearful"
        ]
    }
}
progress=[]
score=1
user_score = [0,0,0,0]
save={
    "1": False,
    "2": False,
    "3": False,
    "4": False
}
answer={
    "1": None,
    "2": None,
    "3": None,
    "4": None
}


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

@app.route('/quiz/<index>')
def bodyQuiz(index=None):
    global quiz_data
    global progress
    global save

    progress.append("quiz")
    if save[index]==False:
        return render_template('bodyQuiz.html', data=quiz_data[index], index=index, save=save[index])
    else:
        return render_template('quiz_saved.html', data=quiz_data[index], index=index,)

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

# for ajax function that achieve user's choice
@app.route('/quiz_get_result', methods=['POST'])
def quiz_get_result():
    global user_score
    global save

    answer = request.get_json()
    print(answer)
    idx=answer["idx"]
    score=answer["score"]
    save[idx]=answer["save"]
    user_score[int(idx)-1]=score
    return jsonify(user_score=user_score, answer=score, save=save[idx])

@app.route('/quiz_check_save', methods=['POST'])
def quiz_check_save():
    global save

    idx= request.get_json()

    
    return jsonify(save=save[idx])

@app.route('/result',methods=['GET', 'POST'])
def result():
    #global score
    global user_score
    global progress
    progress.append("result")
    return render_template('result.html', data=user_score) 

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




