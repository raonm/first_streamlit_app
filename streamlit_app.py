import streamlit
import pandas

streamlit.title('My Mom-s new healthy diner') 
streamlit.header('Breakfast Favorates')

streamlit.text('🥣 Omega 3 Blueberry Oatmeal') 
streamlit.text('🥗 Kale, Spinach and Rocket smoothie') 
streamlit.text('🐔 Hard boiled free-range eggs') 
streamlit.text('🥑🍞 avacado Toast') 

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Read the data from the file into the app
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avacado','Strawberries'])

# Display the table on the page.
