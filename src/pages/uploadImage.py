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
import imgto64 as imgto64
from pymongo import MongoClient
import config as config

Reports = config.db['records']
Users = config.db['users']

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
        st.write("Probability : {:.2f}".format(((1-prob[0,0]))*100),"%")
        return "Covid","{:.2f} %".format((1-prob[0,0])*100)
    else:
        st.info("Normal")
        st.write("Probability : {:.2f}".format((prob[0,0])*100),"%")
        return "Normal","{:.2f} %".format((prob[0,0])*100)

    st.image(image, use_column_width=True)


def main(email):
    st.sidebar.write("""
        # Covid-19 Detection using Deep Learning
        """
        )
    
    st.sidebar.info("Upload the PA view Chest X-ray, and our app will will do the magic 🧙‍♂️")
    st.info("Our model has baseline accuracy of 94%")
    st.title("Predict the Probability of Covid-19 🧙‍♂️")
  
    #st.warning("You have two options here, 1) Upload your X-ray 2) Test the app with test images")
    st.subheader("1) Upload your PA View X-ray 📤")

    st.set_option('deprecation.showfileUploaderEncoding', False)

    file = st.file_uploader("Upload Image here ['jpg', 'png', 'jpeg']", type=["jpg", "png", "jpeg"])

    if file is not None:      
        if st.button("Predict"):
            if file is None:
                st.text("You haven't uploaded an image file")
            else:
                image = Image.open(file)
                base64string = imgto64.b64(file)
                status, percent = predict(image)
                print(email)
                user = Users.find_one({'email': email})
                Reports.insert_one({
                    'email': email,
                    'username': user['username'],
                    'status': status,
                    'percent': percent,
                    'message': 'No messages'
                })


    st.subheader("2) Don't have an X-ray? Worry not! Try our app with test images :pick:")
    test_img = st.radio('Select Test Image!', ('Image 1', 'Image 2'))


    if test_img == 'Image 1':
        image = Image.open('test_img/test.jpeg')
        if st.button("Test"):
            predict(image)
        else:
            st.image(image, caption="Test Image 1" ,use_column_width=True)
        
    elif test_img == 'Image 2':
        image = Image.open('test_img/test1.jpg')
        if st.button("Test"):
            predict(image)
        else:
            st.image(image, caption="Test Image 1" ,use_column_width=True)

if __name__ == "__main__":
    main(email)

