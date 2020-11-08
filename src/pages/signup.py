import streamlit as st
from pymongo import MongoClient

import validateEmail as validateEmail
import hash as hash

client = MongoClient("mongodb+srv://admin:admin@cluster0.wi5ns.gcp.mongodb.net/predictCovid?retryWrites=true&w=majority")
db = client.get_database('predictCovid')
collection = db.userData


def main():

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Passwrod", type="password")
    if st.button("SignUp"):
        if username and email and password:
            if collection.find_one({'Email': email}):
                st.error('This email is taken, please try again with a different email')

            if validateEmail.validateEmail(email):
                st.info("Valid Email")
            else:
                haheshPassword = hash.make_hashes(password)
                collection.insert_one({'username': username, 'email': email, 'password':haheshPassword})
                st.info('Signed Up, please login from the sidebar')


if __name__ == "__main__":
    main()
