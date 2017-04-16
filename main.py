import json
import mmap 
from tqdm import tqdm

path_ids = './py_temp_existing_ids.txt'
path_data = './new_ids.json'
new_results = set()

with open(path_data, 'r') as _in: 
	new_ids = json.load(_in)
	_in.close()

with open(path_ids, 'r+b') as _file:
    mm = mmap.mmap(_file.fileno(), 0)
	

    with tqdm(total=len(new_ids.keys())) as pbar:
        for _id in new_ids:
            if not mm.find(str(_id).encode()) != -1:
                new_results.add((_id, new_ids[_id]))
            else:
                continue
            pbar.update()
    mm.close()
    _file.close()
    

print(str(len(new_results)))
