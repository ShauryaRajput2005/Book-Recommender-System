import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title='Top Recommendations', page_icon='📚', layout='wide')

# Styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #2c3e50;
        text-align: center;
    }
    .recommendation-header {
        color: #e74c3c;
        margin-top: 20px;
    }
    .book-info {
        color: #34495e;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



st.title("📚 Book Recommender System 📖")

# Load data
books = pickle.load(open("final.pkl", "rb"))
data = pd.DataFrame(books) 

with open("pt.pkl", "rb") as file:
    pt = pickle.load(file)


def recommend(book_title):
    if book_title not in pt.index:
        st.error("Book not found in the pivot table.")
        return pd.DataFrame()

    try:
        distances = pt.loc[book_title].values 
    except KeyError:
        st.error("KeyError: Book title not found in the similarity matrix.")
        return pd.DataFrame()

    book_indices = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    recommended_books = data.iloc[[i[0] for i in book_indices]]
    return recommended_books


book = st.selectbox("Pick a Book:", data["Book-Title"].values)

if st.button("💡 Recommend"):
    recommendations = recommend(book)
    if recommendations.empty:
        st.error("No recommendations found. Please try another book.")
    else:
        st.markdown("<h2 class='recommendation-header'>🎉 Recommended Books</h2>", unsafe_allow_html=True)

        for _, book_row in recommendations.iterrows():
            st.markdown(f"### {book_row['Book-Title']}") 

            image_url = book_row.get('Image-URL-L', None)  
            if image_url:
                st.image(image_url, width=150, caption=book_row['Book-Title'])

            st.write(f"**Author:** {book_row.get('Book-Author', 'N/A')}")  
            st.write(f"**Rating:** {book_row.get('Book-Rating', 'Unknown')}") 
            st.write(f"**Year of Publication:** {book_row.get('Year-Of-Publication', 'N/A')}")  
