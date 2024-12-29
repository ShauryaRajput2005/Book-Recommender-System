import streamlit as st

Top_page=st.Page("C:\\Users\\Asus\\Downloads\\MLProjects\\book_rec\\page1.py",title='Top Book📖 Recommendations', icon='📔') 
personal=st.Page("C:\\Users\\Asus\\Downloads\\MLProjects\\book_rec\\page2.py",title='Get Personalised Recommendations', icon='🧑‍🎓')


pg=st.navigation([Top_page,personal])
st.set_page_config(page_title='Top Recommendations',page_icon='📚',layout='wide')
pg.run()
