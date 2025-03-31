import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

# ✅ Load the latest trained spam classifier model
with open("model2.pkl", "rb") as file:
    model = pickle.load(file)

# ✅ Load the latest trained TF-IDF vectorizer
with open("vectorizer3.pkl", "rb") as file:
    vectorizer = pickle.load(file)

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    email_text = data.get("email_text", "").strip()

    if not email_text:
        return jsonify({"error": "No email text provided"}), 400  # Handle empty input

    # ✅ Convert input text into the same format as training
    transformed_text = vectorizer.transform([email_text])

    # ✅ Predict using the trained model
    prediction = model.predict(transformed_text)[0]

    # ✅ Convert prediction to readable format
    result = "Spam" if prediction == 1 else "Not Spam"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
