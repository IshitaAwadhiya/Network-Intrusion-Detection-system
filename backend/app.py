# from flask import Flask, jsonify, request
# from intrusion_detection import detect_intrusion

# app = Flask(__name__)

# # @app.route('/')
# # def home():
# #     return "API is working!"


# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json  # expects JSON with 'features'
#     result = detect_intrusion(data['features'])  # not [['features']]
#     return jsonify({"result": result})

# # if __name__ == '__main__':
# #     app.run(debug=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)


from flask import Flask, request, jsonify
from flask_cors import CORS
from intrusion_detection import detect_intrusion
from db import log_intrusion, fetch_logs

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = data.get("features", [])
    prediction = detect_intrusion(features)
    log_intrusion(prediction, features)
    return jsonify({"result": prediction})

@app.route('/logs', methods=['GET'])
def logs():
    all_logs = fetch_logs()
    return jsonify([
        {"timestamp": row[0], "prediction": row[1], "features": row[2]}
        for row in all_logs
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
