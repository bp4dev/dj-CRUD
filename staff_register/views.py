from django.shortcuts import render

#read R
def staff_list(request):
    return render(request,"staff_register/staff_list.html")

#get post requests => insert update  CRU
def staff_form(request):
    return render(request,"staff_register/staff_form.html")

#delete D
def staff_delete(request):
    return