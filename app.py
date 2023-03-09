import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
conn.commit()

# loading the saved models
heart_disease_model = pickle.load(open(r'heart_disease_model.sav','rb'))
# sidebar for navigation
with st.sidebar:
    selected = option_menu('Heart Disease Prediction System',
                           [
                            'Heart Disease Prediction',
                            'Login',
                            'Register'
                           ],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)
# Heart Disease Prediction Page
# Login page
if selected == 'Login':
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Submit"):
        cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
        user = cursor.fetchone()
        if user:
            st.success("Logged in!")
            st.sidebar.checkbox("Login", value=True, key="login")
        else:
            st.error("Incorrect username or password.")

# Register page
elif selected == 'Register':
    st.title("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')
    if st.button("Submit"):
        if password == confirm_password:
            cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
            conn.commit()
            st.success("Registered!")
        else:
            st.error("Passwords do not match.")
if selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease Prediction')
    # check if the user is logged in
    if not st.sidebar.checkbox('Login'):
        st.warning("Please log in to access this page.")
    else:
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.number_input('Age')

        with col2:
            sex = st.number_input('Sex')

        with col3:
            cp = st.number_input('Chest Pain types')

        with col1:
            trestbps = st.number_input('Resting Blood Pressure')

        with col2:
            chol = st.number_input('Serum Cholestoral in mg/dl')

        with col3:
            fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')

        with col1:
            restecg = st.number_input('Resting Electrocardiographic results')

        with col2:
            thalach = st.number_input('Maximum Heart Rate achieved')

        with col3:
            exang = st.number_input('Exercise Induced Angina')

        with col1:
            oldpeak = st.number_input('ST depression induced by exercise')

        with col2:
            slope = st.number_input('Slope of the peak exercise ST segment')

        with col3:
            ca = st.number_input('Major vessels colored by flourosopy')

        with col1:
            thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

        # code for Prediction
        heart_diagnosis = ''

        # creating a button for Prediction
        if st.button('Heart Disease Test Result'):
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            if heart_prediction[0] == 1:
               heart_diagnosis = 'The person is having heart disease'
            else:
               heart_diagnosis = 'The person does not have any heart disease'

        st.success(heart_diagnosis)


# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu
# import streamlit as st
# import mysql.connector

# # Connect to database
# mydb = mysql.connector.connect(
#     host="host",
#     user="username",
#     password="password",
#     database="database_name"
# )

# # Create login form
# def login():
#     st.title("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type='password')
#     if st.button("Submit"):
#         mycursor = mydb.cursor()
#         mycursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
#         result = mycursor.fetchone()
#         if result:
#             st.success("Logged in as {}".format(username))
#         else:
#             st.error("Incorrect username or password")

# # Add login option to sidebar
# with st.sidebar:
#     if st.button("Login"):
#         login()

# # Your existing code for the Heart Disease Prediction page goes here
# # loading the saved models
# heart_disease_model = pickle.load(open(r'C:\Users\MRCET\Desktop\heart_disease_model.sav','rb'))
# # sidebar for navigation
# with st.sidebar:
#     selected = option_menu('Heart Disease Prediction System',
#                            [
#                             'Heart Disease Prediction',
#                             ],
#                            icons=['activity', 'heart', 'person'],
#                            default_index=0)
# # Heart Disease Prediction Page
# if selected == 'Heart Disease Prediction':
#     # page title
#     st.title('Heart Disease Prediction')

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         age = st.number_input('Age')
    
#     with col2:
#         sex = st.number_input('Sex')

#     with col3:
#         cp = st.number_input('Chest Pain types')

#     with col1:
#         trestbps = st.number_input('Resting Blood Pressure')

#     with col2:
#         chol = st.number_input('Serum Cholestoral in mg/dl')

#     with col3:
#         fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')

#     with col1:
#         restecg = st.number_input('Resting Electrocardiographic results')

#     with col2:
#         thalach = st.number_input('Maximum Heart Rate achieved')

#     with col3:
#         exang = st.number_input('Exercise Induced Angina')

#     with col1:
#         oldpeak = st.number_input('ST depression induced by exercise')

#     with col2:
#         slope = st.number_input('Slope of the peak exercise ST segment')

#     with col3:
#         ca = st.number_input('Major vessels colored by flourosopy')

#     with col1:
#         thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

#     # heart_disease_params = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
#     # heart_disease_int = [int(item) for item in heart_disease_params]

#     # code for Prediction
#     heart_diagnosis = ''

#     # creating a button for Prediction

#     if st.button('Heart Disease Test Result'):
#         heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

#         if heart_prediction[0] == 1:
#             heart_diagnosis = 'The person is having heart disease'
#         else:
#             heart_diagnosis = 'The person does not have any heart disease'

#     st.success(heart_diagnosis)
