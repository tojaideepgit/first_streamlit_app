import streamlit
import pandas

streamlit.title('My parent new healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 and Blueberry oatmeal')
streamlit.text('Spinach smoothie')
streamlit.text('hardboiled eggs')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


