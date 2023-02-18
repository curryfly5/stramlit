import streamlit as st

# Create main function
def main():
    st.sidebar.header("Meau")
    page = st.sidebar.selectbox("Choose a page from here ⬇️", 
                                ["Home", "Marker", "Auto-annotation","batch-test"])
    if page == "Home":
        home()
    elif page == "Marker":
        marker()
    elif page == "Auto-annotation":
        anno()
    elif page == "batch-test"
        batch()

# Create page functions
def home():
    st.title("Homepage")
    st.write("This is the content of the Homepage")

def marker():
    st.title("Marker genes")
    st.write("you can search marker gene of specific celltype on this page")

def anno():
    st.title("Auto annotation")
    st.write("Provide your matrix or h5ad, we can help to annotate")
   
def batch():
    st.title("Batch test")
    st.write("Recommend a best method to correct your batch effect")

# Run main function
if __name__ == "__main__":
    main()
