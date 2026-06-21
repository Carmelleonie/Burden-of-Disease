from dash import html, dcc
import dash_bootstrap_components as dbc
from prepare_data import prepare_data
from prepare_data import prepare_data

def create_app_layout():
	df = prepare_data()
	return html.Div([
		html.H1("Global Burden of Disease Dashboard (1990-2019)"),
		html.Div(
	    className="main-div",
	    children=[
	        # Slicers Div
			html.Div(className="slicers", children=[
				html.Div([
	                    html.Label("Period of Years"),
	                    dcc.Dropdown(
							id='periods',
	                        options=[{"label": str(year), "value":year} for year in range(1990, 2020)],
	                        #value="None",
	                        multi=True
	                    )
	                ]),
				html.Div([
					html.Label("Countries"),
					dcc.Dropdown(
						id='country',
						options= [{"label": c, "value": c} for c in df["Country/Territory"].unique()],
						value=df["Country/Territory"].unique()[0],
						multi=False
					)
				]),
				html.Div([
	                    html.Label("Causes of Death"),
	                    dcc.Dropdown(id='cause',
	                        options=['Meningitis', 'Alzheimer\'s Disease and Other Dementias',
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
              'Fire, Heat, and Hot Substances', 'Acute Hepatitis'],
	                        #value="None",
	                        multi=True
	                    )
					])
			]),
			# Main Div
			html.Div(className="figures-graphs", children=[
				dbc.Tabs([
					dbc.Tab(
						label="Global Overview",
						children=[
							dbc.Row(className="row-one", align="stretch", children=[
								dbc.Col(className="colwidth", children=[
									dbc.Card([
										dbc.CardHeader("Total Deaths", className="card-title"),
										dbc.CardBody([
											html.H3(id="total-deaths", className="figures")
										])
									])
								], width=4),
								dbc.Col(className="colwidth", children=[
									dbc.Card([
										dbc.CardHeader("Top Cause of Deaths", className="card-title"),
										dbc.CardBody([
											html.H3(id="top-cause")
										])
									])
								], width=4),
								dbc.Col(className="colwidth",
										children=[
									   dbc.Card([
										   dbc.CardHeader("Top Country", className="card-title"),
										   dbc.CardBody([
											   html.H3(id='top-country')
										   ])
										   
									   ])
									], width=4),
							]),
							dbc.Row(className="row-two",
								  children=[
									  dcc.Graph(id="trend-line")
								  ]),
							dbc.Row(
								className="row-three",
								children=[
								dbc.Row(
									dcc.Graph(id="top-countries")
								),
								dbc.Row(
									dcc.Graph(id="top-causes")
								)
								])
						]
					),
					dbc.Tab(label="Country Deep Dive",
						   children=[
							   dbc.Row(
								   dcc.Graph(id="map")
							   ),
							   dbc.Row([
								   html.H4(id="donut-title"),
							   dcc.Graph(id='donut')
							   ])
						   ])
			])
		])
		])
	])
        