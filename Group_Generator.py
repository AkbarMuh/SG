import os
import sys
import streamlit as st
from numpy import random
import pandas as pd

st.set_page_config(
    page_title="Regenerator Group",
    initial_sidebar_state="expanded",
    page_icon="🧠",
    menu_items={
        'Get Help': 'https://github.com/xtekky/gpt4free/blob/main/README.md',
        'Report a bug': "https://github.com/xtekky/gpt4free/issues",
        'About': "### gptfree GUI",
    },layout="wide",
)
st.markdown("<h1 style='text-align: center; color: white;'>Regenerator Group</h1><br><br>", unsafe_allow_html=True)


Aslab = ["GNI","ARR","LIP","BDA","PAD"]
SG = [
"TIARA SABRINA",
"Syahreza Adnan Al Azhar",
"Zaky Al Fatih Nata Imam",
"Bagas Eko Tjahyono Putro",
"Valentino Hartanto",
"Muhammad Dwiva Arya Erlangga",
"Rafie aydin ihsan",
"Rifqi Maheswara Karuniyawan",
"Ade Ikmal Maulana",
"Iksan Oktav Risandy",
"Imelda Damayanti",
"Farah Saraswati"
]

random.shuffle(SG)
acak= SG[:5],SG[5:10],SG[10:15],Aslab

df = pd.DataFrame(
   acak,
   columns=('Kelompok %d' % i for i in range(1,6)))

st.dataframe(df,hide_index=True,width=3000)