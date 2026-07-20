from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from Src import helper
from bs4 import BeautifulSoup as bs
from Src.logger import logging
import time


def scrap_images(name): 

    #setting
    options=Options()

    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--log-level=3")

    # Hide webdriver properties from anti-bot detectors
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Set a natural desktop browser profile
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

    try:
        #run chrome instance
        driver=webdriver.Chrome(options=options)


        #open Google Images  tab /webpage
        driver.get(f'https://www.google.com/search?q={name}&tbm=isch')
        logging.info(f"Scraping images for {name} from Google Images")

        #Get Html content of webpage
        
        time.sleep(5) # Wait for 30 seconds to allow the page to load completely
        page=driver.page_source
          

        #parse html content
        soup=bs(page,'lxml')

        #find all links from this html doc 
        print(page)
        links=soup.find_all('img',class_='DS1iW')
        images=[]
        for image in links:
            # if 'images' in image.img['src']:
                images.append(image['src'])
        images
        print(links)
        print(images)

        #download images 
        helper.save_images(name,images)

        return True

    except Exception as e:
        logging.error(f"Error occurred while scraping images for {name}: {e}")
        return None
    
    finally:
        driver.quit()  # Close the browser window after scraping is done

        

        

