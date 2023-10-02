import streamlit as st
import linksgetter  # Replace with your actual function

import streamlit as st
# Replace with your actual function

# Streamlit UI configuration
st.set_page_config(
    page_title="Tamil Movie Download Links Getter",
    page_icon="🎬",
    layout="centered",  # Center the content
)

# Define the Streamlit app
def main():
    st.title("Tamil Movie Download Links Getter")

    # Input field for movie name
    movie_name = st.text_input("Enter Tamil Movie Name")

    # Search button
    if st.button("Search"):
        if movie_name:
            # Call your Python function to fetch download links
            download_links = linksgetter.searchMovie(movie_name)

            # Display download links
            st.subheader("Download Links")
            if download_links:
                for idx, link in enumerate(download_links[:5], start=1):
                    st.write(f"{idx}. [{link}]({link})")
            else:
                st.warning("No download links found for this movie.")

if __name__ == "__main__":
    main()

