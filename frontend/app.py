import streamlit as st
import pandas as pd
import time

# Existing example_pipeline function
def example_pipeline(data, predictions):
    time.sleep(5)
    result = data.head(predictions)
    csv = result.to_csv(index=False)
    return csv

st.title('Gene Time Series Analysis')

with st.form("my-form", clear_on_submit=True):
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    num_predictions = st.number_input("Enter number of predictions", min_value=1, step=1)

    # Parameter selection (if you want the user to customize a parameter)
    #param1 = st.slider('Parameter 1', 0.0, 1.0, 0.5)
    #param2 = st.selectbox('Parameter 2', ['Option 1', 'Option 2', 'Option 3'])

    submitted = st.form_submit_button("Train Model")

if submitted:
    if uploaded_file is not None and uploaded_file.name.endswith('.csv')::
        df = pd.read_csv(uploaded_file)
        st.write("Preview of Uploaded Data:")
        st.dataframe(df.head())

        # Training model and downloading results
        with st.spinner('Training model...'):
            # Intialize progress bar
            progress_bar = st.progress(0)

            # Simulate progress bar
            for percent_complete in range(20):
                time.sleep(0.1)  # simulate a delay for each step (replace with real logic)
                progress_bar.progress(percent_complete + 5)

            # Task completed
            progress_bar.progress(100)
            st.session_state['training_complete'] = True

            # Call to the backend function
            result_csv = example_pipeline(df, num_predictions)
            st.download_button("Download CSV", result_csv, "file.csv", "text/csv", key='download-csv')
            st.success("Model training complete. You can download the results or train a new model.")
    else:
        st.error("Please upload a CSV file.")
