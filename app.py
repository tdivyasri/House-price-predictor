esfrom flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load model data
model_path = os.path.join(os.getcwd(), 'models', 'model.pkl')
model_data = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            area = float(request.form.get('Area in metres'))
            bedrooms = float(request.form.get('Bedrooms'))
            bathrooms = float(request.form.get('Bathrooms'))
            stories = float(request.form.get('Stories'))

            # Fill remaining dummy features as 0
            base_input = {'area': area, 'bedrooms': bedrooms, 'bathrooms': bathrooms, 'stories': stories}
            for col in model_data['columns']:
                if col not in base_input:
                    base_input[col] = 0

            df = pd.DataFrame([base_input])[model_data['columns']]
            prediction = np.dot(df.values, model_data['coef']) + model_data['intercept']

            return render_template('index.html', prediction_text=f'Predicted House Price: ${prediction[0]:,.2f}')
        except Exception as e:
            return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
