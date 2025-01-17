import requests
import random
import os

from .site_data import Site_Data_CLSS, sites_data_dict
from .pretty_print import *

site = "Oshi"

class Oshi:
    
    def Uploader(file, proxy_list, user_agents):
        try:
            ua = random.choice(user_agents)
            upload_url = sites_data_dict[site]["url"]
            size_limit = f'{sites_data_dict[site]["size_limit"]} {sites_data_dict[site]["size_unit"]}'
            
            
            # Get file name
            file_size = os.stat(file).st_size
            file_name = os.path.basename(file)
            file_name = (file_name[:240] + '..') if len(file_name) > 240 else file_name # Changed from 255 to 240 as an additional safety net.
            
            calc_size = Site_Data_CLSS.size_unit_calc(site, file_size)
            
            headers = {"User-Agent": ua}
            proxies = random.choice(proxy_list) if proxy_list else None

            if calc_size == "OK":

                files_data = {'file': (os.path.basename(file), open(str(file), 'rb'), 'multipart/form-data')}
                req = requests.post(url=upload_url, files=files_data, headers=headers, proxies=proxies)
            
                if req.status_code == 200:
                    file_url = req.content.decode("utf-8").rsplit("\nDL: ")
                    file_url = file_url[-1].replace("\n", "")
                    return {"status": "ok", "file_name": file_name, "file_url": file_url, "site": site}
                else:
                    raise Exception(f"Upload Failed: {req.content.decode('utf-8')}")
            else:
                return {"status": "size_error", "file_name": file_name, "site": site, "exception": "SIZE_ERROR", "size_limit": f"{str(size_limit)}"}
                
        except Exception as e:
            return {"status": "error", "file_name": file_name, "site": site, "exception": str(e), "extra": req}