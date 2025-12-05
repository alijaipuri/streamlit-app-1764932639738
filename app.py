import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='BMI Index Calculator', page_icon='🏋️‍♀️')

st.title('🏋️‍♀️ BMI Index Calculator')
st.markdown('Welcome! This app calculates your Body Mass Index (BMI) based on your weight and height.')

# Sidebar inputs
with st.sidebar:
    st.header('Settings')
    weight = st.number_input('Enter your weight (in kg)', min_value=0.0, step=0.1)
    height = st.number_input('Enter your height (in meters)', min_value=0.0, step=0.01)
    st.info('Note: Please enter your weight and height in the respective units.')

# Main content
if st.button('Calculate BMI', type='primary'):
    try:
        if weight > 0 and height > 0:
            bmi = weight / (height ** 2)
            st.write(f'Your BMI is: {bmi:.2f}')
            if bmi < 18.5:
                st.error('You are underweight.')
            elif bmi < 25:
                st.success('You are normal weight.')
            elif bmi < 30:
                st.warning('You are overweight.')
            else:
                st.error('You are obese.')
        else:
            st.error('Please enter a valid weight and height.')
    except Exception as e:
        st.error('An error occurred: ' + str(e))

# Show example
with st.expander('See example'):
    st.write('For example, if your weight is 70 kg and your height is 1.75 m, your BMI would be:')
    example_bmi = 70 / (1.75 ** 2)
    st.write(f'BMI: {example_bmi:.2f}')
    if example_bmi < 18.5:
        st.write('You are underweight.')
    elif example_bmi < 25:
        st.write('You are normal weight.')
    elif example_bmi < 30:
        st.write('You are overweight.')
    else:
        st.write('You are obese.')

# Show BMI categories
st.header('BMI Categories')
bmi_categories = pd.DataFrame({
    'Category': ['Underweight', 'Normal weight', 'Overweight', 'Obese'],
    'BMI Range': ['Less than 18.5', '18.5-24.9', '25-29.9', '30 or greater']
})
st.table(bmi_categories)