from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report

# Create your views here.
def home(request):
    report = report.objects.all()
    context={"reports":reports}
    return render(request, 'WasteTracker/home.html', context)

def createReport(request):
    form = ReportForm() # get an instance of the Ocean form
    if request.method == 'POST':
        form = ReportForm(request.POST) # get what the user has input
        if form.is_valid():  #validate the form to ascetain the input have been dne well
            form.save()
            return redirect('read-reports') 
        else:
            print("kejljwejlwjlkwje=====")
    context = {'form':form}
    return render(request, 'waterbodyApp/form.html', context)


def readReport(request):
    report = Report.objects.all()
    context = {"reports": reports}
    return render(request, 'waterbodyApp/oceans.html', context)

def readReport(request,pk):
    report = Report.objects.get(id=pk)
    context = {"reports": reports}
    return render(request, 'waterbodyApp/ocean.html', context)

def updateReport(request,pk):
    report = Report.objects.get(id=pk)
    form = ReportForm(instance = report)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance= report)
        if form.is_valid():
            report.save()
            return redirect('read-reports')
    context = { "form":form}
    return render(request,'waterbodyApp/form.html', context)

def deleteReport(request, pk):
    report = Report.objects.get(id=pk)
    report.delete()  
    return redirect('read-reports')

def maps(request):
    context={}
    return render(request, 'WasteTracker/maps.html', context)

def report(request):
    context={}
    return render(request, 'WasteTracker/report.html', context)

def eventsAndActivities(request):
    context={}
    return render(request, 'WasteTracker/eventsAndActivities.html', context)