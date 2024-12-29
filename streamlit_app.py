import streamlit as st

Top_page=st.Page("page1.py",title='Top Book📖 Recommendations', icon='📔') 
personal=st.Page("page2.py",title='Get Personalised Recommendations', icon='🧑‍🎓')


pg=st.navigation([Top_page,personal])
st.set_page_config(page_title='Top Recommendations',page_icon='📚',layout='wide')
pg.run()
