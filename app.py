import requests
from bs4 import BeautifulSoup as bs
import logging 
import os
import streamlit as st
from Src.google_main import scrap_images

st.set_page_config(page_title='Image Scraper',page_icon=':camera:',layout='wide')

st.title('Google Image Scraper')

st.markdown('### _Enter a search term to scrape images from Google Images_')
name=st.text_input('hidden',label_visibility='collapsed')


if name is not None and name.strip() != '':
    bar=st.progress(0)

    
    import time
    for i in range(101):
        time.sleep(0.1)
        bar.progress(i,text='Loading')
    
    status=scrap_images(name)
    st.error('Scraping Failed') if status is None else st.success('Scraping Completed')
        
    
    