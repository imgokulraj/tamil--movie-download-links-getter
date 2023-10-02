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
            if type(download_links) is str : 
                st.write("No results found for the movie")
            else : 
            # Display download links
                for movie_data in download_links:
                    st.subheader(movie_data["movie-name"])
                    for link_info in movie_data["links"]:
                        st.write(f"Quality: {link_info['quality']}")
                        st.write(f"Link: [{link_info['link']}]({link_info['link']})")
                    st.markdown("---")  # Add a separator between movies

if __name__ == "__main__":
    main()

