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

## 🔑 Analysis

1. Get the main statistics for every energy: Energy_Stats.ipynb
- Evolution of the Production every 10 years.
- Growth Rates for Periods of major increases.
- Top 10 Producers year by year
  
2. **main.py**
- Create the endpoint of the API.
- We need one endpoint, called arrival_time. It will guide the process through the API to know which information pick.
- The two informations we need to get is the destination_name, which corresponds to the direction of the train, and the expect arrival time at the selected station.

## 🔑 Frontend

1. **Home.py**
- Main page of the Streamlit app.

2. **Navigo Promotions.py**
- Center the map of the Streamlit App on Paris.
- Create Select Boxes to allow the user to select a type of advantage.
- Select the dataframe corresponding to this advantage.

3. **Next Trains.py**
- Create Select Boxes to allow the user to select a line and a stop.
- Request the API and the endpoint arrival time.

