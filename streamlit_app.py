import streamlit
import pandas

streamlit.title('My Mom-s new healthy diner') 
streamlit.header('Breakfast Favorates')

streamlit.text('🥣 Omega 3 Blueberry Oatmeal') 
streamlit.text('🥗 Kale, Spinach and Rocket smoothie') 
streamlit.text('🐔 Hard boiled free-range eggs') 
streamlit.text('🥑🍞 avacado Toast') 

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
