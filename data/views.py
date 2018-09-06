from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the data index.")

def insert_data(request):
    return HttpResponse("You are at the data insertion page.")

def select_data(request):
    return HttpResponse("You are at the data selection page.")
