import requests
import os
import random

from .site_data import Site_Data_CLSS, sites_data_dict
from .pretty_print import *

site = "ShareOnline"

class ShareOnline:
    
    def Uploader(file, proxy_list, user_agents):
        try:
            ua = random.choice(user_agents)
            upload_url = sites_data_dict[site]["url"]
            size_limit = f'{sites_data_dict[site]["size_limit"]} {sites_data_dict[site]["size_unit"]}'
            
            
            file_size = os.stat(file).st_size
            file_name = os.path.basename(file)
            file_name = (file_name[:240] + '..') if len(file_name) > 240 else file_name # Changed from 255 to 240 as an additional safety net.
            
            calc_size = Site_Data_CLSS.size_unit_calc(site, file_size)
            
            if calc_size == "OK":
                files_data = {'file': (os.path.basename(file), open(str(file), 'rb'), 'multipart/form-data')}
                
                if proxy_list == []:
                    req = requests.post(url=upload_url, files=files_data, headers={"User-Agent": ua}).json()
                else:
                    req = requests.post(url=upload_url, files=files_data, headers={"User-Agent": ua}, proxies=random.choice(proxy_list)).json()
                return {"status": "ok", "file_name": file_name, "file_url": req.get("data").get("file").get("url").get("short"), "site": site}
            else:
                return {"status": "size_error", "file_name": file_name, "site": site, "exception": "SIZE_ERROR", "size_limit": f"{str(size_limit)}"}
                
        except Exception as e:
            return {"status": "error", "file_name": file_name, "site": site, "exception": str(e), "extra": req}