from django.shortcuts import render

# Create your views here.

def filters(request):
    import datetime
    dt=datetime.datetime.now()

    d={'data':'Banglore is a green CITy','dt':dt,'c':1 }
    return render(request,'filters.html',d)


def myfilters(request):
    d={'data':'My Name IS Allu STEEve fROm Ap' }
    return render(request,'myfilters.html',d)