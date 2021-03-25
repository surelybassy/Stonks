# Stock Market Analysis
Data Science and Engineer Project
*Andrew Ashdown - 2021*

![Graph](Images/TimeSeriesAMC.png?raw=true "Graph")

## Outline

The project started as a simple data analysis practice, as I wanted to try out some different techniques for financial analysis and prediction. After the initial analysis, I decided to continue the project with more of a focus on data engineering, using Python with the Dash and Plotly libraries to build a tool that can be deployed in the cloud to provide live information.

## Analysis and Predications

Initial analysis took place using Jupyter Notebook. The Pandas-datatreader was used to pul the data of different companies stock information from Yahoo into a dataframe. Then used Seaborn to visualise the results.

Using the Long Short-Term Memory (LSTM) technique to build a predictive model from the first 80% of the data set, I would then predict the outcome for the remaining 20% and compare the results to the actual stock prices.

![Predictions](Images/StonksPredictions.png?raw=true "Predictions")

## Dashboading

I used Python and Dash library to create a dashboarding tool. The pandas-datareader was used again to pull in the data and some calculations were performed using Pandas. Interactive graphs were created using the Plotly Graph Objects library. HTML and CSS were used to style the page.

![Dashboard](Images/StonksDashboard.png?raw=true "Dashboard")


