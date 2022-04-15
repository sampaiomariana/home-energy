from os import write 
import streamlit as st

def usuario():
    st.subheader('Cadastro do usuário')

    with st.form(key = 'cadastrar_usuario'):
        input_name = st.text_input(label = 'Insira seu nome')
        input_email = st.text_input(label = 'Insira seu e-mail')
        input_senha = st.text_input(label = 'Insira sua senha')
        input_buttom_submit = st.form_submit_button('Cadastrar')
        input_buttom_access = st.form_submit_button('Acessar a conta')

    if input_buttom_submit:
        st.subheader('Seus dados foram cadastrados com sucesso')
        st.write(f'Nome:{input_name}')
        st.write(f'Email:{input_email}')

    if input_buttom_access:
        st.subheader(f'Bem vindo a sua conta')
    

