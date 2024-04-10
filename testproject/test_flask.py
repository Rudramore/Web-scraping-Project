from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_query', methods=['POST'])
def process_query():
    # Ensure that the request contains JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()
    
    # Extract the free text query from the JSON data
    query = data.get('query', '')
    
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    # Process the query here (this step is up to you)
    # For demonstration, we'll just echo the query back
    processed_query = f"Processed query: {query}"
    
    # Return the processed query as a JSON response
    return jsonify({"processed_query": processed_query})

if __name__ == '__main__':
    app.run(debug=True)