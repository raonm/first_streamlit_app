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
# Create the repeatable code block ( called a function )
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
        streamlit.error("please select a fruit to get information")
   else:
       back_from_function = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function) 
except URLError as e:
    streamlit.error()
# import requests

streamlit.header("View Our Fruit List - Add Your Favorites!")
#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()
# Add a button to load the fruit
if streamlit.button('Get Fruit List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   my_cnx.close()
   streamlit.dataframe(my_data_rows)

# Allow end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
         return "Thanks for add " + New_Fruit
streamlit.stop()

# Take the json version of the data and normalizes it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it to screen as a table
streamlit.dataframe(fruityvice_normalized)

# Don't run anything beyond this point
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

streamlit.header("The Fruit Load List Contains:")
streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list 
fruit_choice = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# This code will not work for now, but just keep it here
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
