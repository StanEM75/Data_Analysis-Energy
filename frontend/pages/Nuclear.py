import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.express as px

# Define the title and logos for the chat interface
APP_TITLE = """<div style="text-align: center">
                <h1 style="font-size: 48px; color: #6366F1;">
                    Nuclear in the World
                </h1>
                <p>
                    <b style="font-size: 24px">
                        Please select a country to see how nuclear production changed over the past few years.
                    </b>
                </p>
            </div>
        """

# Load data
current_dir = os.path.dirname(__file__)

csv_path_nuclear = os.path.join(current_dir, 'data/world_nuclear_energy_generation.csv')
nuclear = pd.read_csv(csv_path_nuclear)

# Get a list of unique countries
countries = nuclear['Entity'].drop_duplicates().to_list()

# Sidebar Parameters : Countries
st.sidebar.header("Country")

# Users Choices : Countries
country = st.sidebar.selectbox(
    "Which Country do you want to see?",
    (countries)
)

# Select only the country
nuclear = nuclear[nuclear['Year']>=1985]
data = nuclear[nuclear['Entity']==country].rename(columns={'share_of_electricity_pct' : 'Percentage of Nuclear in the Energy Mix'})

# Plot
fig = px.line(data, x='Year', y='Percentage of Nuclear in the Energy Mix', title='Share of Nuclear in the Energy Mix')

# Display
st.plotly_chart(fig)

