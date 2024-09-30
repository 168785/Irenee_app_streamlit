import streamlit as st
import joblib
import numpy as np
# Charger le modèle pré-entraîné
model = joblib.load("insurance.pkl")

# Titre de l'application
st.title('Prédiction du Coût de l\'Assurance Santé')

# Description de l'application
st.write('''
Cette Applicatiion predit le cout de l'assurance sante en fonction de l'age, sex, bmi, region, children and smoker
''')
# creer  des sliders et des options pour les inputs de l'utilisation
age = st.number_input('Age', 1, 100, 39)
sex = st.selectbox('Sex', ('female', 'male'))
bmi = st.number_input('BMI', 15.00, 53.00, 30.00 )
children = st.number_input('Children', 0, 5, 1)
smoker = st.selectbox('Smoker', ('yes', 'no'))
region = st.selectbox('Region', ('southwest', 'southeast', 'northwest', 'northeast'))
# convertir les inputs en format numeriques
# convertir la collone sex
if sex == 'male':
    sex = 1
elif sex == 'female':
    sex = 0
# convertie la collone smoker
if smoker == 'yes':
    smoker = 1
elif smoker == 'no':
    smoker = 0
# convertir la collone region
if region == 'southwest':
    region = 3
elif region == 'southeast':
    region = 2
elif region == 'northwest':
    region = 1
elif region == 'northeast':
    region  = 0
# afficher les inputs saisis par l'utilisateur
st.subheader('Vos informations:')
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
# creer une prediction quand l'utilisateur appuie sur le boutton
if st.button('Predire le cout de charge'):
    # preparer les donnees d'entrees pour le modele
    input_data = np.array([[age, sex, bmi, children, smoker, region]])
    # faire la prediction
    predicted_cost = model.predict(input_data)
    # afficher le resultat
    st.subheader(f"{predicted_cost[0]}")

