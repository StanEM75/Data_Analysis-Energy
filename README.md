# Streamlit Project - Energy Production across the World

![Project Image](https://justenergy.com/wp-content/uploads/2023/08/energy-production-and-consumption-on-the-environment.jpeg)

Access the application here:

## 🚀 Introduction

The productions of 3 fossil energies were put in a file.<br><br>
From 1900 to 2022, we can check how much all the countries produced for oil, gas and coal.<br><br>
We started to produce process the data, then agregated it and analysed it at the end.<br><br>
The first part of the analysis is made through the PDF file: summarizing the main trends for oil, gas and coal productions.<br><br>
The second part is to display the information contained in the file through a Streamlit application.

## 🛠️ Technos Used

- **Python**
- **Streamlit**
- **Tableau**
- **Microsoft Office**
- **Pandas**

## 🔑 Data Preparation : World_Consumption.ipynb
- Import the file and check the overall information: number of rows, null values, data types.
- Remove null values.
- Create 3 dataframes : one for each type of energy.
- Export the 3 dataframes to an 'output' folder.

## 🔑 Data Preparation : Map_Preparation.ipynb
- Keep only the most recent value for every country.
- Calculate the percentage of the total production represented by the country.
- Rank the country based on the percentage represented.
- Add Longitudes and Latitudes information from a Geo file, to help Streamlit to localize the countries.
- Export to pages/data folder.

## 🔑 Analysis

1. Get the main statistics for every energy: Energy_Stats.ipynb
- Evolution of the Production every 10 years.
- Growth Rates for Periods of major increases.
- Top 10 Producers year by year.
  
2. Produce figures: Tableau
- On Tableau, import the 3 files from the 'output' folder.
- Produce figures showing the evolution of the production between 1900 and 2022.
- Add additional information from the statistics file.

## 🔑 Frontend : Application Development

1. **Home.py**
- Main page of the Streamlit app.

2. **Country.py**
- Import the 3 dataframes from data folder in pages.
- Create Select Boxes to allow the user to select an energy and a country.
- Create a dataframe taking only into account the data for the selected country and selected energy.

3. **Map.py**
- For each energy, take only the 10 first values, which correspond to the 10 first producers.
- Create a map of the World.
- Create Select Box to allow the user to select an energy.
- Print the information on the map using Pydeck.

