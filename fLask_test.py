from flask import Flask
import random



app = Flask(__name__)


messages = [
    'Buna ziua. Astazi este o zi cu cer senin si mult soare!',
    'Salut. Bine te-am gasit. Eu am fost creat in baza la Flask!',
    'Hey, ce mai faci? Iti doresc mult succes pe drumul ales!',
    'Buna. Sper ca esti in toane bune astazi!'
]


@app.route("/")
def mesaj_aleator():
    return random.choice(messages)

if __name__ == '__main__':
    app.run()