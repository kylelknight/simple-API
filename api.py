from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Define a simple route for the API
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the Simple API!",
        "status": "success"
    })

# A route to fetch a list of items
@app.route('/items', methods=['GET'])
def get_items():
    items = [
        {"id": 1, "name": "Item One"},
        {"id": 2, "name": "Item Two"},
        {"id": 3, "name": "Item Three"}
    ]
    return jsonify(items)

# A route to add a new item
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Invalid data"}), 400
    new_item = {"id": 4, "name": data['name']}
    return jsonify(new_item), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

