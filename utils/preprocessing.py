import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

def initialize_encoders():
    encoders = {
        'Age': OrdinalEncoder(categories=[['15-20', '20-30', '30-40', '40 or above']]),
        'Gender': OrdinalEncoder(categories=[['Male', 'Female']]),
        'FreeTimeActivity': OrdinalEncoder(categories=[
            ['Reading a book in the garden during summer.', 'Playing sports with your friends.', 
             'Embracing your artistic skills by painting or sketching.', 'Lying on your couch and watching Netflix.', 
             'Developing your skills in trading or learning about the financial market.', 
             'Writing and developing programming codes.', 'Thinking about business ideas while watching Shark Tank.']
        ]),
        'WorkEnvironment': OrdinalEncoder(categories=[
            ['Office setting', 'Laboratory', 'Studio/Workshop', 'Remote/Work from home', 'Retail/Customer-facing']
        ]),
        #'SkillsStrengths': OrdinalEncoder(categories=[
         #   ['Communication', 'Critical thinking', 'Creativity', 'Technical skills', 'Leadership', 'Organization', 'Marketing and Sales']
        #]),
        'TechComfort': OrdinalEncoder(categories=[
            ['Very comfortable', 'Comfortable', 'Neutral', 'Uncomfortable', 'Very uncomfortable']
        ]),
        'JobSecurityImportance': OrdinalEncoder(categories=[
            ['Very important', 'Important', 'Neutral', 'Not very important', 'Not important at all']
        ]),
        'ArtisticExpressionImportance': OrdinalEncoder(categories=[
            ['Essential, I thrive on creativity', 'Very important, it\'s a significant part of who I am',
             'Moderately important, I enjoy creative pursuits', 'Not very important, I prefer practical tasks',
             'Not important at all, I focus on other aspects of life']
        ]),
        'PhysicalFitnessImportance': OrdinalEncoder(categories=[
            ['Very important, I prioritize fitness and health', 'Important, I try to stay active regularly',
             'Moderately important, I enjoy physical activities occasionally', 'Not very important, fitness is not a priority for me']
        ]),
        'FinancialAnalysisApproach': OrdinalEncoder(categories=[
            ['I enjoy analyzing financial reports and making informed decisions.', 
             'I can perform financial analysis tasks but prefer other responsibilities.',
             'Neutral, I haven\'t had much experience in financial analysis and decision-making.',
             'Not interested in this']
        ]),
        'ProgrammingInterest': OrdinalEncoder(categories=[
            ['Yes, I have experience or a strong interest in these areas',
             'Somewhat, I\'m interested in learning more', 'Neutral, I haven\'t explored technical fields',
             'No, technical fields don\'t appeal to me']
        ]),
        'EntrepreneurshipInterest': OrdinalEncoder(categories=[
            ['Yes, I aspire to be an entrepreneur or business owner', 
             'Somewhat, I\'m open to entrepreneurial opportunities', 
             'Neutral, I haven\'t considered entrepreneurship', 
             'No, entrepreneurship isn\'t my career goal']
        ]),
        'ContentCreationEnjoyment': OrdinalEncoder(categories=[
            ['Yes, I\'m passionate about media and communication',
             'Somewhat, I find these areas interesting',
             'Neutral, I haven\'t considered media and communication careers',
             'No, media and communication aren\'t my focus']
        ]),
        'PublicServicePassion': OrdinalEncoder(categories=[
            ['Yes, very much', 'Yes, somewhat', 'Neutral', 'No, not at all']
        ]),
        'ComplexConceptsExplanation': OrdinalEncoder(categories=[
            ['Yes, I excel in explaining concepts to others', 'Somewhat, I\'m capable of explaining concepts',
             'Neutral, I haven\'t assessed my ability in this area', 'No, explaining concepts isn\'t my strength']
        ]),
        'PublicSpeakingComfort': OrdinalEncoder(categories=[
            ['Yes, I excel in public speaking, journalism, or digital media', 
             'Somewhat, I have some experience in these areas', 
             'Neutral, I haven\'t assessed my skills in public speaking or journalism',
             'No , Public speaking isn’t interest of mine']
        ]),
        'ToolsMachineryComfort': OrdinalEncoder(categories=[
            ['Yes, I\'m comfortable with tools and machinery', 
             'Somewhat, I have some experience with specialized equipment',
             'Neutral, I haven\'t assessed my comfort level', 'Uncomfortable',
             'No, working with tools and equipment isn\'t my preference']
        ]),
        'StrategicPlanningEnjoyment': OrdinalEncoder(categories=[
            ['Yes, I thrive in leadership roles and enjoy strategic planning',
             'Somewhat, I can handle leadership and decision-making responsibilities',
             'Neutral, I haven\'t assessed my interest in business management',
             'No, business management isn\'t my strength or interest']
        ]),
        'ExperimentationEnjoyment': OrdinalEncoder(categories=[
            ['Yes, I\'m passionate about scientific inquiry', 
             'Somewhat, I find research intriguing', 'Neutral',
             'Not really, research isn\'t my area of interest']
        ]),
        'KnowledgeSharing': OrdinalEncoder(categories=[
            ['Yes, teaching is fulfilling for me', 'Somewhat, I find it rewarding occasionally',
             'Neutral, I haven\'t considered teaching', 'No, teaching isn\'t a career path I\'m interested in']
        ]),
        'HelpingOthersDesire': OrdinalEncoder(categories=[
            ['Yes, caring for others is important to me', 'Somewhat, I\'m interested in healthcare',
             'Neutral', 'Not really, caregiving isn\'t my priority']
        ]),
        'MedicalInterest': OrdinalEncoder(categories=[
            ['Yes, I\'m passionate about healthcare', 'Somewhat, I\'m curious about medical fields',
             'Neutral', 'Not really, healthcare isn\'t my area of interest']
        ]),
        'MarketTrendsInterest': OrdinalEncoder(categories=[
            ['Very interested', 'Interested', 'Neutral', 'Not very interested', 'Not interested at all']
        ]),
        'SportsManagementInterest': OrdinalEncoder(categories=[
            ['Yes, I enjoy coaching and organizing sports activities', 'Somewhat, I might consider it',
             'Neutral, I\'m unsure', 'No, I prefer participating rather than organizing']
        ]),
        'SportsPassion': OrdinalEncoder(categories=[
            ['Very passionate', 'Passionate', 'Neutral', 'Not very passionate', 'Not passionate at all']
        ]),
        'FinanceManagementInterest': OrdinalEncoder(categories=[
            ['Yes, very much', 'Yes, somewhat', 'Neutral', 'Not really', 'No, not at all']
        ]),
        'TechnologyCuriosity': OrdinalEncoder(categories=[
            ['Yes, I\'m interested in these fields', 'Somewhat, I\'m curious to learn more',
             'Neutral', 'Not really, scientific disciplines aren\'t my focus']
        ]),
        'EducationalContentInterest': OrdinalEncoder(categories=[
            ['Yes, very much', 'Yes, somewhat', 'Neutral', 'Not really', 'No, not at all']
        ]),
        'FashionInterest': OrdinalEncoder(categories=[
            ['Yes, very much', 'Yes, somewhat', 'Neutral', 'Not really', 'No, not at all']
        ]),
        'FinancialStatementsRole': OrdinalEncoder(categories=[
            ['They are crucial for assessing financial health and making informed decisions.',
             'I understand their importance but prefer other aspects of business decision-making.',
             'Neutral, I haven\'t considered the role of financial statements in decision-making',
             'I don\'t have any idea but I am keen to explore this field',
             'I don\'t have any idea and I am not interested in it']
        ])
    }
    
    return encoders

def preprocess(data, encoders):
    # Ensure all required features are present
    required_features = [
        'Age', 'Gender', 'FreeTimeActivity', 'WorkEnvironment', 'SkillsStrengths', 'TechComfort', 'JobSecurityImportance', 
        'ArtisticExpressionImportance', 'PhysicalFitnessImportance', 'FinancialAnalysisApproach', 
        'ProgrammingInterest', 'EntrepreneurshipInterest', 'ContentCreationEnjoyment', 
        'PublicServicePassion', 'ComplexConceptsExplanation', 'PublicSpeakingComfort', 
        'ToolsMachineryComfort', 'StrategicPlanningEnjoyment', 'ExperimentationEnjoyment', 
        'KnowledgeSharing', 'HelpingOthersDesire', 'MedicalInterest', 'MarketTrendsInterest', 
        'SportsManagementInterest', 'SportsPassion', 'FinanceManagementInterest', 
        'TechnologyCuriosity', 'EducationalContentInterest', 'FashionInterest', 
        'FinancialStatementsRole'
    ]

    # Create DataFrame with correct columns
    data = pd.DataFrame([data], columns=required_features)
    
    # Apply ordinal encoding
    for feature, encoder in encoders.items():
        if not hasattr(encoder, 'categories_'):
            raise ValueError(f"Encoder for feature '{feature}' is not fitted.")
        try:
            data[feature] = encoder.transform(data[[feature]])
        except Exception as e:
            print(f"Error transforming feature '{feature}': {e}")
            raise
    return data  # Convert DataFrame to numpy array
