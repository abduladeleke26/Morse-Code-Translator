from flask import Flask, render_template, request

app = Flask(__name__)







@app.route('/')
def home():
    return render_template("index.html")

@app.route('/translate',methods = ['POST'])
def trans():
    text = request.form.get('statement')
    morse_code = translate(text)
    return render_template("index.html", morse=morse_code, textfr = text)

def translate(text):
    letters = list(text)

    morse_code = ""

    for i in range(len(letters)):
        if letters[i] == 'a':
            morse_code += "·− "

        elif letters[i] == 'b':
            morse_code += "−··· "

        elif letters[i] == 'c':
            morse_code += "−·−· "

        elif letters[i] == 'd':
            morse_code += "−·· "

        elif letters[i] == 'e':
            morse_code += "· "

        elif letters[i] == 'f':
            morse_code += "··−· "

        elif letters[i] == 'g':
            morse_code += "−−· "

        elif letters[i] == 'h':
            morse_code += "···· "

        elif letters[i] == 'i':
            morse_code += "·· "

        elif letters[i] == 'j':
            morse_code += "·−−− "

        elif letters[i] == 'k':
            morse_code += "−·− "

        elif letters[i] == 'l':
            morse_code += "·−·· "

        elif letters[i] == 'm':
            morse_code += "−− "

        elif letters[i] == 'n':
            morse_code += "−· "

        elif letters[i] == 'o':
            morse_code += "−−− "

        elif letters[i] == 'p':
            morse_code += "·−−· "

        elif letters[i] == 'q':
            morse_code += "−−·− "

        elif letters[i] == 'r':
            morse_code += "·−· "

        elif letters[i] == 's':
            morse_code += "··· "

        elif letters[i] == 't':
            morse_code += "− "

        elif letters[i] == 'u':
            morse_code += "··− "

        elif letters[i] == 'v':
            morse_code += "···− "

        elif letters[i] == 'w':
            morse_code += "·−− "

        elif letters[i] == 'x':
            morse_code += "−··− "

        elif letters[i] == 'y':
            morse_code += "−·−− "

        elif letters[i] == 'z':
            morse_code += "−−·· "

        elif letters[i] == '1':
            morse_code += "·−−−−  "

        elif letters[i] == '2':
            morse_code += "··−−−  "

        elif letters[i] == '3':
            morse_code += "···−−  "

        elif letters[i] == '4':
            morse_code += "····−  "

        elif letters[i] == '5':
            morse_code += "·····  "

        elif letters[i] == '6':
            morse_code += "−····  "

        elif letters[i] == '7':
            morse_code += "−−···  "

        elif letters[i] == '8':
            morse_code += "−−−··  "

        elif letters[i] == '9':
            morse_code += "−−−−·  "

        elif letters[i] == '0':
            morse_code += "−−−−−  "

        elif letters[i] == ' ':
            morse_code += "  "
        else:
            morse_code += letters[i]

    return morse_code








if __name__ == "__main__":
    app.run(debug=True)


