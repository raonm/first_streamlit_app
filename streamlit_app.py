import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Mom-s new healthy diner') 
streamlit.header('Breakfast Favorates')

streamlit.text('🥣 Omega 3 Blueberry Oatmeal') 
streamlit.text('🥗 Kale, Spinach and Rocket smoothie') 
streamlit.text('🐔 Hard boiled free-range eggs') 
streamlit.text('🥑🍞 avacado Toast') 

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# import pandas

# Read the data from the file into the app
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# Display the table on the page.
# New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
        streamlit.error("please select a fruit for information")
   else:
       fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
       fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       streamlit.dataframe(fruityvice_normalized) 
except URLError as e:
    streamlit.error()
# import requests

# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# Take the json version of the data and normalizes it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it to screen as a table
streamlit.dataframe(fruityvice_normalized)

# Don't run anything beyond this point
streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load List Contains:")
streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list 
fruit_choice = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# This code will not work for now, but just keep it here
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
