import streamlit as st
import pandas as pd
import pickle


# Top recommendations
st.title("Top Book📖 Recommendations 🔖")

df = pickle.load(open('popular.pkl', 'rb'))
df = pd.DataFrame(df)

df['Image-URL-S_x'] = df['Image-URL-S_x'].fillna('https://via.placeholder.com/150')  # Placeholder for missing images
df['Book-Title'] = df['Book-Title'].fillna('No Title Available')
df['Book-Author_x'] = df['Book-Author_x'].fillna('Unknown Author')
df['avg_ratings'] = df['avg_ratings'].fillna(0.0)
df['num_ratings'] = df['num_ratings'].fillna(0)


books_per_row = 5


for i in range(0, len(df), books_per_row):
    cols = st.columns(books_per_row)
    for col, (_, row) in zip(cols, df.iloc[i:i + books_per_row].iterrows()):
        with col:
            
            st.image(row["Image-URL-S_x"], width=250)  
            st.markdown(f"**{row['Book-Title']}**")
            st.write(f"Author: {row['Book-Author_x']}")
            st.write(f"Avg Rating: {row['avg_ratings']:.2f}")
            st.write(f"Num Ratings: {row['num_ratings']}")