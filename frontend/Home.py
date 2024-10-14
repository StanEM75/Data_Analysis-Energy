import streamlit as st
import pandas as pd
import os
from streamlit_globe import streamlit_globe

# Define the title and logos for the chat interface
APP_TITLE = """<div style="text-align: center">
                <h1 style="font-size: 48px; color: #6366F1;">
                    Fossil Energy in the World
                </h1>
                <p>
                    <b style="font-size: 24px">
                        Powered by Streamlit
                    </b>
                </p>
                <p>
                        Please select a tab. </b> The 'Country' tab will display energy production by country, while the 'Map' tab will showcase the 10 most important countries in terms of energy production.
                    </b>
                </p>
            </div>
        """

# App
def app():
    # Display the title
    st.markdown(APP_TITLE, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    app()