import streamlit as st 
import ProjectPropsal as pp

st.sidebar.title("Cover Letter Customizer")

user_menu=st.sidebar.selectbox("Select an option",["Project Description","Job Profile"])
my_name=st.sidebar.text_input("Enter Your Name:")
client_name=st.sidebar.text_input("Enter Client Name:")

if(user_menu=='Project Description'):
    description=st.sidebar.text_area("Enter Project Description:")        
elif(user_menu=='Job Profile'):
    description=st.sidebar.text_input("Enter Job Profile Name:")
    
if st.sidebar.button('Generate'):
    if(user_menu=='Project Description'):
        response=pp.project(description,client_name,my_name)
        st.write(response)
    elif(user_menu=='Job Profile'):
        response=pp.job(description,client_name,my_name)
        st.write(response)
    

