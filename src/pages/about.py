import streamlit as st
import base64
from PIL import Image
import streamlit.components.v1 as components



def main():

    st.sidebar.title("About")
    # render_md("resources/README.md")
    st.sidebar.info("Please let us know what do you think about it!")



    st.markdown('![GitHub top language](https://img.shields.io/github/languages/top/tuminzee/PredictCovid?style=for-the-badge)  [![Github Repo](https://img.shields.io/badge/GitHub-Repo-green?style=for-the-badge&logo=appveyor)](https://github.com/tuminzee/PredictCovid) ![GitHub contributors](https://img.shields.io/github/contributors/tuminzee/PredictCovid?style=for-the-badge) ![GitHub forks](https://img.shields.io/github/forks/tuminzee/PredictCovid?label=Fork&style=for-the-badge)')
    
    
    st.subheader("Meet Our Team")
    nav = st.radio("🚀🚀🚀",["Fenil Mehta","Krunal Vasoya","Tumin Sheth"])
    if nav == "Fenil Mehta":
        st.subheader("Fenil Mehta")
        st.markdown('[**LinkedIn**](https://www.linkedin.com/in/fenilmehta/), [GitHub](https://github.com/mmehtafenil) ')


        st.image('https://scontent.fraj1-1.fna.fbcdn.net/v/t1.0-9/61701274_1123202517864590_8437565335774691328_o.jpg?_nc_cat=108&_nc_sid=09cbfe&_nc_ohc=A5HaTjgE_FUAX9UOXzy&_nc_ht=scontent.fraj1-1.fna&oh=b6d434721b8bd5f7c2fd6dcd5c6daa9a&oe=5FA47C85', width=400)
        CSS = """
        h1 {
            color: red;
        }
        """
        st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


    if nav == "Krunal Vasoya":
        st.subheader("Krunal Vasoya")    
        st.markdown('[**LinkedIn**](https://www.linkedin.com/in/krunal-vasoya-29a3691b5), [Github](https://github.com/krunal310) ')
        st.image('https://ca.slack-edge.com/T01BJES4D55-U01BSKSHWUE-38c35bc21a3f-512', width=400)
        CSS = """
        h1 {
            color: orange;
        }
        """
        st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

    if nav == "Tumin Sheth":
        st.subheader("Tumin Sheth")
        st.markdown('[**LinkedIn**](https://www.linkedin.com/in/fenilmehta/), [Github](upload://7FxfXwDqJIZdYJ2QYADywvNRjB.png) ')
        st.image('https://scontent.fraj1-1.fna.fbcdn.net/v/t1.0-9/82964587_2468658349912598_1034881642805592064_o.jpg?_nc_cat=107&_nc_sid=09cbfe&_nc_ohc=RCNghyTbZHUAX-io3uQ&_nc_ht=scontent.fraj1-1.fna&oh=e5c440e75d4ae80b9bac9d47c7fe1a88&oe=5FA67127', width=400)


if __name__ == "__main__":
    main()
