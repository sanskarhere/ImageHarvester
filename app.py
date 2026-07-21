import requests
from bs4 import BeautifulSoup as bs
import logging 
import os
import streamlit as st
from Src.google_main import scrap_images
from Src.helper import zip_images

st.set_page_config(page_title='Image Scraper',page_icon=':camera:',layout='wide')

st.title('Image Harvester')

st.markdown('### _Enter a search term to scrape images from Google Images_')
name=st.text_input('hidden',label_visibility='collapsed')


if name is not None and name.strip() != '':
    bar=st.progress(0)

    
    import time
    for i in range(101):
        time.sleep(0.1)
        bar.progress(i,text='Loading')
    
    status=scrap_images(name)
    #st.error('Scraping Failed') if status is None else st.success('Scraping Completed')
        


    st.subheader('Download Images')
    logging.info('Zipping the images')
    zip_status=zip_images(name)

    path=os.path.join(os.getcwd(),f'{name}.zip')
    if zip_status:
        st.success('Folder Compressed Successfully')
        
        
        with open(path,'rb') as f:
            st.download_button(
                '''💾 Click Here to Download ZIP''',
                data=f,
                file_name=f'{name}.zip',
                mime='application/zip'

            )
            
    
    else:
        st.warning(f"The local folder '{path}' does not exist yet. Run your scraper first!")

