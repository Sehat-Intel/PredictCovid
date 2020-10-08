#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 00:22:10 2020

@author: tumin
"""

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import os
import base64
import requests
from io import BytesIO

def import_and_predict(image_data, model):
        size = (128,128)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = image.convert('RGB')
        image = np.asarray(image)
        image = (image.astype(np.float32) / 255.0)

        img_reshape = image[np.newaxis,...]

        prediction = model.predict_classes(img_reshape)
        prob = model.predict_proba(img_reshape)
        return prediction, prob

def predict(image):
    model = tf.keras.models.load_model('model.hdf5')
    prediction, prob = import_and_predict(image, model)
    
    if prediction[0,0] == 0:
        st.warning("Covid-19")
        st.write("Accuray : {:.2f}".format(((1-prob[0,0]))*100),"%")
    else:
        st.info("Normal")
        st.write("Accuracy : {:.2f}".format((prob[0,0])*100),"%")

    st.image(image, use_column_width=True)


def main():
    st.sidebar.write("""
        # Covid-19 Detection using Deep Learning
        """
        )
    st.sidebar.info("Upload the PA view Chest X-ray, and our app will will do the magic 🧙‍♂️")
    st.title("Upload X-ray and Predict")
    st.write("Our model has an accuracy of 94%")

    st.set_option('deprecation.showfileUploaderEncoding', False)

    file = st.file_uploader("Upload Chest X-ray(PA view)", type=["jpg", "png", "jpeg"])

    if file is not None:      
        if st.button("Predict"):
            if file is None:
                st.text("You haven't uploaded an image file")
            else:
                image = Image.open(file)
                predict(image)


    st.subheader("Want to try our model with some test images?")
    image = Image.open('test_img/test.jpeg')
    st.image(image, caption="Test Image 1" ,use_column_width=False)
    if st.button("Select this one"):
        image = Image.open('test_img/test.jpeg')
        predict(image)

    image = Image.open('test_img/test1.jpg')
    st.image(image, caption='Test Image 2', use_column_width=False)
    if st.button("or select this one"):
        image = Image.open('test_img/test1.jpg')
        predict(image)

if __name__ == "__main__":
    main()

