import streamlit as st
import src.pages.uploadImage as uploadImage
import src.pages.url as url
import src.pages.about as about


def main():
    nav = st.radio("Navigate to",["Upload X-ray and Predict","X-ray Url and Predict", "About"], key=1)


    if nav == "Upload X-ray and Predict":
        uploadImage.main()


    if nav == "X-ray Url and Predict":
        url.main()

    if nav == "About":
        about.main()


if __name__ == "__main__":
    main()