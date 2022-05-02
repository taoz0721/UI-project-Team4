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
            "https://2.bp.blogspot.com/-e-mmKK8Lud4/XFXm_-VVRhI/AAAAAAAABK0/tPvppYyYoNkiy7F9RsjbYMtrXHXXOo4RQCLcBGAs/s1600/Hilarious%2Bcat%2BGIF%2B%25E2%2580%25A2%2BCrazy%2Bcat%2Bscared%2Bof%2Bhis%2Bown%2Breflection%2Bin%2Bthe%2Bmirror%2Bhaha.gif": "Aggression",
            "https://media0.giphy.com/media/MpNy5P7x5vWM0/giphy.gif?cid=790b7611fe2dddb7cce9113fe2f66ef5834739e834221e62&rid=giphy.gif&ct=g": "Anxiety/Fear",
            "https://media0.giphy.com/media/Ter8NaRzBVjGGk6MRS/giphy.gif?cid=790b7611ffddb9550ac8ec9f5f5868f1b5c7c772e50bbd55&rid=giphy.gif&ct=g": "Confident"
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
        "material":"https://akns-images.eonline.com/eol_images/Entire_Site/201478/rs_500x281-140808101812-tumblr_n4jwzrs6tK1spy7ono1_500.gif?fit=around%7C500:281&output-quality=90&crop=500:281;center,top",
        "answer":"False"
    },
    "3":{
        "type": "Drag",
        "area": "tails",
        "question":"Drag to match the image with the corresponding emotion according to the hints of tails.",
        "material":{
            "https://c.tenor.com/8erPxXJ65nIAAAAM/cat-waddling.gif": "Friendly",
            "https://c.tenor.com/z4ojU1xR-qoAAAAC/cat-funny-cat.gif": "Terrified",
            "https://c.tenor.com/ZPWp8yBockgAAAAC/annoyed-cat.gif": "Irritated"
        },
        "tags":[
            "Irritated",
            "Friendly",
            "Terrified"
        ]
    },
    "4":{
        "type": "Drag",
        "area": "earsandeyes",
        "question":"Drag to match the image with the corresponding emotion according to the hints of ears and eyes.",
         "material":{
            "https://thumbs.gfycat.com/BlindKeyCowrie-size_restricted.gif": "Angery",
            "https://i.pinimg.com/originals/e9/60/fa/e960fad6069ff3f5b6c8a27b31f1c1e5.gif": "Attentive",
            "https://i.chzbgr.com/full/9566880512/hA3C5065B/cat": "Comfortable"
        },
        "tags":[
            "Attentive",
            "Comfortable",
            "Angery"
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
user_answer={
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

@app.route('/quiz')
def quiz():
    global body_data
    global progress

    progress.append("quiz")
    return render_template('quiz_start.html')

@app.route('/quiz/<index>')
def bodyQuiz(index=None):
    global quiz_data
    global progress
    global save

    progress.append("quiz")
    print(save[index])
    if save[index]==False:
        
        return render_template('bodyQuiz.html', data=quiz_data[index], index=index, save=save[index])
    else:
        print(user_answer[index])
        return render_template('quiz_saved.html', data=quiz_data[index], index=index, user_answer=user_answer[index])

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
    global user_answer

    answer = request.get_json()
    print(answer)
    idx=answer["idx"]
    score=answer["score"]
    save[idx]=answer["save"]
    user_score[int(idx)-1]=score

    #if answer["type"]=="TF":
    user_answer[idx]=answer["answer"]
    
    return jsonify(user_score=user_score, answer=score, save=save[idx])

@app.route('/quiz_check_save', methods=['POST'])
def quiz_check_save():
    global save

    idx= request.get_json()

    
    return jsonify(save=save[idx])

@app.route('/quiz_redo', methods=['POST'])
def quiz_redo():
    global save
    global user_answer
    global user_score

    data_refresh= request.get_json()
    save=data_refresh["save"]
    user_answer=data_refresh["user_answer"]
    user_score=data_refresh["user_score"]
    
    return jsonify(data=user_score)

@app.route('/result',methods=['GET', 'POST'])
def result():
    #global score
    global user_score
    global progress

    data=sum(user_score)
    print(user_score)
    progress.append("result")
    return render_template('result.html', data=data) 

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




