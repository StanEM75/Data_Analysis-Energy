import streamlit as st
import pandas as pd
import os
import pydeck as pdk

# Define the title and logos for the chat interface
APP_TITLE = """<div style="text-align: center">
                <h1 style="font-size: 48px; color: #6366F1;">
                    Top 10 Producers in the World
                </h1>
                <p>
                    <b style="font-size: 24px">
                        Select an energy. You will see the Top 10 producers for this energy.
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

# Rank by Percentage of Production and get only the Top 10
coal = coal.sort_values(by='Percentage', ascending=False).head(10)
gas = gas.sort_values(by='Percentage', ascending=False).head(10)
oil = oil.sort_values(by='Percentage', ascending=False).head(10)

# Sidebar Parameters
st.sidebar.header("Type of Resource")

# Users Choices
choice = st.sidebar.selectbox(
    "Which Resource do you want to see?",
    ("Coal", "Gas", "Oil")
)

# Zoom Slider
zoom_level = st.sidebar.slider("Zoom Level", min_value=0.5, max_value=3.0, value=1.0, step=0.1)

# Select data corresponding to the resource
data = coal if choice == "Coal" else gas if choice == "Gas" else oil

# Determine the production column name based on the choice
production_column = 'coal_production' if choice == "Coal" else 'gas_production' if choice == "Gas" else 'oil_production'

# Create a DataFrame with the points and tooltips
data['tooltip'] = data.apply(
    lambda row: (
        f"{row['country']}\n"
        f"Percentage of World Production: {row['Percentage']}%\n"
        f"Rank: {row['Rank']}"
    ), axis=1
)

# Define the PyDeck map
deck_map = pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=20,  # Center of the map
        longitude=0,
        zoom=zoom_level,
        pitch=0
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position='[Longitude, Latitude]',
            get_color='[255, 0, 0]',
            get_radius=100000,
            pickable=True,
        ),
        pdk.Layer(
            'TextLayer',
            data=data,
            get_position='[Longitude, Latitude]',
            get_text='tooltip',  # Use the tooltip column for displaying text
            get_size=8,
            get_color='[255, 255, 255]',
            size_scale=1,
            pickable=False,
        )
    ],
)

# Render the map and title
st.markdown(APP_TITLE, unsafe_allow_html=True)
st.subheader("Map")
st.pydeck_chart(deck_map)
