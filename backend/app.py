from flask import Flask, render_template, request, jsonify
import model_api
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def handle_api():
    if request.is_json:
        # Parse the JSON data
        data = request.get_json()
        userMessage = data["userMessage"]
        print(userMessage)

        ollama_response = model_api.run_ollama(userMessage)
        # Handle the data (for example, just return it)
        print(ollama_response)
        response = {
            "serverMessage": ollama_response
        }
        return jsonify(response), 200
    else:
        # Handle cases where JSON is not provided
        return jsonify({"error": "Invalid JSON data"}), 400
