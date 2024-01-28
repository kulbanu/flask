from flask import Flask, request, jsonify
from flask_cors import CORS
import g4f

app = Flask(__name__)
CORS(app)

@app.route('/answer', methods=['POST'])
def answer():
    prompt = request.json['prompt']
    print(prompt);
    response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": prompt}])
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)