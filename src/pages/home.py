import streamlit as st


def main():
    st.title("""Covid-19 Detection using Deep Learning🏠🏡""" )
    st.write("Home from the pages")
    st.sidebar.title("Home")
    st.sidebar.info("This is the home page, it conatins all the basic info about the app")

    # Youtube vide link 
    st.subheader("Watch the tutorial 👀")
    st.video('https://www.youtube.com/watch?v=Yw6u6YkTgQ4')



if __name__ == "__main__":
    main()