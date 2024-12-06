from flask import Flask

app = Flask(__name__)


@app.route("/home")
def home():
    return "Hello, I am Anantheswar"

@app.route("/friend")
def Second():
    return "Neee verum M@app.route"

@app.route("/sreeja")
def forSreeja():
    return "Hey, Sreeja you are great.You are a great tutor,WOnderful,fantastic,elastic,gymnastic.......Advance Merry Christmas and Happy New Year 🎅🥳🍾🎇"


@app.route("/reema")
def forReema():
    return "Hey, Reema you are great.You are a great tutor,WOnderful,fantastic,elastic,gymnastic.......Advance Merry Christmas and Happy New Year 🎅🥳🍾🎇"

@app.route("/sadhika")
def forsadhika():
    return "Hey Sadhika Chechi, You are sooo good and sooo caring we love you sooo much espeaciallly me.Keep going like this. You are always in my prayers God bless you.Merry Christmas and Happy New Year 🥳🎅🍾😘🎇"
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
