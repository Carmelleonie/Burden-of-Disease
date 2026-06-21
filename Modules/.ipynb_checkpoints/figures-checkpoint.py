import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from prepare_data import prepare_data

#Overview
## Global trend of deaths in the world
def global_trend(df, country=None, cause=None):
	if country and cause is None:
		df = df[df["Country/Territory"] == country]
		year = df.groupby("Year")["value"].sum().reset_index()
		fig = px.line(data_frame=year,
			x="Year",
			y="value",
			labels={
				"x":"Year",
				"y":"Number of Death"},
			title="Trend of Deaths over time")
	elif country and isinstance(cause, str):
		df = df[(df["Country/Territory"] == country) & (df["Cause of deaths"] == cause)]
		year = df.groupby("Year")["value"].sum().reset_index()
		fig = px.line(data_frame=year,
			x="Year",
			y="value",
			labels={
				"x":"Year",
				"y":"Number of Death"},
			title=f"Trend of Deaths over time due to {cause}")
	elif country and isinstance(cause, list):
		f = df[(df["Country/Territory"] == country) & (df["Cause of deaths"].isin(cause))]
		year = df.groupby(["Year", "Cause of deaths"])["value"].sum().reset_index()
		fig = px.line(data_frame=year,
			x="Year",
			y="value",
			color="Cause of deaths",
			labels={
				"x":"Year",
				"y":"Number of Death"},
			title=f"Trend of Deaths over time due to: {",".join(cause)}")
	else:
		df = df
		year = df.groupby("Year")["value"].sum().reset_index()
		fig = px.line(data_frame=year,
			x="Year",
			y="value",
			labels={
				"x":"Year",
				"y":"Number of Death"},
			title="Trend of Deaths over time")
	return fig

## Top 15 major causes of death
def major_causes(df, year=None):
	if year:
		df = df[df["Year"]==int(year)]
	else:
		df=df
	causes = (df.groupby("Cause of deaths", sort=True)["value"].sum().sort_values(ascending=True))
	causes = causes.tail(15)
	fig = px.bar(
		data_frame=causes,
		x=causes.values,
		y=causes.index,
		orientation="h",
		labels={"x":"Number of death", "y":"Top 15 causes"}
	)
	return fig

## Top fifteenth countries
def top_fifteenth_countries(df, year=None):
	if year:
		df = df[df["Year"] == int(year)]
	groupby_country = df.groupby(by="Country/Territory", sort=True)["value"].sum().sort_values(ascending=True)
	# Get the fifteen countries with the highest number of death cases 
	fifteen_top = groupby_country.tail(15)
	fig = px.bar(
		x=fifteen_top.values,
		y=fifteen_top.index,
		orientation="h",
		labels={"x":"Number of death", "y":"Top 15 countries"}
	)
	return fig

# Country deep dive
## Choropleth world map
def country_year_map(df, year=None, cause=None):
	if year:
		if isinstance(year, str):
			df = df[df["Year"] == int(year)]
		elif isinstance(year, list):
			df = df[df["Year"].isin([int(y) for y in year])]
	elif cause:
		if isinstance(cause, str):
			df = df[df["Cause of deaths"] == cause]
		elif isinstance(cause, list):
			df = df[df["Cause of deaths"].isin(cause)]
	elif year and cause:
		if isinstance(year, str) and isinstance(cause, str):
			df = df[(df["Year"] == int(year)) & (df["Cause of deaths"] == cause)]
		elif isinstance(year, list) and isinstance(cause, str):
			df = df[(df["Year"].isin([int(y) for y in year])) & (df["Cause of deaths"] == cause)]
		elif isinstance(year, list) and isinstance(cause, list):
			df = df[(df["Year"].isin([int(y) for y in year])) & (df["Cause of deaths"].isin(cause))]
		elif isinstance(year, str) and isinstance(cause, list):
			df = df[(df["Year"] == int(y)) & (df["Cause of deaths"].isin(cause))]
	else:
		df = df
	df_groupby_country = df.groupby(["Country/Territory", "Code"])["value"].sum().to_frame().reset_index()
		
	fig = px.choropleth(
		data_frame=df_groupby_country,
	    locationmode='ISO-3',
	    locations="Code",
	    hover_name="Country/Territory",
	    hover_data="value",
	    projection="natural earth",
	    color="value",
	    color_continuous_scale="Reds"
	)
	return fig


## Profile of deaths in country and year
def death_profile_donut(df, country=None, year=None):
	if country:
		if isinstance(year, str):
		    data = df[
		        (df["Country/Territory"] == country) &
		        (df["Year"] == int(year))
		    ]
		elif isinstance(year, list):
			data = df[
		        (df["Country/Territory"] == country) &
		        (df["Year"].isin([int(y) for y in year]))
		    ]
		else:
			data = df[
		        df["Country/Territory"] == country
		    ]
	else:
		data = df
	causes = (
        data.groupby("Cause of deaths")["value"]
        .sum()
        .reset_index())
	
	fig = px.pie(causes,
				 names="Cause of deaths",
				 values="value",
				 hole=0.5,
				 title=f"Death Profile in {country} ({year})"
				)
	fig.update_traces(textinfo="percent+label")
	return fig