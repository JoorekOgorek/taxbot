from flask import Flask, render_template, request, jsonify, Response

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

        # Handle the data (for example, just return it)
        response = {
            "serverMessage": "You just sent me " + str(userMessage)
        }
        return jsonify(response), 200
    else:
        # Handle cases where JSON is not provided
        return jsonify({"error": "Invalid JSON data"}), 400

@app.route('/taxform.xml')
def get_xml():
    xmlstring = """<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>"""

    r = Response(response=xmlstring, status=200, mimetype='text/xml')
    # r.headers["Content-Type"] = "text/xml; charset=utf-8"
    return r

