import AIGPT
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message']
    answer = AIGPT.get_text(user_input)
    while answer == '':
        answer = AIGPT.get_text(user_input)
    return jsonify({'response': answer})

if __name__ == '__main__':
    app.run(debug=True)