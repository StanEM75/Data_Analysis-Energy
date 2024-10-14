import streamlit as st
import pandas as pd
import os

# Define the title and logos for the chat interface
APP_TITLE = """<div style="text-align: center">
                <h1 style="font-size: 48px; color: #6366F1;">
                    Production of Energy for Every Country
                </h1>
                <p>
                    <b style="font-size: 24px">
                        Please select a country and an energy to see how much the selected country produces.
                    </b>
                </p>
            </div>
        """

# Load data
current_dir = os.path.dirname(__file__)

csv_path_coal = os.path.join(current_dir, 'data/coal_prod.csv')
coal = pd.read_csv(csv_path_coal)

csv_path_gas = os.path.join(current_dir, 'data/gas_prod.csv')
gas = pd.read_csv(csv_path_gas)

csv_path_oil = os.path.join(current_dir, 'data/oil_prod.csv')
oil = pd.read_csv(csv_path_oil)

# Get a list of unique countries
countries = coal['country'].drop_duplicates().to_list()

# Sidebar Parameters : Resources
st.sidebar.header("Type of Resource")

# Users Choices : Resources
resource = st.sidebar.selectbox(
    "Which Resource do you want to see?",
    ("Coal", "Gas", "Oil")
)

# Sidebar Parameters : Countries
st.sidebar.header("Country")

# Users Choices : Countries
country = st.sidebar.selectbox(
    "Which Country do you want to see?",
    (countries)
)

# Select data corresponding to the resource
data = coal if resource == "Coal" else gas if resource == "Gas" else oil

# Determine the production column name based on the choice
production_column = 'coal_production' if resource == "Coal" else 'gas_production' if resource == "Gas" else 'oil_production'

# Filter data for the selected country
country_data = data[data['country'] == country]

# Display the production information for the selected country
if not country_data.empty:
    # Create a new DataFrame with renamed columns
    renamed_data = country_data[[production_column, 'Percentage', 'Rank']].rename(columns={
        production_column: 'Production (MT)',
        'Percentage': 'Percentage (%)',
        'Rank': 'Rank'
    })
    
    # Display the renamed DataFrame
    st.dataframe(renamed_data)
else:
    st.write("No data available for the selected country.")