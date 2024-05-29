import streamlit as st
import pandas as pd

# Title of the app
st.title('ATSPM AI')

# File uploader widget
uploaded_file = st.file_uploader('Choose a Perflog CSV file', type='csv')

if uploaded_file is not None:
    # Convert the uploaded file to a dataframe
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.write('DataFrame:')
    st.dataframe(df)

    # Display some statistics
    st.write('Basic Statistics:')
    st.write(df.describe())
else:
    st.write('Please upload Perflog CSV file to see the data.')
