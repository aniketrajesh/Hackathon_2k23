# Prediction of MBTA bus delay times of route 8

1. The given code can be used to show a machine learning model with the use of a Streamlit app. https://codebusters.streamlit.app/

3. The dataset was acquired from the following link: https://geo-massdot.opendata.arcgis.com/datasets/mbta-bus-stops/explore?location=42.390369%2C-71.004835%2C13.73

4. The main objective of the code is to predict the estimated waitng time by showing the delays across 6 intervals in a day

5. The dataset was filtered with route_id as 8. This means we considered the bus that navigates along route 8 which is catered to the Umass Boston community.

4. We set the X train as the stop_id concatenated with each interval across the day and Y-train to be time difference, which is the difference between scheduled time and actual time.

5. The data was trained with the help of linear regression model

6. The user can access our website and select the stop name and interval time to their convenience and our model would predict the wait time and suggest if the the bus is delayed or early
   
7. The analysis of our model:
   
  Mean Absolute Error: 263.33
  Mean Squared Error: 204018.77
  Root Mean Squared Error: 451.68
  R-squared: 0.11
