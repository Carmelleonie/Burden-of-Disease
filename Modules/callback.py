from dash import html, dcc, Output, Input
from dash.exceptions import PreventUpdate
from kpi_functions import *
from prepare_data import *
from figures import *

def app_callback_functions(app):
	
	##Overview
	@app.callback(
		Output(component_id='total-deaths', component_property='children'),
		Input(component_id='country', component_property='value')
	)
	def n_deaths(country=None):
		df = prepare_data()
		if country:
			total = get_total_number_deaths(df, country)
		else:
			total = get_total_number_deaths(df)
		return total

	@app.callback(
		Output(component_id='top-cause', component_property='children'),
		Input(component_id='country', component_property='value'),
		Input(component_id='periods', component_property='value')
	)
	def top_cause(country=None, year=None):
		df= prepare_data()
		if year:
			cause = get_major_cause_death(df, country=None, year=year)
		elif country:
			cause = get_major_cause_death(df, country=country)
		elif country and year:
			cause = get_major_cause_death(df, country=country, year=year)
		else:
			cause = get_major_cause_death(df)
		return cause

	@app.callback(
		Output(component_id='top-country', component_property='children'),
		Input(component_id='cause', component_property='value')
	)
	def top_country(cause=None):
		df = prepare_data()
		if cause:
			country = get_major_country(df, causes=cause)
		else:
			country = get_major_country(df)
		return country

	
	# Trend overtime
	@app.callback(
		Output(component_id='trend-line', component_property='figure'),
		Input(component_id='country', component_property='value'),
		Input(component_id='cause', component_property='value')
	)
	def trend(country, cause):
		df = prepare_data()
		if country:
			return global_trend(df, country=country)
		elif country and cause:
			return global_trend(df, country=country, cause=cause)
		else:
			return global_trend(df)

	
	@app.callback(
		Output(component_id='top-countries', component_property='figure'),
		Input(component_id='periods', component_property='value')
	)
	def top_countries(year=None):
		df= prepare_data()
		if year and year != None:
			df = df[df["Year"].isin(year)]
		else:
			df=df
		return top_fifteenth_countries(df)

	
	@app.callback(
		Output(component_id='top-causes', component_property='figure'),
		Input(component_id='periods', component_property='value')
	)
	def top_causes(year=None):
		df= prepare_data()
		if year and year != None:
			year = [int(y) for y in year]
			df = df[df["Year"].isin(year)]
		else:
			df=df
		return major_causes(df)

	## Country deep dive
	@app.callback(
		Output(component_id='map', component_property='figure'),
		Input(component_id='periods', component_property='value'),
		Input(component_id='cause', component_property='value')
	)
	def build_map(year=None, cause=None):
		df = prepare_data()
		if year:
			choro_map = country_year_map(df, year=year, cause=None)
		elif cause:
			choro_map = country_year_map(df, year=None, cause=cause)
		elif year and cause:
			choro_map = country_year_map(df, year=year, cause=cause)
		else:
			choro_map=country_year_map(df, year=None, cause=None)
		return choro_map


	@app.callback(
		Output(component_id='donut', component_property='figure'),
		Input(component_id='country', component_property='value'),
		Input(component_id='periods', component_property='value'),
		prevent_initial_call=True
	)
	def countries_dount_chart(country, year):
		df = prepare_data()
		if country :
			return death_profile_donut(df=df, country=country, year=None)
		elif country and year:
			return death_profile_donut(df=df, country=country, year=year)
		else:
			return death_profile_donut(df=df)