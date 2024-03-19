import os
import random
import time
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.db.models.expressions import RawSQL
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from App.models import *
import os

BASE_DIR = r"C:\Fermier\FermierApp\App\static\\"

# ----------------------------------------Common--------------------------------------------------#




def login(request):
    return render(request, 'login_index.html')


def login_post(request):
    username = request.POST['username']
    password = request.POST['password']
    obj = Login.objects.filter(username=username, password=password)
    if obj.exists():
        obj = obj[0]
        request.session['lid'] = obj.id
        if obj.usertype == 'admin':
            request.session['usertype'] = 'admin'
            return redirect('/admin_home')
        elif obj.usertype == 'officer':
            request.session['usertype'] = 'officer'
            return redirect('/officer_home')
        elif obj.usertype == 'techwing':
            request.session['usertype'] = 'techwing'
            return redirect('/tech_wing_home')
        else:
            return HttpResponse("Something Wrong")
    else:
        return HttpResponse("<script>alert('Username or password is incorrect, Try again');location='/'</script>")


def logout(request):
    request.session.clear()
    return redirect('/#login')


# ----------------------------------------Admin--------------------------------------------------#


def admin_home(request):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    return render(request, 'admin/admin_home.html')


def admin_add_officer(request):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    return render(request, 'admin/add_agg_off.html')


def admin_add_officer_post(request):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    if Login.objects.filter(username=email).exists():
        return HttpResponse(
            "<script>alert('This Email/Username is already used! Try other'); location='/admin_add_officer'</script>")
    obj1 = Login()
    obj1.username = email
    obj1.password = random.randint(10000000, 99999999)
    obj1.usertype = 'officer'
    obj1.save()

    obj = AgrOff()
    obj.name = name
    obj.email = email
    obj.phone = phone
    obj.latitude = latitude
    obj.longitude = longitude
    obj.LOGIN = obj1
    obj.save()
    return HttpResponse("<script>alert('Successfully Added');location='/admin_view_officer'</script>")


def admin_view_officer(request):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = AgrOff.objects.all()
    return render(request, 'admin/view_agg_off.html', {"data": obj})


def admin_edit_officer(request, officerid):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = AgrOff.objects.get(id=officerid)
    return render(request, 'admin/edit_agg_off.html', {"data": obj})


def admin_edit_officer_post(request, officerid):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    name = request.POST['name']
    phone = request.POST['phone']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    AgrOff.objects.filter(id=officerid).update(name=name, phone=phone, latitude=latitude, longitude=longitude)
    return HttpResponse("<script>alert('Successfully Updated');location='/admin_view_officer'</script>")


def adin_delete_officer(request, officerid):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    AgrOff.objects.filter(id=officerid).delete()
    return HttpResponse("<script>alert('Successfully Deleted');location='/admin_view_officer'</script>")


def admin_add_notification(request):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    return render(request, 'admin/add_notification.html')


def admin_add_notification_post(request):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    notification = request.POST['notification']
    obj = Notification()
    obj.notification = notification
    obj.date = datetime.now().strftime("%d-%m-%Y")
    obj.time = datetime.now().strftime("%H:%M")
    try:
        file = request.FILES['file']
        filename = datetime.now().strftime("%d%m%y%H%M%S") + ".pdf"
        FileSystemStorage().save(BASE_DIR+"notification files//" + filename, file)
        path = '/static/notification files/' + filename
        obj.filename = path
        obj.save()
    except:
        obj.save()
    return HttpResponse("<script>alert('Successfully Added');location='/admin_view_notification'</script>")


def admin_view_notification(request):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = Notification.objects.all()
    return render(request, 'admin/view_notification.html', {"data": obj})


def admin_delete_notification(request, notificationid):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    Notification.objects.filter(id=notificationid).delete()
    return HttpResponse("<script>alert('Successfully Deleted');location='/admin_view_notification'</script>")


def admin_view_feedback(request):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = Feedback.objects.all()
    return render(request, 'admin/view_feedback.html', {"data": obj})


def admin_add_crop_fert_perc(request):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    return render(request, 'admin/add_cfp.html')


def admin_add_crop_fert_perc_post(request):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    name = request.POST['name']
    description = request.POST['description']
    typee = request.POST['type']
    rate = request.POST['rate']
    file = request.FILES['file']
    filename = datetime.now().strftime("%d%M%Y%H%M%S") + ".jpg"
    FileSystemStorage().save(BASE_DIR+"cfp image//" + filename, file)
    path = '/static/cfp image/' + filename
    obj = Cfp()
    obj.name = name
    obj.description = description
    obj.type = typee
    obj.price = rate
    obj.photo = path
    obj.save()
    return HttpResponse("<script>alert('Successfully Added');location='/admin_view_crop_fert_perc'</script>")


def admin_view_crop_fert_perc(request):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = Cfp.objects.all()
    return render(request, 'admin/view_cfp.html', {"data": obj})


def admin_edit_crop_fert_perc(request, cfpid):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = Cfp.objects.get(id=cfpid)
    return render(request, 'admin/edit_cfp.html', {"data": obj})


def admin_edit_crop_fert_perc_post(request, cfpid):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    name = request.POST['name']
    description = request.POST['description']
    typee = request.POST['type']
    rate = request.POST['rate']
    try:
        file = request.FILES['file']
        filename = datetime.now().strftime("%d%M%Y%H%M%S") + ".jpg"
        FileSystemStorage().save(r"C:\Fermier\FermierApp\App\static\cfp image//" + filename, file)
        path = 'static/cfp image/' + filename
        Cfp.objects.filter(id=cfpid).update(name=name, description=description, type=typee, price=rate, photo=path)
    except:
        Cfp.objects.filter(id=cfpid).update(name=name, description=description, type=typee, price=rate)

    return HttpResponse("<script>alert('Successfully Updated');location='/admin_view_crop_fert_perc'</script>")


def admin_delete_crop_fert_perc(request, cfpid):
    if 'lid' not in request.session and request.session['usertype'] != 'admin':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    Cfp.objects.filter(id=cfpid).delete()
    return HttpResponse("<script>alert('Successfully Deleted');location='/admin_view_crop_fert_perc'</script>")



def list_table_list(request, qry):
    obj = Cfp.objects.filter(type=qry)
    print(qry, "ytygu")
    return render(request, 'admin/ajaxlist.html', {"data": obj, "type": qry})


def admin_view_complaints(request):
    obj = Complaints.objects.all().order_by('-id')

    return render(request, 'admin/view_complaints.html', {"data": obj})


def admin_send_reply(request, id):
    return render(request, 'admin/send_reply.html', {"id": id})


def admin_send_reply_post(request, id):
    reply = request.POST['reply']
    Complaints.objects.filter(id=id).update(reply=reply, reply_date=datetime.now().strftime("%Y-%m-%d"))
    return HttpResponse("<script>alert('replied'); location='/admin_view_complaints#aaa'</script>")


# ----------------------------------------Officer--------------------------------------------------#


def officer_home(request):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    return render(request, 'officer/officer_home.html')


def officer_view_profile(request):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = AgrOff.objects.get(LOGIN=request.session['lid'])
    return render(request, 'officer/viewprofile.html', {"data": obj})


def officer_view_cfp(request):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = Cfp.objects.all()
    arr = []
    for i in obj:
        arr.append({
            "id": i.id,
            "name": i.name,
            "description": i.description,
            "photo": i.photo,
            "type": i.type,
            "price": i.price,
            "stock": Stock.objects.get(CFP=i.id, AGROFF__LOGIN_id=request.session['lid']).count if Stock.objects.filter(
                CFP=i.id, AGROFF__LOGIN_id=request.session['lid']).exists() else 0
        })
    return render(request, 'officer/view_cfp.html', {"data": arr})


def officer_list_table_list(request, qry):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = Cfp.objects.filter(type=qry)
    arr = []
    for i in obj:
        arr.append({
            "id": i.id,
            "name": i.name,
            "description": i.description,
            "photo": i.photo,
            "type": i.type,
            "price": i.price,
            "stock": Stock.objects.get(CFP=i.id).count if Stock.objects.filter(CFP=i.id).exists() else 0
        })
    return render(request, 'officer/ajaxlist.html', {"data": arr, "type": qry})


def officer_update_stock(request, cfpid):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    name = Cfp.objects.get(id=cfpid).name
    stock = Stock.objects.get(CFP=cfpid).count if Stock.objects.filter(CFP=cfpid).exists() else 0
    return render(request, 'officer/update_stock.html', {"item": name, "stock": stock, "id": cfpid})


def officer_update_stock_post(request, cfpid):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    stock = request.POST['stock']
    agrof = AgrOff.objects.get(LOGIN_id=request.session['lid'])
    obj = Stock.objects.filter(CFP=cfpid, AGROFF=agrof)
    if obj.exists():
        obj.update(count=stock, CFP_id=cfpid, AGROFF=agrof)
    else:
        qry = Stock()
        qry.count = stock
        qry.AGROFF = agrof
        qry.CFP_id = cfpid
        qry.save()
    return HttpResponse("<script>alert('Successfully Updated');location='/officer_view_cfp'</script>")


def officer_view_request(request):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = CfpReqMain.objects.filter(AGROFF__LOGIN=request.session['lid'], date=datetime.now().strftime("%Y-%m-%d"))
    return render(request, 'officer/view_req_farmer.html', {"data": obj})


def officer_view_previous(request):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = CfpReqMain.objects.filter(AGROFF__LOGIN=request.session['lid'], date__lt=datetime.now().strftime("%Y-%m-%d"))
    return render(request, 'officer/view_req_previous.html', {"data": obj})


def officer_view_items(request, id):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = CfpReqSub.objects.filter(CFPREQMAIN=id)
    arr = []
    for i in obj:
        arr.append({"item": i.CFP.name,
                    "count": i.count,
                    "total": i.price,
                    "stock": Stock.objects.get(CFP=i.CFP).count if Stock.objects.filter(CFP=i.CFP).exists() else 0})
    return render(request, 'officer/view_items.html', {"data": arr})


def officer_accept_request(request, reqid):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    CfpReqMain.objects.filter(id=reqid).update(status='approved')
    return HttpResponse("<script>alert('Successfully Approved');location='/officer_view_request'</script>")


def officer_reject_request(request, reqid):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    CfpReqMain.objects.filter(id=reqid).update(status='rejected')
    return HttpResponse("<script>alert('Successfully Rejected');location='/officer_view_request'</script>")


def officer_chat_page(request):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = Chat.objects.filter(OFFICER__LOGIN=request.session['lid'])
    arr = []
    for i in obj:
        if i.FARMER.id not in arr:
            arr.append(i.FARMER.id)
    dta = []
    for i in arr:
        qry = Farmer.objects.get(id=i)
        dta.append({"id": qry.id,
                    "name": qry.name})

    return render(request, 'officer/chat_page.html', {"data": dta})


def chatt(request, u):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    request.session['head'] = "CHAT"
    request.session['uid'] = u
    return render(request, 'officer/chat.html', {'u': u})


def chatsnd(request, u):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    d = datetime.now().strftime("%d-%m-%Y")
    t = datetime.now().strftime("%H:%M:%S")
    c = request.session['lid']
    b = request.POST['n']
    m = request.POST['m']
    cc = AgrOff.objects.get(LOGIN__id=c)
    uu = Farmer.objects.get(id=request.session['uid'])
    obj = Chat()
    obj.mdate = d
    obj.mtime = t
    obj.type = 'officer'
    obj.OFFICER = cc
    obj.FARMER = uu
    obj.message = m
    obj.save()
    v = {}
    if int(obj) > 0:
        v["status"] = "ok"
    else:
        v["status"] = "error"
    r = JsonResponse.encode(v)
    return r


# else:
#     return redirect('/')


def chatrply(request):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    c = request.session['lid']
    cc = AgrOff.objects.get(LOGIN__id=c)
    uu = Farmer.objects.get(id=request.session['uid'])
    res = Chat.objects.filter(OFFICER=cc, FARMER=uu)
    v = []
    if len(res) > 0:
        for i in res:
            v.append({
                'type': i.type,
                'chat': i.message,
                'name': i.FARMER.name,
                'dtime': i.mtime,
                'ddate': i.mdate,
                'tname': i.OFFICER.name,
            })
        return JsonResponse({"status": "ok", "data": v, "id": cc.id})
    else:
        return JsonResponse({"status": "error"})


def officer_view_notifications(request):
    if 'lid' not in request.session and request.session['usertype'] != 'officer':
        return HttpResponse("<script>alert('Session Expired, Login Again'); location='/'</script>")
    obj = Notification.objects.all()
    return render(request, 'officer/view_notifications.html', {"data": obj})


def officer_change_password(request):
    return render(request, 'officer/change password.html')


def officer_change_password_post(request):
    cp = request.POST['current']
    np = request.POST['new']
    obj = Login.objects.filter(password=cp, id=request.session['lid'])
    if obj.exists():
        obj.update(password=np)
        return HttpResponse("<script>alert('Successfully Changed');location='/officer_view_request'</script>")
    else:
        return HttpResponse("<script>alert('Passwords are incorrect');location='/officer_view_request'</script>")


# ----------------------------------------Techwing--------------------------------------------------#


# ------------------------------------------------Android-------------------------------------------------


def loginAndroid(request):
    username = request.POST['username']
    password = request.POST['password']
    obj = Login.objects.filter(username=username, password=password, usertype='farmer')
    if obj.exists():
        obj = obj[0]
        data = Farmer.objects.get(LOGIN=obj.id)
        return JsonResponse(
            {"status": "ok", "lid": obj.id, "name": data.name, "email": data.email, "phone": data.phone})
    return JsonResponse({"status": "no"})


def register(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    password = request.POST['password']

    obj = Login()
    obj.username = email
    obj.password = password
    obj.usertype = 'farmer'
    obj.save()

    obj1 = Farmer()
    obj1.name = name
    obj1.latitude = latitude
    obj1.longitude = longitude
    obj1.email = email
    obj1.phone = phone
    obj1.LOGIN = obj
    obj1.save()
    return JsonResponse({"status": "ok"})


def viewcfp(request):
    qry = request.POST['qry']
    obj = Cfp.objects.all()
    if qry != 'all':
        obj = Cfp.objects.filter(type=qry)
    arr = []
    for i in obj:
        arr.append({"name": i.name,
                    "description": i.description,
                    "price": i.price,
                    "type": i.type,
                    "photo": i.photo})
    return JsonResponse({"status": "ok", "data": arr})


def view_agroff(request):
    userid = request.POST['userid']
    obj = Farmer.objects.get(LOGIN=userid)
    latitude = obj.latitude
    longitude = obj.longitude

    gcd_formula = "6371 * acos(least(greatest(cos(radians(%s)) * cos(radians('" + latitude + "')) * cos(radians('" + longitude + "') - radians(%s)) + sin(radians(%s)) * sin(radians('" + latitude + "')), -1), 1))"
    qry = AgrOff.objects.all()
    li = []
    for i in qry:
        qs = AgrOff.objects.filter(id=i.id).annotate(
            distance=RawSQL(gcd_formula, (i.latitude, i.longitude, i.latitude))).order_by('distance')
        li.append({
            "officeid": i.id,
            "name": i.name,
            "email": i.email,
            "phone": i.phone,
            "distance": "%.2f" % qs[0].distance
        })

    def sort_distance(e):
        return e['distance']

    li.sort(key=sort_distance)
    return JsonResponse({"status": "ok", "data": li})


def view_stock(request):
    officerid = request.POST['officerid']
    obj = Stock.objects.filter(AGROFF=officerid)
    arr = []
    for i in obj:
        arr.append({"id": i.CFP.id,
                    "name": i.CFP.name,
                    "stock": i.count,
                    "stockid": i.id})
    return JsonResponse({"status": "ok", "data": arr})


def add_cart(request):
    loginid = request.POST['farmerid']
    stockid = request.POST['stockid']
    quantity = request.POST['count']
    if CfpCart.objects.filter(FARMER__LOGIN=loginid, STOCK=stockid).exists():
        CfpCart.objects.filter(FARMER__LOGIN=loginid, STOCK=stockid).update(count=quantity)
    else:
        obj = CfpCart()
        obj.FARMER = Farmer.objects.get(LOGIN=loginid)
        obj.count = quantity
        obj.STOCK_id = stockid
        obj.save()
    return JsonResponse({"status": "ok"})


def view_cart(request):
    userid = request.POST['userid']
    obj = CfpCart.objects.filter(FARMER__LOGIN=userid)
    arr = []
    for i in obj:
        arr.append({"cfpname": i.STOCK.CFP.name,
                    "quantity": i.count,
                    "id": i.id})
    return JsonResponse({"status": "ok", "data": arr})


def delete_cart(request):
    cartid = request.POST['cartid']
    CfpCart.objects.filter(id=cartid).delete()
    return JsonResponse({"status": "ok"})


def send_request(request):
    userid = request.POST['userid']
    date = datetime.now().strftime("%d-%m-%Y")
    time = datetime.now().strftime("%H:%M")
    for i in CfpCart.objects.filter(FARMER__LOGIN=userid):
        cfpqry = CfpReqMain.objects.filter(FARMER__LOGIN=userid, AGROFF=i.STOCK.AGROFF)
        if cfpqry.filter(status__in=['approved', 'rejected']).exists() or not cfpqry.exists():
            obj = CfpReqMain()
            obj.time = time
            obj.date = date
            obj.status = 'pending'
            obj.FARMER = Farmer.objects.get(LOGIN=userid)
            obj.AGROFF = i.STOCK.AGROFF
            obj.save()
        else:
            cfpqry.filter(status='pending').update(date=date, time=time)
        if CfpReqSub.objects.filter(CFPREQMAIN=cfpqry.filter(status='pending')[0]).exists():
            CfpReqSub.objects.filter(CFPREQMAIN=cfpqry).update(count=i.count, CFP=i.STOCK.CFP,
                                                               price=float(i.STOCK.CFP.price) * float(i.count))
        else:
            qry = CfpReqSub()
            qry.count = i.count
            qry.CFP = i.STOCK.CFP
            qry.price = float(i.STOCK.CFP.price) * float(i.count)
            qry.CFPREQMAIN = obj
            qry.save()
    CfpCart.objects.filter(FARMER__LOGIN=userid).delete()
    return JsonResponse({"status": "ok"})


def view_request_status(request):
    userid = request.POST['userid']
    obj = CfpReqMain.objects.filter(FARMER__LOGIN=userid).order_by('-id')
    arr = []
    for i in obj:
        arr.append({"reqid": i.id,
                    "date": i.date,
                    "time": i.time,
                    "status": i.status,
                    "officer": i.AGROFF.name})
    return JsonResponse({"status": "ok", "data": arr})


def view_items(request):
    reqid = request.POST['reqid']
    obj = CfpReqSub.objects.filter(CFPREQMAIN=reqid).order_by("-id")
    arr = []
    for i in obj:
        arr.append({"name": i.CFP.name,
                    "quantity": i.count,
                    "price": i.price})
    return JsonResponse({"status": "ok", "data": arr})


def view_notification(request):
    obj = Notification.objects.all().order_by('-id')
    arr = []
    for i in obj:
        arr.append({"notification": i.notification,
                    "date": i.date,
                    "time": i.time,
                    "file": i.filename})
    return JsonResponse({"status": "ok", "data": arr})


def add_chat(request):
    lid = request.POST['lid']
    toid = request.POST['toid']
    message = request.POST['message']
    obj = Chat()
    obj.FARMER = Farmer.objects.get(LOGIN=lid)
    obj.OFFICER_id = toid
    obj.mdate = datetime.now().strftime("%d-%m-%Y")
    obj.mtime = datetime.now().strftime("%H:%M")
    obj.message = message
    obj.type = 'farmer'
    obj.save()
    return JsonResponse({"status": "ok"})


def view_chat(request):
    lid = request.POST['lid']
    toid = request.POST['toid']
    lastid = request.POST['lastid']
    obj = Chat.objects.filter(Q(FARMER__LOGIN=lid), Q(OFFICER=toid), Q(id__gt=lastid))
    arr = []
    for i in obj:
        arr.append({"message": i.message,
                    "chat_id": i.id,
                    "date": i.mdate,
                    "time": i.mtime,
                    "type": i.type,
                    "from_id": i.FARMER.LOGIN.id,
                    "name": i.OFFICER.name,
                    })
    return JsonResponse({"status": "ok", "data": arr})


def view_updates(request):
    lid = request.POST['lid']
    Stories.objects.filter(date__lt=datetime.now().strftime("%Y-%m-%d"),
                           time__lt=datetime.now().strftime("%H:%M")).delete()
    obj = Stories.objects.all().exclude(FARMER__LOGIN=lid)
    arr = []
    for i in obj:
        arr.append({"image": i.image,
                    "description": i.description,
                    "date": i.date,
                    "time": i.time})

    return JsonResponse({"status": "ok", "data": arr})


def view_own_updates(request):
    lid = request.POST['lid']
    Stories.objects.filter(date__lt=datetime.now().strftime("%Y-%m-%d"),
                           time__lt=datetime.now().strftime("%H:%M")).delete()
    obj = Stories.objects.filter(FARMER__LOGIN=lid)
    arr = []
    for i in obj:
        arr.append({"image": i.image,
                    "description": i.description,
                    "date": i.date,
                    "time": i.time,
                    "id": i.id})

    return JsonResponse({"status": "ok", "data": arr})


def send_update(request):
    lid = request.POST['lid']
    pic = request.FILES['pic']
    description = request.POST['description']
    filename = datetime.now().strftime("%d%M%Y%H%M%S") + ".jpg"
    FileSystemStorage().save(BASE_DIR+"cfp image//" + filename, pic)
    path = '/static/cfp image/' + filename
    obj = Stories()
    obj.image = path
    obj.description = description
    obj.date = datetime.now().strftime("%Y-%m-%d")
    obj.time = datetime.now().strftime("%H:%M")
    obj.FARMER = Farmer.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({"status": "ok"})


def and_send_feedback(request):
    lid = request.POST['lid']
    feedback = request.POST['feedback']
    obj = Feedback()
    obj.feedback = feedback
    obj.date = datetime.now().strftime("%Y-%m-%d")
    obj.time = datetime.now().strftime("%H:%M")
    obj.FARMER = Farmer.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({"status": "ok"})


def and_send_complaint(request):
    lid = request.POST['lid']
    complaint = request.POST['complaint']

    obj = Complaints()
    obj.complaint = complaint
    obj.FARMER = Farmer.objects.get(LOGIN=lid)
    obj.reply = "pending"
    obj.reply_date = "pending"
    obj.complaint_date = datetime.now().strftime("%Y-%m-%d")
    obj.save()
    return JsonResponse({"status": "ok"})


def and_view_complaints(request):
    lid = request.POST['lid']

    obj = Complaints.objects.filter(FARMER__LOGIN=lid).order_by('-id')
    arr = []
    for i in obj:
        arr.append({"complaint": i.complaint,
                    "cdate": i.complaint_date,
                    "reply": i.reply,
                    "rdate": i.reply_date})
    print(arr)
    return JsonResponse({"status": "ok", "data": arr})


def delete_story(request):
    storyid = request.POST['storyid']

    Stories.objects.filter(id=storyid).delete()
    return JsonResponse({"status": "ok"})

