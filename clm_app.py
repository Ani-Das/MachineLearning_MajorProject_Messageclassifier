import streamlit as st
import joblib
model = joblib.load('Message_classifier')
st.title('Spam Ham Message Classifier')
ip=st.text_input('Enter your message')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
