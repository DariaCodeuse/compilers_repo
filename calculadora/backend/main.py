from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(main)
@app.route('/api/analyze', methods=['POST'])
def analyze_code():
    data = request.get_json()
    code 0 data.get('code', '')
    

if __name__ == '__main__':
    app.run(debug=True)
