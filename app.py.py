from logging import exception
import streamlit as st
import plotly
import pandas as pd
import plotly.express as px

app = (__name__)

st.title("UAS Data Science: Muh. Fadhil Aqilah. M")
st.sidebar.subheader("Aplikasi Visualisasi Exel & csv.")
uploaded_file = st.sidebar.file_uploader(label="Upload Data Kamu",
                          type= ['csv', 'xlsx'])
global df
if uploaded_file is not None:
   print (uploaded_file)
   print ("Hello!")
   try:
       df = pd.read_csv(uploaded_file)
   except Exception as e:
       print(e)
       df = pd.read_excel(uploaded_file)

global numeric_columns
try:
    st.write(df)
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
except Exception as e:
    print(e)
    st.write("Kasih Masukki Dulu File csv/Exel ta")
    st.write("klik Pojok Kiri Atas")

chart_select = st.sidebar.selectbox(
    label="Silahkan pilih Jenis Visualisasi",
    options=['Scatterplots', 'Lineplot', 'Histogram']
)

if chart_select == 'Scatterplots':
    st.sidebar.subheader("Scatterplot Settings")
    try:
        x_values = st.sidebar.selectbox('x axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('y axis', options=numeric_columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
if chart_select == 'Lineplot':
    st.sidebar.subheader("Lineplot Settings")
    try:
        x_values = st.sidebar.selectbox('x axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('y axis', options=numeric_columns)
        plot = px.line(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
if chart_select == 'Histogram':
    st.sidebar.subheader("Histogram Settings")
    try:
        x_values = st.sidebar.selectbox('x axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('y axis', options=numeric_columns)
        plot = px.histogram(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
