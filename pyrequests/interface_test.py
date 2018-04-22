# encoding: utf-8


import requests
# import unittest
url = 'http://127.0.0.1:8000/api/get_event_list/'
r = requests.post(url, data={'eid': 11})
result = r.json()
assert result['status'] == 200
assert result['message'] == 'success'
assert result['data']['name'] == '苹果mac发布会'.decode('utf-8')
print type(result['data']['name'])
print r.url
