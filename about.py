import streamlit as st

def show_about_contact():
    st.markdown("---")  # horizontal line
    st.subheader("About")
    st.write("""
    This is a **Bangalore House Price Prediction App** developed using **Python, Scikit-Learn, and Streamlit**.  
    The model predicts house prices based on the following features:  
    - Total Square Feet  
    - Number of Bathrooms  
    - Number of BHK  
    - Location of the property
    """)

    st.subheader("Contact")
    st.write("""
    **Developer:** Niveditha   
    **Email:** nivegowda@example.com  
    **LinkedIn:** (www.linkedin.com/in/niveditha-89ba04356)  
    **GitHub:** [github.com/niveditha](https://github.com/Nivedithagowda2)
    """)

