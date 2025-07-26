import streamlit as st
import pandas as pd

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title and intro
st.title("Simple website ")
st.write("This is a simple Streamlit app with buttons and a bit of CSS styling, Using python!")

# Button 1: Show welcome message
if st.button("Click Me!"):
    st.image("rickroll.gif", caption="Never gonna give you up", use_column_width=True)
    st.success("ew3aa el zorar sha8alllll!!!!")


# Button 2
show_secret = st.checkbox("Show me a secret")
if show_secret:
    st.info("3eeb 3alek ya handasa")
    st.image("rickroll.gif", caption="Never gonna give let you down", use_column_width=True)
    st.info("eh dah hena kaman!")


st.subheader("📁 Upload Your CSV to View It")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # --- Show Table Under Dropdown ---
    with st.expander(" Click to show table"):
        st.dataframe(df)
else:
    st.info("Please upload a CSV file to see the table.")

# Footer
st.markdown("<hr><left>Shout out ly Abdullah 🫡</left>", unsafe_allow_html=True)
