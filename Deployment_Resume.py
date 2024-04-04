import pickle
import streamlit as st
from PIL import Image
import hydralit_components as hc

# Loading the Best Model Decision Tree
pickle_in = open('Resumes.pkl', 'rb')
Resumes = pickle.load(pickle_in)

st.markdown("<h1 style='text-align: center; text-border:5px solid red; color: Dark Blue; font-size:80px; '>Resumes Analyser</h1>", unsafe_allow_html=True)

#Background Image
import base64
def add_bg_from_local(image_file):
    with open(image_file,"rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-Image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: Cover
    }}
    </style>""",
    unsafe_allow_html=True
    )
add_bg_from_local('Image-Resume.jpg')


# specify the primary menu definition
menu_data = [
    {'icon': "fa fa-address-card", 'label':"Resume Parser"},
    {'icon': "far fa-file-word", 'label':"Resume Classification"}
]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    login_name=None,
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)
