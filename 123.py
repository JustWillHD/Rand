from flask import Flask, render_template
import psutil

maintenance = "false"

app = Flask(__name__)

@app.route('/')
def index():
    f = open("index.json", "r")
    return f.read()
    f.close()

@app.route('/check/<word>/<username>/<userid>')
def update(word, username, userid):
  if maintenance == "false":
    file = open("words.txt", "r")
    upperWord = word.upper()
    lowerWord = word.lower()
    words = file.read()
    splitWords = words.split("\n")
    if word in splitWords or upperWord in splitWords or lowerWord in splitWords:
        print("Search Return | Username:", username, " | User ID:", userid, " | Word:", word, "(Exists)")
        file.close()
        returnCode = open("wordFound.json", "r")
        return returnCode.read()
        returnCode.close()
    else:
        print("Search Return | Username:", username, " | User ID:", userid, " | Word:", word, "(Doesn't Exist)")
        file.close()
        returnCode = open("wordNotFound.json", "r")
        return returnCode.read()
        returnCode.close()
  else:
        print("MAINTENENCE! Returned a 503 Error to", username, "(", userid, ")")
        returnCode = open("maintenance.json", "r")
        return returnCode.read()
        returnCode.close()
  
@app.errorhandler(404)
def notfound():
  returnCode = open("wordNotFound.json", "r")
  return returnCode.read()
  returnCode.close()

if __name__ == "__main__": 
	app.run(
		host='0.0.0.0',
		port=80
  )
