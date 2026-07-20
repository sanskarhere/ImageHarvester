import logging 
import os
from datetime import datetime

date=datetime.now().strftime('%d-%m-%Y')
print(date)

path=os.path.join(os.getcwd(),'Logs',date)
print(path)


logging.basicConfig(filename=path,level=logging.DEBUG,format='[%(asctime)s]-%(levelname)s - %(message)s')

logging.debug('Logging Info')