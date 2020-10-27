from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/check/<input>', methods=['GET'])
def chekcOutput(input):
    lowerLetter, upperLetter, specialSign = false

if __name__ == '__main__':
    app.run(port=25000)
