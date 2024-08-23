from flask import Flask, render_template, request
from forms import ProfessionPredictionForm
import joblib
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Dictionary for mapping prediction results to professions
proff = {
    1: "Creative Arts and Design & Literature",
    2: "Sports and Recreation",
    3: "Social Services and Education",
    4: "Technical, Scientific and Healthcare",
    5: "Business and Management",
    6: "Finance and Accountancy"
}

# Load the trained model and encoders
model = joblib.load('model_prof.joblib')

encoders = joblib.load('encoder.joblib')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ProfessionPredictionForm()
    profession = None
    
    if form.validate_on_submit():
        # Extract data from the form
        data = {
            'Age': form.age.data,
            'Gender': form.gender.data,
            'Free Time Activity': form.free_time_activity.data,
            'Work Environment': form.work_environment.data,
            'Tech Comfort': form.tech_comfort.data,
            'JobSecurity Importance': form.job_security_importance.data,
            'Artistic Expression Importance': form.artistic_expression_importance.data,
            'Physical Fitness Importance': form.physical_fitness_importance.data,
            'Financial Analysis Approach': form.financial_analysis_approach.data,
            'Programming Interest': form.programming_interest.data,
            'Entrepreneurship Interest': form.entrepreneurship_interest.data,
            'Content Creation Enjoyment': form.content_creation_enjoyment.data,
            'Public Service Passion': form.public_service_passion.data,
            'Complex Concepts Explanation': form.complex_concepts_explanation.data,
            'Public Speaking Comfort': form.public_speaking_comfort.data,
            'Tools Machinery Comfort': form.tools_machinery_comfort.data,
            'Strategic Planning Enjoyment': form.strategic_planning_enjoyment.data,
            'Experimentation Enjoyment': form.experimentation_enjoyment.data,
            'Knowledge Sharing': form.knowledge_sharing.data,
            'Helping Others Desire': form.helping_others_desire.data,
            'Medical Interest': form.medical_interest.data,
            'Market Trends Interest': form.market_trends_interest.data,
            'Sports Management Interest': form.sports_management_interest.data,
            'Sports Passion': form.sports_passion.data,
            'Finance Management Interest': form.finance_management_interest.data,
            'Technology Curiosity': form.technology_curiosity.data,
            'Educational Content Interest': form.educational_content_interest.data,
            'Fashion Interest': form.fashion_interest.data,
            'Financial Statements Role': form.financial_statements_role.data,
        }

        # Convert the data to a DataFrame for encoding
        data_df = pd.DataFrame([data])
        
        
            # Apply encoders
        preprocessed_data = encoders.transform(data_df)
            # print(preprocessed_data)
            # Make prediction
        prediction = model.predict(preprocessed_data)
        result = int(prediction[0])
            
            # Map the result to profession
        profession = proff.get(result, "Unknown Profession")
        
           

    return render_template('index.html', form=form, result=profession)

if __name__ == '__main__':
    app.run(debug=True)
