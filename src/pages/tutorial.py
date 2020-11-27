import streamlit as st
from pymongo import MongoClient

import src.assets.hash as hash


def main():
    
    st.sidebar.title("Tutorial")
    st.sidebar.info("This page conatins all the basic info about the app")

    # Youtube vide link 
    st.text("Watch the tutorial 👀")
    st.video('https://youtu.be/Yw6u6YkTgQ4');
    # st.video('https://www.youtube.com/watch?v=OVTwE3rf0-w')
    # if not hasattr(st, "client"):

    

if __name__ == "__main__":
    main()