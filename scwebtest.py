import streamlit as st
import pandas as pd
from connection import conn

#Create a function for each page of your website
def home():
    st.title("scRNA-seq")
    st.write("scRNA-seq stands for single-cell RNA sequencing. It is a powerful technology used to profile gene expression at the single-cell level.")

def marker():
    st.title("Marker Gene Search")
    st.write("Please enter a gene symbol (e.g. MAPK1) to search for its expression in the database:")
    #Add an input box
    gene_symbol = st.text_input("")
    if st.button("Submit"):
        #Connect to MySQL
        # cursor = conn.cursor()
        #Query the database
        # query = "SELECT * FROM genes WHERE gene_symbol = %s"
        # cursor.execute(query, (gene_symbol,))
        #Fetch the result
        # result = cursor.fetchone()
        #if result:
            #Display the result
            #st.write(pd.DataFrame(list(result),columns=["Gene Symbol","Expression Level","Cell Type","Cluster"]))
        #else:
            #st.write("This gene symbol does not exist in the database.")

def batch():
    st.title("Batch Effects")
    st.write("Batch effects occur when there are systematic differences between experimental batches that lead to erroneous conclusions about the data.")

#Add a sidebar with a navigation menu to the app.py file
st.sidebar.title("Navigation")
#Use streamlit’s st.sidebar.button() to create a navigation menu
#and link it to each function
page = st.sidebar.radio("Go to",("Home","Marker Gene Search","Batch Effects"))

#Add an if statement to main() to call the functions when a button
#is clicked.
def main():
    if page == "Home":
        home()
    elif page == "Marker Gene Search":
        marker()
    elif page == "Batch Effects":
        batch()

if __name__ == "__main__":
    main()
