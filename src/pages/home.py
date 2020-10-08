import streamlit as st
import streamlit.components.v1 as components


def main():
    st.title("Predict Covid ✨")
    st.subheader("""An app which detects the probablity of Covid-19 using Deep Learning""" )
    st.sidebar.title("Home")
    st.sidebar.info("This page conatins all the basic info about the app")
    st.sidebar.warning("Use the top corner buttons to explore the additional funcationality of the app")
    st.sidebar.markdown('Made with ❤️ in India')

    # Youtube vide link 
    st.subheader("Watch the tutorial 👀")
    st.video('https://www.youtube.com/watch?v=Yw6u6YkTgQ4')
    

if __name__ == "__main__":
    main()