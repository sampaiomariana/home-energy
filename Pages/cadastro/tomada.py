from os import write 
import streamlit as st

def tomada():
    st.subheader('Cadastro da tomada')

    with st.form(key = 'cadastrar_tomada'):
        input_name_tomada = st.text_input(label = 'Insira o nome da tomada')
        input_ambiente = st.text_input(label = 'Insira em qual ambiente está sua tomada')
        input_buttom_submit = st.form_submit_button('Cadastrar')
     
        if input_buttom_submit:
            st.subheader('A tomada foi cadastrada com sucesso')
            st.write(f'Nome:{input_name_tomada}')
            st.write(f'Email:{input_ambiente}')
