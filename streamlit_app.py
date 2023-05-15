#Write a simple app that reads the user input and display the output
import streamlit as st
import pandas as pd
import altair as alt


openai.api_key = st.secrets["API_key"]

def save_and_download_csv(dataframe):
    # Save the dataframe as a CSV file
    dataframe.to_csv('output.csv', index=False)

    # Generate a download link for the CSV file
    with open('output.csv', 'rb') as file:
        csv_data = file.read()
    st.download_button(label='Download CSV', data=csv_data, \
                       file_name='output.csv', mime='text/csv')


# Define the Streamlit app
def app():

d
    st.title("CSV File Download")
    st.write("Generate a CSV file and download it.")

    # Create a sample dataframe
    data = {'Name': ['John', 'Jane', 'Mike'],
            'Age': [25, 30, 35]}
    df = pd.DataFrame(data)

    # Display the dataframe
    st.header("Dataframe")
    st.write(df)

    # Save and download the CSV file
    save_and_download_csv(df)

# Run the app
if __name__ == "__main__":
    app()
