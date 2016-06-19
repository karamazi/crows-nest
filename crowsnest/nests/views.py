from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("""<html>
    <head>
    <title>Armada Crow's Nest</title>
    </head>
    </html>""")

