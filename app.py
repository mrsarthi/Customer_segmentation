from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__, template_folder="templates")


def run_segmentation():
    # Run your model script and capture output
    result = subprocess.run(
        ["python", "customer_segmentation.py"], capture_output=True, text=True)
    return result.stdout  # Return model results as text


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/run', methods=['POST'])
def run():
    output = run_segmentation()
    return jsonify({'output': output})  # Send output to frontend as JSON


if __name__ == '__main__':
    app.run(debug=True)
