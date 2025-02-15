from flask import Flask, request, jsonify
import matlab.engine

app = Flask(__name__)

# Start MATLAB engine
eng = matlab.engine.start_matlab()

@app.route('/')
def home():
    return "MATLAB API is running!"

@app.route('/calculate_gear_ratio', methods=['POST'])
def calculate_gear_ratio():
    data = request.json
    input_gear = data.get("input_gear")
    output_gear = data.get("output_gear")

    # Convert values to MATLAB format
    input_gear = matlab.double([input_gear])
    output_gear = matlab.double([output_gear])

    # Call MATLAB function (to be created next)
    result = eng.calculate_gear_ratio(input_gear, output_gear)

    return jsonify({"gear_ratio": result})

if __name__ == '__main__':
    app.run(debug=True)
