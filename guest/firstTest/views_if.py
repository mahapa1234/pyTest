#encoding: utf-8

from django.http import JsonResponse
from firstTest.models import Event, Guest
from django.core.exceptions import ValidationError, ObjectDoesNotExist

def add_event(request):
    eid = request.POST.get('eid', '')
    name = request.POST.get('name', '')
    limit = request.POST.get('limit', '')
    status = request.POST.get('status', '')
    address = request.POST.get('address', '')
    start_time = request.POST.get('start_time', '')

    if eid=='' or name=='' or limit=='' or start_time=='' or status=='' or address=='' :
        return JsonResponse({'status':10021,'message':'parameter error'})
    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status':10022,'message':'event id already exists'})
    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status':10023,'message':'event name already exists'})
    if status == '':
        status = 1
    try:
        Event.objects.create(id=eid, name=name, limit=limit, status=int(status), address=address, start_time=start_time)
    except ValidationError as e:
        error = 'start_time format error. It must bu in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status':10024, 'message':error})
    return JsonResponse({'status':200, 'message':'add event success'})

def sss(request):
    return JsonResponse({'status':200, 'message':'add event success'})

def get_event_list(request):
    eid = request.POST.get("eid", '')
    name = request.POST.get("name", '')

    if eid == '' and name == '':
        return JsonResponse({'status':10021, 'message':'paramer error'})

    if eid != '':
        event = {}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022, 'message':'query result is empty'})
        else:
            event['name'] = result.name
            event['limit'] = result.limit
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            return JsonResponse({'status':200, 'message':'success', 'data':event})

    if name != '':
        datas = []
        if name == 'all':
            results = Event.objects.all()
        else:
            results = Event.objects.filter(name__contains=name)
        if results:
            for result in results:
                event = {}
                event['name'] = result.name
                event['limit'] = result.limit
                event['status'] = result.status
                event['address'] = result.address
                event['start_time'] = result.start_time
                datas.append(event)
            return JsonResponse({'status':200, 'message':'success', 'data':datas})
        else:
            return JsonResponse({'status':10022, 'message':'query result is empty'})

def get_guest_list(request):
    eid = request.POST.get('eid', '')
    phone = request.POST.get('phone', '')

    if eid == '':
        return JsonResponse({'status':10021, 'message':'eid cannot be empty'})

    if eid !='' and phone == '':
        datas = []
        results = Guest.objects.filter(event_id=eid)
        if results:
            for r in results:
                guest={}
                guest['realname'] = r.realname
                guest['phone'] = r.phone
                guest['email'] = r.email
                guest['sign'] = r.sign
                datas.append(guest)
            return JsonResponse({'status':200, 'message':'success', 'data':datas})
        else:
            return JsonResponse({'status':10022, 'message':'query result is empty'})

    if eid != '' and phone != '':
        guest = {}
        try:
            result = Guest.objects.get(phone=phone, event_id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'sutaut':10022, 'message':'query result is empty'})
        else:
            guest['realname'] = result.realname
            guest['phone'] = result.phone
            guest['email'] = result.email
            guest['sign'] = result.sign
            return JsonResponse({'status':200, 'message':'success', 'data':guest})
