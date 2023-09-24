import pandas as pd
from sklearn.preprocessing import normalize, MinMaxScaler
import streamlit as st
import joblib
import pandas as pd
import os


if os.path.exists("MBTA_Model.joblib"):
    model = joblib.load("MBTA_Model.joblib")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score



df = pd.read_csv("MBTA_DATA_08_FINAL_NEW.csv", delimiter= ',')

selected_features = df.columns[1:]


X = df[selected_features]
def main():

    st.set_page_config(page_title="Hackathon Model Showcase", page_icon="🧊")

    st.title("Welcome to MBTA")
    st.write("Estimate The delays in Route 8 by choosing Bus Stop and Timeslot")
main()

bus_stops = {
    "Harrison Ave @ E Newton St": 10015,
    "Ruggles St @ Huntington Ave": 1784,  # Multiple stop IDs for the same stop name
    "Columbia Rd opp Pond St": 123,
    "Ruggles Station - Lane 2": 17863,
    "Ruggles Sta - Upper Level": 17861,
    "91 E Concord St": 5089,
    "Dudley Station": 64,
    "South Bay Mall @ Target": 11241,
    "Kenmore Station Busway": 899,
    "Mt Vernon St @ South Point Dr": 111,  # Multiple stop IDs for the same stop name
    "Massachusetts Ave @ Columbia Rd": 134,
    "Columbia Rd @ JFK/UMASS Station": 121,
    "Longwood Ave @ Brookline Ave": 1779,
    "Brookline Ave @ Longwood Ave": 1804,
    "South Bay Mall @ Office Max": 29051,
    "Brookline Ave @ Yawkey Way": 1563,
    "Brookline Ave opp Yawkey Way": 1518
}

st.write("Choose the Bus Stop")
options = bus_stops.keys()

selected_option = st.selectbox("Select an option:", options)

# Display the selected option
st.write("You selected:", selected_option)

st.write("Choose the time Slot (3hrs interval during day )")
# Create a list of time slot options
time_slots = ['6to9', '9to12', '12to15', '15to18', '18to21']

# Use st.selectbox to create the dropdown for time slots
selected_time_slot = st.selectbox('Select a time slot:', time_slots)

# Display the selected time slot
st.write('You selected:', selected_time_slot)

x_test_inp = str(bus_stops[selected_option]) + "_" + selected_time_slot

num = X.columns.get_loc(x_test_inp)
x_test_inp_new = [0 for i in range(131)]
x_test_inp_new[num] = 1

y_pred_inp = model.predict([x_test_inp_new])
final_output = y_pred_inp[0] / 60

if y_pred_inp[0] > 0:
    st.write("Bus Delays in the above selected Bus Stop and Timeslot is :", final_output, " minutes")
else:
    st.write("Bus is early in the above selected Bus Stop and Timeslot by:", -final_output, " minutes")



