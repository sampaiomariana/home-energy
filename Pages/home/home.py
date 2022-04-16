from os import write 
import streamlit as st

def home():
    #st.subheader('Home energy monitoring')


    with st.form(key = 'home'):
        input_name= st.text_input(label = 'Insira o seu nome')
        input_senha = st.text_input(label = 'Insira sua senha')
        input_buttom_submit = st.form_submit_button('Acessar sua conta')
     
        if input_buttom_submit:
            st.subheader(f'Bem vindo @{input_name}!')
         
