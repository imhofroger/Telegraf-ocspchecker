from ocspchecker import ocspchecker
import time
import json

def ocsp_stat(uri):
    start_time = time.time()
    ocsp_request = ocspchecker.get_ocsp_status(uri)
    end_time = time.time()

    responsetime = float(end_time-start_time)
    
    if len(ocsp_request) == 3:
        if ocsp_request[2].split()[2] == "GOOD":
            data = f'OCSP_Check,URI="{uri}" resolution=1,response_time={responsetime},raw="{ocsp_request}"'
    else:
        data = f'OCSP_Check,URI="{uri}" resolution=2,response_time={responsetime},raw="{ocsp_request}"' 
    return data


print(ocsp_stat("google.ch"))
print(ocsp_stat("postfinance.ch"))
#print(ocsp_stat("judihio.ch"))
