import requests 
from Src.logger import logging
import os
import shutil

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

                

def zip_images(name:str)->str:
    path=os.path.join(os.getcwd(),name)
    print(path)

    zip_name=name

    if os.path.exists(path):

        #shutil automatically compresses the directory into a zip on hdd _> path
        shutil.make_archive(zip_name,'zip',path)

        return True
    
    else:
        False #folder doesnt exist->warning

