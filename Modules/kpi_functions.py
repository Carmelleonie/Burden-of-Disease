import pandas as pd
import plotly.express as px

def country_year(df, country=None, year=None):
	# Select the top 15 causes
	if country and year:
		df = df[(df["Country/Territory"] == country) & df["Year"] == year]
		causes = df.groupby("Cause of deaths")["value"].sum().sort_values(ascending=True).tail(15)

		fig = px.bar(
			data_frame=causes,
			x=causes.values,
			y=cause.index,
			labels={
				"x":"Number of death",
				"y":"Top 15 causes of death"
			}
		)
	fig = px.bar(
		data_frame=causes,
		x=causes.values,
		y=causes.index,
		orientation="h",
		labels={"x":"Number of death", "y":"Major Causes"}
	)
	return fig

# Get the total number of deaths
def get_total_number_deaths(df, country=None):
	if country and isinstance(country, str):
		country=[country]
		df = df[df["Country/Territory"].isin(country)]
		total = df["value"].sum()
	elif country and isinstance(country, list):
		country=country
		df = df[df["Country/Territory"].isin(country)]
		total = df["value"].sum()
	else:
		total = df["value"].sum()
	return total

# Get the major cause and the number of deaths
def get_major_cause_death(df, country=None, year=None):
	if country:
		if isinstance(country, str):
			country = [country]
			df = df[df["Country/Territory"].isin(country)]
		elif isinstance(country, list):
			country = country
			df = df[df["Country/Territory"].isin(country)]
	elif year:
		if isinstance(year, str):
			year = [year]
			df = df[df["Year"].isin(year)]
		elif year and isinstance(year, list):
			year = [int(y) for y in year]
			df = df[df["Year"].isin(year)]
	elif country and year:
		if isinstance(country, str) and isinstance(year, str):
			df = df[(df["Country/Territory"] == country) & (df[df["Year"]==int(year)])]
		elif isinstance(country, str) and isinstance(year, list):
			df = df[(df["Country/Territory"] == country) & (df[df["Year"].isin([int(y) for y in year])])]
		elif isinstance(country, list) and isinstance(year, str):
			df = df[(df["Country/Territory"].isin(country)) & (df[df["Year"]==int(year)])]
		if isinstance(country, list) and isinstance(year, list):
			df = df[(df["Country/Territory"].isin(country)) & (df[df["Year"].isin([int(y) for y in year])])]
	else:
		df=df
	groupby_causes = df.groupby("Cause of deaths")["value"].sum()
	cause = groupby_causes.idxmax()
	#n_deaths = groupby_causes.max()
	return cause

# Get the Top country and the number of deaths
def get_major_country(df, causes=None):
	if causes and isinstance(causes, str):
		causes = [causes]
		df = df[df["Cause of deaths"].isin(causes)]
	elif causes and isinstance(causes, list):
		causes = causes
		df = df[df["Cause of deaths"].isin(causes)]
	else:
		df = df
	groupby_country = df.groupby("Country/Territory")["value"].sum()
	country = groupby_country.idxmax()
	#n_deaths = groupby_causes.max()
	return country

	