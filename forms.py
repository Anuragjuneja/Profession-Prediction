from flask_wtf import FlaskForm
from wtforms import RadioField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

class ProfessionPredictionForm(FlaskForm):
    
    age = RadioField('What is your age ?',
                      choices=[('15-20', '15-20'),
                               ('20-30', '20-30'),
                               ('30-40', '30-40'),
                               ('40 or above', '40 or above')],
                      validators=[DataRequired()])

    gender = RadioField('Select your gender',
                        choices=[('Male', 'Male'),
                                 ('Female', 'Female')],
                        validators=[DataRequired()])
    
    
    free_time_activity = RadioField('Q1 Which of the following would you enjoy doing the most in your free time?',
                                     choices=[('Reading a book in the garden during summer.', 'Reading a book in the garden during summer.'),
                                              ('Playing sports with your friends.', 'Playing sports with your friends.'),
                                              ('Embracing your artistic skills by painting or sketching.', 'Embracing your artistic skills by painting or sketching.'),
                                              ('Lying on your couch and watching Netflix.', 'Lying on your couch and watching Netflix.'),
                                              ('Developing your skills in trading or learning about the financial market.', 'Developing your skills in trading or learning about the financial market.'),
                                              ('Writing and developing programming codes.', 'Writing and developing programming codes.'),
                                              ('Thinking about business ideas while watching Shark Tank.', 'Thinking about business ideas while watching Shark Tank.')],
                                     validators=[DataRequired()])

    work_environment = RadioField('Q2 Which type of work environment do you prefer?',
                                   choices=[('Office setting', 'Office setting'),
                                            ('Laboratory', 'Laboratory'),
                                            ('Studio/Workshop', 'Studio/Workshop'),
                                            ('Remote/Work from home', 'Remote/Work from home'),
                                            ('Retail/Customer-facing', 'Retail/Customer-facing')],
                                   validators=[DataRequired()])

    #skills_strengths = SelectMultipleField('Q3 Which of the following skills do you consider your strengths? (You can select more than one option)',
     #                                       choices=[('Communication', 'Communication'),
      #                                               ('Critical thinking', 'Critical thinking'),
       #                                              ('Creativity', 'Creativity'),
        #                                           ('Leadership', 'Leadership'),
         #                                         ('Marketing and Sales', 'Marketing and Sales')],
          #                                  validators=[DataRequired()])

    tech_comfort = RadioField('Q4 How comfortable are you with technology and computers?',
                              choices=[('Very comfortable', 'Very comfortable'),
                                       ('Comfortable', 'Comfortable'),
                                       ('Neutral', 'Neutral'),
                                       ('Uncomfortable', 'Uncomfortable'),
                                       ('Very uncomfortable', 'Very uncomfortable')],
                              validators=[DataRequired()])

    job_security_importance = RadioField('Q5 How important is job security to you?',
                                         choices=[('Very important', 'Very important'),
                                                  ('Important', 'Important'),
                                                  ('Neutral', 'Neutral'),
                                                  ('Not very important', 'Not very important'),
                                                  ('Not important at all', 'Not important at all')],
                                         validators=[DataRequired()])

    artistic_expression_importance = RadioField('Q6 How important is artistic expression in your life and work?',
                                                choices=[('Essential, I thrive on creativity', 'Essential, I thrive on creativity'),
                                                         ('Very important, it\'s a significant part of who I am', 'Very important, it\'s a significant part of who I am'),
                                                         ('Moderately important, I enjoy creative pursuits', 'Moderately important, I enjoy creative pursuits'),
                                                         ('Not very important, I prefer practical tasks', 'Not very important, I prefer practical tasks'),
                                                         ('Not important at all, I focus on other aspects of life', 'Not important at all, I focus on other aspects of life')],
                                                validators=[DataRequired()])

    physical_fitness_importance = RadioField('Q7 How important is physical fitness and well-being in your daily life?',
                                             choices=[('Very important, I prioritize fitness and health', 'Very important, I prioritize fitness and health'),
                                                      ('Important, I try to stay active regularly', 'Important, I try to stay active regularly'),
                                                      ('Moderately important, I enjoy physical activities occasionally', 'Moderately important, I enjoy physical activities occasionally'),
                                                      ('Not very important, fitness is not a priority for me', 'Not very important, fitness is not a priority for me')],
                                             validators=[DataRequired()])

    financial_analysis_approach = RadioField('Q8 How do you approach financial analysis and decision-making based on financial reports?',
                                             choices=[('I enjoy analyzing financial reports and making informed decisions.', 'I enjoy analyzing financial reports and making informed decisions.'),
                                                      ('I can perform financial analysis tasks but prefer other responsibilities.', 'I can perform financial analysis tasks but prefer other responsibilities.'),
                                                      ('Neutral, I haven\'t had much experience in financial analysis and decision-making.', 'Neutral, I haven\'t had much experience in financial analysis and decision-making.'),
                                                      ('Not interested in this', 'Not interested in this')],
                                             validators=[DataRequired()])

    programming_interest = RadioField('Q9 Do you have experience or interest in programming, engineering, or technical design?',
                                      choices=[('Yes, I have experience or a strong interest in these areas', 'Yes, I have experience or a strong interest in these areas'),
                                               ('Somewhat, I\'m interested in learning more', 'Somewhat, I\'m interested in learning more'),
                                               ('Neutral, I haven\'t explored technical fields', 'Neutral, I haven\'t explored technical fields'),
                                               ('No, technical fields don\'t appeal to me', 'No, technical fields don\'t appeal to me')],
                                      validators=[DataRequired()])

    entrepreneurship_interest = RadioField('Q10 Are you interested in entrepreneurship or managing your own business?',
                                           choices=[('Yes, I aspire to be an entrepreneur or business owner', 'Yes, I aspire to be an entrepreneur or business owner'),
                                                    ('Somewhat, I\'m open to entrepreneurial opportunities', 'Somewhat, I\'m open to entrepreneurial opportunities'),
                                                    ('Neutral, I haven\'t considered entrepreneurship', 'Neutral, I haven\'t considered entrepreneurship'),
                                                    ('No, entrepreneurship isn\'t my career goal', 'No, entrepreneurship isn\'t my career goal')],
                                           validators=[DataRequired()])

    content_creation_enjoyment = RadioField('Q11  Do you enjoy storytelling, writing, or creating content?',
                                            choices=[('Yes, I\'m passionate about media and communication', 'Yes, I\'m passionate about media and communication'),
                                                     ('Somewhat, I find these areas interesting', 'Somewhat, I find these areas interesting'),
                                                     ('Neutral, I haven\'t considered media and communication careers', 'Neutral, I haven\'t considered media and communication careers'),
                                                     ('No, media and communication aren\'t my focus', 'No, media and communication aren\'t my focus')],
                                            validators=[DataRequired()])

    public_service_passion = RadioField('Q12  Do you have a passion for working in government and public service roles?',
                                        choices=[('Yes, very much', 'Yes, very much'),
                                                 ('Yes, somewhat', 'Yes, somewhat'),
                                                 ('Neutral', 'Neutral'),
                                                 ('Yes, somewhat', 'Yes, somewhat'),
                                                 ('No, not at all', 'No, not at all')],
                                        validators=[DataRequired()])

    complex_concepts_explanation = RadioField('Q13 Are you patient and skilled at explaining complex concepts',
                                              choices=[('Yes, I excel in explaining concepts to others', 'Yes, I excel in explaining concepts to others'),
                                                       ('Somewhat, I\'m capable of explaining concepts', 'Somewhat, I\'m capable of explaining concepts'),
                                                       ('Neutral, I haven\'t assessed my ability in this area', 'Neutral, I haven\'t assessed my ability in this area'),
                                                       ('No, explaining concepts isn\'t my strength', 'No, explaining concepts isn\'t my strength')
                                                       ],
                                              validators=[DataRequired()])

    public_speaking_comfort = RadioField('Q14  Are you comfortable with public speaking, journalism, or digital media?',
                                         choices=[('Yes, I excel in public speaking, journalism, or digital media', 'Yes, I excel in public speaking, journalism, or digital media'),
                                                  ('Somewhat, I have some experience in these areas', 'Somewhat, I have some experience in these areas'),
                                                  ('Neutral, I haven\'t assessed my skills in public speaking or journalism', 'Neutral, I haven\'t assessed my skills in public speaking or journalism'),
                                                  ('No , Public speaking isn’t interest of mine', 'No , Public speaking isn’t interest of mine')
                                                  ],
                                         validators=[DataRequired()])

    tools_machinery_comfort = RadioField('Q15 Are you comfortable working with tools, machinery, or specialized equipment?',
                                         choices=[('Yes, I\'m comfortable with tools and machinery', 'Yes, I\'m comfortable with tools and machinery'),
                                                  ('Somewhat, I have some experience with specialized equipment', 'Somewhat, I have some experience with specialized equipment'),
                                                  ('Neutral, I haven\'t assessed my comfort level', 'Neutral, I haven\'t assessed my comfort level'),
                                                  ('Uncomfortable', 'Uncomfortable'),
                                                  ('No, working with tools and equipment isn\'t my preference', 'No, working with tools and equipment isn\'t my preference')],
                                         validators=[DataRequired()])

    strategic_planning_enjoyment = RadioField('Q16 Do you enjoy strategic planning, decision-making, policy-making and overseeing operations?',
                                              choices=[('Yes, I thrive in leadership roles and enjoy strategic planning', 'Yes, I thrive in leadership roles and enjoy strategic planning'),
                                                       ('Somewhat, I can handle leadership and decision-making responsibilities', 'Somewhat, I can handle leadership and decision-making responsibilities'),
                                                       ('Neutral, I haven\'t assessed my interest in business management', 'Neutral, I haven\'t assessed my interest in business management'),
                                                       ('No, business management isn\'t my strength or interest', 'No, business management isn\'t my strength or interest')
                                                       ],
                                              validators=[DataRequired()])

    experimentation_enjoyment = RadioField('Q17 Do you enjoy conducting experiments, analyzing data, and discovering new information?',
                                           choices=[('Yes, I\'m passionate about scientific inquiry', 'Yes, I\'m passionate about scientific inquiry'),
                                                    ('Somewhat, I find research intriguing', 'Somewhat, I find research intriguing'),
                                                    ('Neutral', 'Neutral'),
                                                    ('Not really, research isn\'t my area of interest', 'Not really, research isn\'t my area of interest')
                                                    ],
                                           validators=[DataRequired()])

    knowledge_sharing = RadioField('Q18 Do you enjoy sharing knowledge and helping others learn?',
                                    choices=[('Yes, teaching is fulfilling for me', 'Somewhat, I find it rewarding occasionally'),
                                             ('Somewhat, I find it rewarding occasionally', 'Somewhat, I find it rewarding occasionally'),
                                             ('Neutral, I haven\'t considered teaching', 'Neutral, I haven\'t considered teaching'),
                                             ('No, teaching isn\'t a career path I\'m interested in', 'No, teaching isn\'t a career path I\'m interested in')],
                                    validators=[DataRequired()])

    helping_others_desire = RadioField('Q19  Do you have a strong desire to help others and make a positive impact on their lives?',
                                       choices=[('Yes, caring for others is important to me', 'Yes, caring for others is important to me'),
                                                ('Somewhat, I\'m interested in healthcare', 'Somewhat, I\'m interested in healthcare'),
                                                ('Neutral', 'Neutral'),
                                                ('Not really, caregiving isn\'t my priority', 'Not really, caregiving isn\'t my priority')
                                                ],
                                       validators=[DataRequired()])

    medical_interest = RadioField('Q20  Are you interested in medical sciences, patient care, or public health initiatives?',
                                  choices=[('Yes, I\'m passionate about healthcare', 'Yes, I\'m passionate about healthcare'),
                                           ('Somewhat, I\'m curious about medical fields', 'Somewhat, I\'m curious about medical fields'),
                                           ('Neutral', 'Neutral'),
                                           ('Not really, healthcare isn\'t my area of interest', 'Not really, healthcare isn\'t my area of interest')],
                                  validators=[DataRequired()])

    market_trends_interest = RadioField('Q21  How interested are you in understanding and analyzing market trends?',
                                        choices=[('Very interested', 'Very interested'),
                                                 ('Interested', 'Interested'),
                                                 ('Neutral', 'Neutral'),
                                                 ('Not very interested', 'Not very interested'),
                                                 ('Not interested at all', 'Not interested at all')],
                                        validators=[DataRequired()])

    sports_management_interest = RadioField('Q22 Are you interested in coaching, organizing, or managing sports events?',
                                            choices=[('Yes, I enjoy coaching and organizing sports activities', 'Yes, I enjoy coaching and organizing sports activities'),
                                                     ('Somewhat, I might consider it', 'Somewhat, I might consider it'),
                                                     ('Neutral, I\'m unsure', 'Neutral, I\'m unsure'),
                                                     ('No, I prefer participating rather than organizing', 'No, I prefer participating rather than organizing')],
                                            validators=[DataRequired()])

    sports_passion = RadioField('Q23 How passionate are you about participating in sports activities?',
                                choices=[('Very passionate', 'Very passionate'),
                                         ('Passionate', 'Passionate'),
                                         ('Neutral', 'Neutral'),
                                         ('Not very passionate', 'Not very passionate'),
                                         ('Not passionate at all', 'Not passionate at all')],
                                validators=[DataRequired()])

    finance_management_interest = RadioField('Q24 Do you enjoy managing finances and planning business strategies?',
                                             choices=[('Yes, very much', 'Yes, very much'),
                                                      ('Yes, somewhat', 'Yes, somewhat'),
                                                      ('Neutral', 'Neutral'),
                                                      ('Not really', 'Not really'),
                                                      ('No, not at all', 'No, not at all')],
                                             validators=[DataRequired()])

    technology_curiosity = RadioField('Q25 Are you curious about advancements in technology, medicine, or environmental sciences?',
                                       choices=[('Yes, I\'m interested in these fields', 'Yes, I\'m interested in these fields'),
                                                ('Somewhat, I\'m curious to learn more', 'Somewhat, I\'m curious to learn more'),
                                                ('Neutral', 'Neutral'),
                                                ('Not really, scientific disciplines aren\'t my focus', 'Not really, scientific disciplines aren\'t my focus')],
                                       validators=[DataRequired()])

    educational_content_interest = RadioField('Q26  Do you have an interest in developing and delivering educational content?',
                                              choices=[('Yes, very much', 'Yes, very much'),
                                                       ('Yes, somewhat', 'Yes, somewhat'),
                                                       ('Neutral', 'Neutral'),
                                                       ('Not really', 'Not really'),
                                                       ('No, not at all', 'No, not at all')],
                                              validators=[DataRequired()])

    fashion_interest = RadioField('Q27 Do you have an interest in fashion and beauty trends?',
                                  choices=[('Yes, very much', 'Yes, very much'),
                                           ('Yes, somewhat', 'Yes, somewhat'),
                                           ('Neutral', 'Neutral'),
                                           ('Not really', 'Not really'),
                                           ('No, not at all', 'No, not at all')],
                                  validators=[DataRequired()])

    financial_statements_role = RadioField('Q28 What role do you think financial statements play in decision-making within a company?',
                                            choices=[('They are crucial for assessing financial health and making informed decisions.', 'They are crucial for assessing financial health and making informed decisions.'),
                                                     ('I understand their importance but prefer other aspects of business decision-making.', 'I understand their importance but prefer other aspects of business decision-making.'),
                                                     ('Neutral, I haven\'t considered the role of financial statements in decision-making', 'Neutral, I haven\'t considered the role of financial statements in decision-making'),
                                                     ('I don\'t have any idea but I am keen to explore this field', 'I don\'t have any idea but I am keen to explore this field'),
                                                     ('I don\'t have any idea and I am not interested in it', 'I don\'t have any idea and I am not interested in it')],
                                            validators=[DataRequired()])

    submit = SubmitField('Submit')
