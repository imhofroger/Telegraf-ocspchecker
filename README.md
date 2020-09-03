# Telegraf-ocspchecker

## Needed Python Library

https://pypi.org/project/ocsp-checker/
pip install ocsp-checker

## Python Script
```
from ocspchecker import ocspchecker
import time

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
    
print(ocsp_stat("google.com"))
```

To add more URLs to Check add aditional Line like
```print(ocsp_stat("url.url"))```

Responsecode 1 = OK
Responsecode 2 = NOK

### Script Output
```OCSP_Check,URI="google.com" resolution=1,response_time=0.2316288948059082,raw="['Host: google.com:443', 'OCSP URL: http://ocsp.pki.goog/gts1o1core', 'OCSP Status: GOOD']"```


## Telegraf Inputs
Docu: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/exec
[[inputs.exec]]
  commands = [
    'python3 ocsp.py',
  ]
 data_format = "influx"
