from os import write 
import streamlit as st

def dispositivo():
    st.subheader('Cadastro do dispositivo')

    with st.form(key = 'cadastrar_dispositivo'):
        input_name_dispositivo = st.text_input(label = 'Insira o nome do seu dispositivo')
        input_buttom_submit = st.form_submit_button('Cadastrar')
     
        if input_buttom_submit:
            st.subheader('O seu dispositivo foi cadastrado com sucesso')
            st.write(f'Nome:{input_name_dispositivo}')
