from flask import Flask, render_template, request, jsonify, send_file
import model_api
from io import BytesIO

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

        ollama_response = model_api.send_prompt(userMessage)
        # Handle the data (for example, just return it)
        print(ollama_response)
        response = {
            "serverMessage": ollama_response
        }
        return jsonify(response), 200
    else:
        # Handle cases where JSON is not provided
        return jsonify({"error": "Invalid JSON data"}), 400

# in the end the model should give the user a link in chat, in a form:
# <a href="/taxform.xml">Download generated taxform XML</a>

@app.route('/taxform.xml')
def get_xml():
    file_data = BytesIO()


    xmlstring = model_api.generated_xml
    print(xmlstring)

    file_data.write(xmlstring.encode('utf-8'))
    file_data.seek(0)

    return send_file(file_data, as_attachment=True, download_name="taxform.xml", mimetype='text/xml')

    return r

