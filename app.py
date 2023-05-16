import streamlit as st

# Set page title, meta description, and logo
st.set_page_config(
    page_title="AI Workshop Summary",
    page_icon="logo.png",  # replace with your logo file
    initial_sidebar_state="expanded",
    layout='centered'
)

def main():
    # Display app title
    st.title("AI Workshop Summary by Frej Andreassen")

    # Read markdown file
    with open("workshop_summary.md", "r", encoding='utf-8') as file:
        markdown_text = file.read()

    # Display markdown using Streamlit
    st.markdown(markdown_text)

if __name__ == "__main__":
    main()
