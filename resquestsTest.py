#encoding: utf-8

import requests
import json
url= 'http://127.0.0.1:8000/api/get_event_list/'
r = requests.post(url, data={'eid':11})
result = r.content

print json.dumps(json.loads(result), ensure_ascii=False)