import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def b64(file):
    
    #PIL to base64 String
    img = Image.open(file)
    im_file = BytesIO()
    img.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue()
    im_b64 = base64.b64encode(im_bytes)        
    st.write(im_b64) #encoded image base64 string

def imgc(text):
    #base64 to PIL Image
    im_bytes = base64.b64decode(text) 
    im_file = BytesIO(im_bytes) 
    img64 = Image.open(im_file)       
    
    st.image(img64, use_column_width=True)  #decoded image

def main():

    st.set_option('deprecation.showfileUploaderEncoding', False)

    file = st.file_uploader("Upload Image here ['jpg', 'png', 'jpeg']", type=["jpg", "png", "jpeg"])
    st.write("                                              or")
    text = st.text_area("Enter base64 string of image")
    if file is not None or text is not None:
        conv = st.radio('Conversion :', ('Image to base64', 'base64 to Image'))      
        if conv=='Image to base64':
            if file is None:
                st.text("You haven't uploaded an image file")
            else:
                b64(file)
        if conv=='base64 to Image':
            if text=="":
                st.text("You haven't entered the base64 string")
            else:
                imgc(text)

if __name__ == "__main__":
    main()

