from django.shortcuts import render, HttpResponse



def login(request):
    return render(request,"login.html")


def register(request):
    return render(request,"registration.html")

def customers_table(request):
  return render (request,"customers_table.html")

