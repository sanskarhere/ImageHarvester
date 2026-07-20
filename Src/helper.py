import requests 
from Src.logger import logging
import os

def fetch_image(link:str)->bytes:
    try:
        res=requests.get(link)
        if res.ok:
            return res.content
    
        else:
            logging.debug('status_code!=200')
    
    except requests.exceptions.RequestException as e:
        print(e)
        logging.error('Fetching Failed Because',e)
        return None


def save_images(name:str,links:list):

    for i in range(len(links)):
        path=os.path.join(os.getcwd(),name,f'{name}-{i}.jpeg')
        print(path)

        os.makedirs(os.path.dirname(path),exist_ok=True)

        content=fetch_image(links[i])

        if content is not None: 
            with open(path,'wb') as f:
                f.write(content)
        
    else:
        return True
    
    return False

                

