import streamlit as st
import joblib
import numpy as np
# Load the pre-trained model
model = joblib.load("insurance.pkl")

# App title
st.title('Prédiction du Coût de l\'Assurance Santé')

# App description
st.write('''
This App predicts the cost of health insurance based on age, sex, bmi, region, children and smoker
''')
# Creation of slider and options of input of user
age = st.number_input('Age', 1.00, 100.00, 39.00)
sex = st.selectbox('Sex', ('female', 'male'))
bmi = st.number_input('BMI', 15.00, 53.00, 30.00 )
children = st.number_input('Children', 0.00, 5.00, 1.00)
smoker = st.selectbox('Smoker', ('yes', 'no'))
region = st.selectbox('Region', ('southwest', 'southeast', 'northwest', 'northeast'))
# convert inputs into numeric format
# convert sex column
if sex == 'male':
    sex = 1
elif sex == 'female':
    sex = 0
# converted the smoker column
if smoker == 'yes':
    smoker = 1
elif smoker == 'no':
    smoker = 0
# convert region column
if region == 'southwest':
    region = 3
elif region == 'southeast':
    region = 2
elif region == 'northwest':
    region = 1
elif region == 'northeast':
    region  = 0
# display inputs entered by the use
st.subheader('Your information:')
st.write(f'Age = {age}')
st.write(f'Sex = {'male' if sex == 1 else 'female'}')
st.write(f'BMI = {bmi}')
st.write(f'Children = {children}')
st.write(f'Smoker = {'yes' if smoker == 1 else 'no'}')
if region == 3:
    st.write(f'Region = {'southwest'}')
elif region == 2:
    st.write(f'Region = {'southeast'}')
elif region == 1:
    st.write(f'Region = {'northwest'}')
elif region == 0:
    st.write(f'Region = {'northeast'}')
# create a prediction when the user presses the button
if st.button('Predict the charging cost'):
    # prepare input data for the model
    input_data = np.array([[age, sex, bmi, children, smoker, region]])
    # make the prediction
    predicted_cost = model.predict(input_data)
    # show result
    st.subheader(predicted_cost[0])

