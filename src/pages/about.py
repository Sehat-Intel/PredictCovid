import streamlit as st
import base64
import importlib

def render_page(menupage):
    menupage.write()

def render_md(md_file_name):
    st.markdown(get_file_content_as_string(md_file_name))

def get_file_content_as_string(path):
    response = open(path, encoding="utf-8").read()
    return response

def show_code(file_name):
    return get_file_content_as_string(file_name)

def main():
    st.title("About 🚀")

    st.sidebar.title("About")
    # render_md("resources/README.md")
    st.sidebar.info("Please let us know what do you think about it!")

    if st.button('Click here if you like the app!'):
        st.balloons()


    
    
if __name__ == "__main__":
    main()
