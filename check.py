import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.exceptions import NotFittedError

def preprocess(data, encoders):
    for feature, encoder in encoders.items():
        # Ensure encoder is fitted before transforming
        if not hasattr(encoder, 'categories_'):
            raise ValueError(f"Encoder for feature '{feature}' is not fitted.")
        data[feature] = encoder.transform(data[[feature]])
    return data

# Create mock data
data = pd.DataFrame({
    'age': ['20-30', '30-40', '15-20'],
    'gender': ['Male', 'Female', 'Male'],
    'free_time_activity': ['Reading a book in the garden during summer.', 'Playing sports with your friends.', 'Lying on your couch and watching Netflix.']
})

# Create dummy encoders and fit them
encoders = {
    'age': OrdinalEncoder(categories=[['15-20', '20-30', '30-40', '40 or above']]),
    'gender': OrdinalEncoder(categories=[['Male', 'Female']]),
    'free_time_activity': OrdinalEncoder(categories=[[
        'Reading a book in the garden during summer.',
        'Playing sports with your friends.',
        'Embracing your artistic skills by painting or sketching.',
        'Lying on your couch and watching Netflix.',
        'Developing your skills in trading or learning about the financial market.',
        'Writing and developing programming codes.',
        'Thinking about business ideas while watching Shark Tank.'
    ]])
}

# Fit encoders
for feature, encoder in encoders.items():
    encoder.fit(data[[feature]])

# Process data
try:
    processed_data = preprocess(data, encoders)
    print("Processed Data:")
    print(processed_data)
except ValueError as e:
    print(f"Error: {e}")
except NotFittedError as e:
    print(f"NotFittedError: {e}")

