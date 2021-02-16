from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'quiz.html')

def submit(request):
    a1= request.GET['1'];
    a2= request.GET['2'];
    a3= request.GET['3'];
    a4= request.GET['4'];
    a5= request.GET['5'];
    a6= request.GET['6'];
    a7= request.GET['7'];
    a8= request.GET['8'];
    a9= request.GET['9'];
    a10= request.GET['10'];
    points=0;
    if a1.upper()=='AEGON TARGARYEN':
        points=points+10;
    if a2.upper()=='RHAELLA TARGARYEN':
        points=points+10;
    if a3.upper()=='RHAEGAR TARGARYEN':
        points=points+10;
    if a4.upper()=='13':
        points=points+10;
    if a5.upper()=='DRAGONGLASS':
        points=points+10;
    if a6.upper()=='GHOST':
        points=points+10;
    if a7.upper()=='OBERYN MARTELL':
        points=points+10;
    if a8.upper()=='ROBERT BARATHEON':
        points=points+10;
    if a9.upper()=='HOUSE TULLY':
        points=points+10;
    if a10.upper()=='PETER DINKLAGE':
        points=points+10;
    return render(request, 'result.html',{'points':points})