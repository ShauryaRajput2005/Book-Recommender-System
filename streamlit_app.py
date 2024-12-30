import streamlit as st
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

Top_page=st.Page("page1.py",title='Top Book📖 Recommendations', icon='📔') 
personal=st.Page("page2.py",title='Get Personalised Recommendations', icon='🧑‍🎓')


pg=st.navigation([Top_page,personal])
pg.run()
