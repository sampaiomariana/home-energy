from os import write 
import streamlit as st
import Pages.cadastro.usuario as user
import Pages.cadastro.tomada as tomada
import Pages.cadastro.dispositivo as dispositivo
import Pages.home.home as home
import Pages.dash.dash as dash

st.title('Home energy monitoring')

st.sidebar.title('Menu')
page_home = st.sidebar.selectbox('Opções',['Home','Cadastrar usuário','Cadastrar tomada','Cadastrar dispositivo','Conectar tomada e dispositivo','Dashboard'])

if page_home == 'Home':
    home.home()

if page_home == 'Cadastrar usuário':
    user.usuario()

    
if page_home == 'Cadastrar tomada':
    tomada.tomada()

   
if page_home == 'Cadastrar dispositivo':
    dispositivo.dispositivo()

if page_home == 'Dashboard':
    dash.dash()