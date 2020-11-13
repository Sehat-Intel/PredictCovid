import streamlit as st
from pymongo import MongoClient
import hash as hash

client = MongoClient('localhost', 27017)
db = client['predict-covid']
collection = db['user-data']


def main():
    
    st.sidebar.title("Tutorial")
    st.sidebar.info("This page conatins all the basic info about the app")

    # Youtube vide link 
    st.subheader("Watch the tutorial 👀")
    st.video('https://www.youtube.com/watch?v=OVTwE3rf0-w')
    # if not hasattr(st, "client"):
    #     st.client = MongoClient('mongodb://127.0.0.1/local')

    # collection = st.client.local.user
    # st.title('Login')
    # name = st.text_input('name')
    # password = st.text_input('password' ,type="password")

    

    # if st.button("Save"):
    #     if name and password:
    #         hashed = hash.make_hashes(password)
    #         collection.insert_one({'name': name, 'password': hashed})

    # if st.button("Login"):
    #     if name and password:
    #         obj = collection.find_one({"name": name})
            
    #         # st.text(obj['password'])
    #         st.text(hash.check_hashes(password, obj['password']))


    # if st.button("Show list of users"):
    #     st.write(list(collection.find()))
    

if __name__ == "__main__":
    main()