from flask import Flask, request, jsonify
from flask_cors import CORS
import g4f

app = Flask(__name__)
CORS(app, resources={r"/api/answer*": {"origins": "*"}})

@app.route('/api/answer', methods=['POST'])
def answer():
    prompt = request.json['prompt']
    print(prompt);
    response = g4f.ChatCompletion.create(
    model=g4f.models.gemini_pro,
    messages=[{"role": "user", "content": prompt}])
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
