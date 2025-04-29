import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

# Load the dataset
data = pd.read_csv('Housing.csv')

# Feature columns (adjust as per the dataset structure)
features = ['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 
            'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus']
X = data[features]
y = data['price']

# Encode categorical variables
X = pd.get_dummies(X, drop_first=True)

# Save column order (needed later)
model_data = {'columns': X.columns.tolist()}

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Save model coefficients and intercept
model_data['coef'] = model.coef_.tolist()
model_data['intercept'] = model.intercept_

# Save the model data
model_dir = r'C:\Users\Divya\Downloads\devops\House-price-predictor\models'
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, 'model.pkl')
pickle.dump(model_data, open(model_path, 'wb'))

print(f'Model saved to {model_path}')
