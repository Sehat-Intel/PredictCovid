import streamlit as st
import webbrowser

import src.pages.tutorial as tutorial
import src.pages.signup as signup
import src.pages.dashboard as dashboard
import src.assets.config as config
import src.assets.hash as hash

collection = config.db['users']

st.set_page_config(
     page_title="Sehat Intel",
     page_icon="💊",
     layout="centered", 
     initial_sidebar_state="auto") 

st.title("Sehat Intel 💊")
st.warning("""Covid-19 Detection using Deep Learning""" )
st.info("Our model has baseline accuracy of 94%")
st.title("Predict the Probability of Covid-19 🧙‍♂️")

choice = st.sidebar.radio("User Login",["Tutorial","SignUp", "Login"], key=1)

if st.sidebar.button('Click here if you are a doctor'):
    webbrowser.open_new_tab('https://gallant-kilby-f9f3a3.netlify.app/')


if choice == "Tutorial":
    st.subheader("Tutorial")
    tutorial.main()

elif choice == "SignUp":
    st.subheader("SignUp")
    signup.main()
    
elif choice == "Login":
    st.sidebar.header("Login")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type='password')
    if st.sidebar.checkbox("Login"):
        if email and password:
            obj = collection.find_one({"email": email})
            if obj:
                if (hash.check_hashes(password, obj['password'])):
                    st.info('Logged in as ' + obj['email'])
                    dashboard.main(email)
            else:
                st.warning('Invalid Username or Password, please try again')




if st.sidebar.button('Like the app👍'):
    st.balloons()

st.sidebar.markdown('![GitHub top language](https://img.shields.io/github/languages/top/tuminzee/PredictCovid?style=for-the-badge)  [![Github Repo](https://img.shields.io/badge/GitHub-Repo-green?style=for-the-badge&logo=appveyor)](https://github.com/tuminzee/PredictCovid)')
st.sidebar.markdown('![GitHub contributors](https://img.shields.io/github/contributors/tuminzee/PredictCovid?style=for-the-badge) ![GitHub forks](https://img.shields.io/github/forks/tuminzee/PredictCovid?label=Fork&style=for-the-badge)')
st.sidebar.markdown('![forthebadge](https://forthebadge.com/images/badges/for-you.svg) ![ForTheBadge built-with-love](https://ForTheBadge.com/images/badges/built-with-love.svg)')



