import streamlit
import pandas

streamlit.title('My parent new healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 and Blueberry oatmeal')
streamlit.text('Spinach smoothie')
streamlit.text('hardboiled eggs')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
