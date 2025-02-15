import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Only import MATLAB Engine if running locally
if os.getenv("MATLAB_LOCAL", "False") == "True":
    import matlab.engine
    eng = matlab.engine.start_matlab()
else:
    eng = None  # Placeholder

@app.route('/')
def home():
    return "MATLAB API is running!"

@app.route('/calculate_gear_ratio', methods=['POST'])
def calculate_gear_ratio():
    data = request.json
    input_gear = data.get("input_gear")
    output_gear = data.get("output_gear")

    if eng:  # If MATLAB is available locally
        input_gear = matlab.double([input_gear])
        output_gear = matlab.double([output_gear])
        result = eng.calculate_gear_ratio(input_gear, output_gear)
        return jsonify({"gear_ratio": result})
    else:  # Running on Render, MATLAB is not available
        return jsonify({"error": "MATLAB Engine is not available on Render"}), 503

if __name__ == '__main__':
    app.run(debug=True)
