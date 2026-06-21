import pandas as pd

def prepare_data():
	# Select rows of a specific country
	df = pd.read_csv("Cause_of_death_in_the_world/data/cause_of_deaths.csv")
	ids = ['Country/Territory', 'Code', 'Year']
	causes = ['Meningitis', 'Alzheimer\'s Disease and Other Dementias',
          'Parkinson\'s Disease', 'Nutritional Deficiencies', 'Malaria',
          'Drowning', 'Interpersonal Violence',
          'Maternal Disorders', 'HIV/AIDS', 'Drug Use Disorders', 
          'Tuberculosis', 'Cardiovascular Diseases',
          'Lower Respiratory Infections', 'Neonatal Disorders',
          'Alcohol Use Disorders', 'Self-harm', 'Exposure to Forces of Nature',
          'Diarrheal Diseases', 'Environmental Heat and Cold Exposure',
          'Neoplasms', 'Conflict and Terrorism', 'Diabetes Mellitus',
          'Chronic Kidney Disease', 'Poisonings', 'Protein-Energy Malnutrition',
          'Road Injuries', 'Chronic Respiratory Diseases',
          'Cirrhosis and Other Chronic Liver Diseases', 'Digestive Diseases',
          'Fire, Heat, and Hot Substances', 'Acute Hepatitis']

	df_long = df.melt(id_vars=ids,
                  value_vars=causes,
                  var_name="Cause of deaths",
                  value_name="value")
	return df_long
