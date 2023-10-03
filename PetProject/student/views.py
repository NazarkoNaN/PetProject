from django.shortcuts import render
from .forms import *

def index(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        data = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": '('+phone[0]+phone[1]+phone[2]+') '+phone[3]+phone[4]+phone[5]+'-'+phone[6]+phone[7]+phone[8]+phone[9]
        }
        return render(request,'student/index.html', data)
    else:
        studentform = StudentForm()
        return render(request,'student/index.html',{"form": studentform})