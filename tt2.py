# encoding: utf-8
import requests
# def add_event():
#     data = {"eid":13,
#               "name":"msi发布会",
#               "limit":100,
#               "status":0,
#               "address":"GUANGZHOU",
#               "start_time":"2011-03-03 11:00:00"}
#     r = requests.post("http://127.0.0.1:8000/api/add_event/", data=data)
#     print r.json()
# add_event()

# def sss():
#      data = {"eid":11}
#      r = requests.post("http://127.0.0.1:8000/api/sss/", data=data)
#      print r.json()
# sss()


# def get_event_list():
#     data = {"name":'all'}
#     r = requests.post("http://127.0.0.1:8000/api/get_event_list/", data=data)
#     print r.json()
# get_event_list()

def get_guest_list():
    data = {'eid': 11, 'phone': 18800001005}
    r = requests.post("http://127.0.0.1:8000/api/get_guest_list/", data=data)
    print r.json()


    # assert res['status'] == 200
get_guest_list()
