from utils.preprocessing import preprocess, initialize_encoders
encoders = initialize_encoders()
test_data = {
    'Age': '20-30',
    'Gender': 'Male',
    'FreeTimeActivity': 'Reading a book in the garden during summer.',
    'WorkEnvironment': 'Office setting',
    'SkillsStrengths': 'Communication',
    'TechComfort': 'Comfortable',
    'JobSecurityImportance': 'Important',
    'ArtisticExpressionImportance': 'Very important, it\'s a significant part of who I am',
    'PhysicalFitnessImportance': 'Important, I try to stay active regularly',
    'FinancialAnalysisApproach': 'I enjoy analyzing financial reports and making informed decisions.',
    'ProgrammingInterest': 'Yes, I have experience or a strong interest in these areas',
    'EntrepreneurshipInterest': 'Yes, I aspire to be an entrepreneur or business owner',
    'ContentCreationEnjoyment': 'Yes, I\'m passionate about media and communication',
    'PublicServicePassion': 'Yes, very much',
    'ComplexConceptsExplanation': 'Yes, I excel in explaining concepts to others',
    'PublicSpeakingComfort': 'Yes, I excel in public speaking, journalism, or digital media',
    'ToolsMachineryComfort': 'Yes, I\'m comfortable with tools and machinery',
    'StrategicPlanningEnjoyment': 'Yes, I thrive in leadership roles and enjoy strategic planning',
    'ExperimentationEnjoyment': 'Yes, I\'m passionate about scientific inquiry',
    'KnowledgeSharing': 'Yes, teaching is fulfilling for me',
    'HelpingOthersDesire': 'Yes, caring for others is important to me',
    'MedicalInterest': 'Yes, I\'m passionate about healthcare',
    'MarketTrendsInterest': 'Very interested',
    'SportsManagementInterest': 'Yes, I enjoy coaching and organizing sports activities',
    'SportsPassion': 'Very passionate',
    'FinanceManagementInterest': 'Yes, very much',
    'TechnologyCuriosity': 'Yes, I\'m interested in these fields',
    'EducationalContentInterest': 'Yes, very much',
    'FashionInterest': 'Yes, very much',
    'FinancialStatementsRole': 'They are crucial for assessing financial health and making informed decisions.'
}
processed_data = preprocess(test_data, encoders)
print(processed_data)

