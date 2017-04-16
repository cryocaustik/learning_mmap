from os.path import isfile
import requests 
import mmap 
from tqdm import tqdm

path = 'dev_pad/py_temp_existing_ids.txt'

with open(path, 'r+b') as _file:
    mm = mmap.mmap(_file.fileno(), 0)
    
    response = requests.get('https://zkillboard.com/api/history/20161201/')
    if response.status_code == 200:
        results = response.json()
        new_results = set()
        
        with tqdm(total=len(results.keys())) as pbar:
            for _id in results:
                if mm.find(str(_id).encode()) != -1:
                    new_results.add((_id, results[_id]))
                else:
                    continue
                pbar.update()
    mm.close()
    _file.close()
    

print(str(len(new_results)))
