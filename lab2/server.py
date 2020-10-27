from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/check/<string:input>')
def chekcOutput(input):
    lowerCase = False
    upperCase = False
    digit = False
    specialSign = False
    
    for i in input:
        if i >= 'A' and i <= 'Z':
            upperCase = True
        elif i >= 'a' and i <= 'z':
            lowerCase = True
        elif i >= '0' and i <= '9':
            digit = True
        else:
            specialSign = True

    return jsonify({'lowerCase': lowerCase,
                    'upperCase': upperCase,
                    'digit': digit,
                    'specialSign': specialSign
                    })

if __name__ == '__main__':
    app.run(port=25000)
