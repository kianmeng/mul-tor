import requests
import os
import random
import string
import re

from .site_data import Site_Data_CLSS, sites_data_dict
from .pretty_print import *
from main import DEBUG

site = "YourFileStore"

class YourFileStore:
    
    def Uploader(file, proxy_list, user_agents):
        req = "which one of you maggots ate the fucking request huh?"
        try:
            ua = random.choice(user_agents)
            upload_url = sites_data_dict[site]["url"]
            size_limit = f'{sites_data_dict[site]["size_limit"]} {sites_data_dict[site]["size_unit"]}'
            
            
            file_size = os.stat(file).st_size
            file_name = os.path.basename(file)
            file_name = (file_name[:240] + '..') if len(file_name) > 240 else file_name # Changed from 255 to 240 as an additional safety net.

            calc_size = Site_Data_CLSS.size_unit_calc(site, file_size)
            
            headers = {"User-Agent": ua}
            proxies = random.choice(proxy_list) if proxy_list else None

            if calc_size == "OK":

                characters = string.ascii_lowercase + string.digits + string.ascii_uppercase
                random_string = ''.join(random.choice(characters) for i in range(32))

                # This site has problems with certain characters in file names
                safe_file_name = os.path.basename(file).replace("(", ""). replace(")", "").replace("[", "").replace("]", "")

                form_data = {
                    'UPLOAD_IDENTIFIER': random_string,
                    'userfile': (safe_file_name, open(str(file), 'rb'), 'application/octet-stream')
                }
                
                raw_req = requests.post(url=upload_url, files=form_data, headers=headers, proxies=proxies)

                url_pattern = r'https://yourfilestore\.com/download/\d+/[^"]+'

                match = re.search(url_pattern, raw_req.text)
                download_url = match.group()

                return {"status": "ok", "file_name": file_name, "file_url": download_url, "site": site}
            else:
                return {"status": "size_error", "file_name": file_name, "site": site, "exception": "SIZE_ERROR", "size_limit": f"{str(size_limit)}"}
                
        except Exception as e:
            return {"status": "error", "file_name": file_name, "site": site, "exception": str(e), "extra": raw_req.content}