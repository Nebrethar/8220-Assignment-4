from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm
from assign4.forms import SignUpFormPE, SignUpFormHM, DocumentForm
from django.urls import reverse
from datetime import datetime
from django.conf import settings
import os
import io

def signupPE(request):
    if request.method == 'POST':
        form = SignUpFormPE(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.groups.add(Group.objects.get(name='PotentialEmployee'))
            login(request, user)
            return redirect('index')
    else:
        form = SignUpFormPE()

    return render(request, "signupPE.html", {'form': form})

def signupHM(request):
    if request.method == 'POST':
        form = SignUpFormHM(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.groups.add(Group.objects.get(name='HiringManager'))
            login(request, user)
            return redirect('index')
    else:
        form = SignUpFormHM()

    return render(request, "signupHM.html", {'form': form})

def index(request):
    return render(request, 'index.html')

def roleSU(request):
    return render(request, 'roleSU.html')

def roleLI(request):
    return render(request, 'roleLI.html')
    
def loginform(request):
    return render(request, 'loginform.html')

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        username = form.data.get('username')
        raw_password = form.data.get('password')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        if user.groups.filter(name='PotentialEmployee').exists():
            return redirect('homepagePE')
        if user.groups.filter(name='HiringManager').exists():
            return redirect('homepageHM')
        else:
            return redirect('admin/')
    else:
        form = AuthenticationForm()
    return render(request, 'loginform.html', {'form': form})

def homepageHM(request):
    user = request.user
    print(User.objects)
    PE = User.objects.filter(groups__name='PotentialEmployee')
    print(PE)
    return render(request, 'homeHM.html', {'PE': PE, 'user': user})

def homepagePE(request):
    user = request.user
    print(User.objects)
    HM = User.objects.filter(groups__name='HiringManager')
    print(HM)
    return render(request, 'homePE.html', {'HM': HM, 'user': user})

"""
def homePE(request):
    user = request.user
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        print("FILE UPLOADED: " + str(myfile))
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print("URL IS AT: \n" + uploaded_file_url)
    return render(request, 'homePE.html', {'user': user})


def list(request):
    user = request.user
    print("USER: " + user.username)
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print("**********")
            print(Resume)
            print(request.FILES['docfile'])
            newdoc = Resume(docfile = request.FILES['docfile'])
            print(vars(newdoc))
            newdoc.save()
            print(vars(newdoc))
            print("**********")
            os.rename(str(settings.MEDIA_ROOT) + "/" + str(newdoc.docfile), user.username + "|" + str(datetime.now()).replace(" ", "|") + ".pdf")
            # Redirect to the document list after POST
    else:
        form = DocumentForm() # A empty, 


    # Load documents for the list page
    RS = Resume.objects.all()
    CVS = CV.objects.all()


    # Render list page with the documents and the form
    return render(request, 'homePE.html',{'user': user, 'RS': RS, 'CVS': CVS, 'form': form})

"""