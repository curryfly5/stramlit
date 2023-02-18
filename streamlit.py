import streamlit as st

# Create main function
def main():
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox("Choose a page", 
                                ["Home", "About", "Contact"])
    if page == "Home":
        home()
    elif page == "About":
        about()
    elif page == "Contact":
        contact()

# Create page functions
def home():
    st.title("Homepage")
    st.write("This is the content of the Homepage")

def about():
    st.title("About")
    st.write("This is the content of the About page")

def contact():
    st.title("Contact")
    st.write("This is the content of the Contact page")

# Run main function
if __name__ == "__main__":
    main()
