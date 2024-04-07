import streamlit as st
import pandas as pd
from streamlit.elements.balloons import BalloonsMixin

st.title('Apartamentos no Rio de Janeiro')

rioAptos = pd.read_csv("rioAptos.csv")
st.header('A base: ')
st.write(rioAptos)


bairrosLista = rioAptos['bairro'].unique()

st.header('Selection Box: ')
e1 = st.selectbox('Selecione os bairros', bairrosLista)
st.write('Bairros escolhidos: ', e1)
dfa = rioAptos[rioAptos['bairro'] == e1]
st.write(dfa)

st.header('Multiselect: ')
e2 = st.multiselect('Selecione os bairros', bairrosLista)
st.write('Bairros escolhidos: ', e2)
dfb = rioAptos[rioAptos['bairro'].isin(e2)]
st.write(dfb)

st.header('Radio: ')
e3 = st.radio('Selecione os bairros', bairrosLista)
st.write('Bairros escolhidos: ', e3)
dfc = rioAptos[rioAptos['bairro'] == e3]
st.write(dfc)

st.title('')
st.title('')
st.title('')
st.title('')
st.title('')
st.title('')
st.title('')
st.title('')
st.title('')
surpresa = st.button("Botão Secreto")


if (surpresa == True):
    st.balloons()
    surpresa = False