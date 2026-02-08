from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Load trained model
with open('mini_prj.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        features = [float(x) for x in request.form.values()]
        features = np.array(features).reshape(1, -1)
        # Predict using model
        prediction = model.predict(features)[0]
        return render_template('index.html', prediction_text=f"Predicted Price: ₹{prediction:,.2f}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
