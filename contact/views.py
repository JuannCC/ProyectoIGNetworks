from http.client import HTTPResponse
from django.shortcuts import render, redirect

#from Django.agenda import contact
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import render_to_string

# Create your views here.
def index(request, letter= 'NULL'):
    if letter != 'NULL':
        contacts= Contact.objects.filter(name__istartswith=letter)
    else:
        contacts= Contact.objects.filter(name__contains= request.GET.get('search',''))
    
    #contacts= Contact.objects.all()
    context={
        'contacts':contacts
    }
    return render(request,'contact/index.html',context)

def view(request,id):
    contact= Contact.objects.get(id=id)
    context= {
        'contact':contact
    }
    return render(request,'contact/detail.html', context)

def edit(request,id):
    contact= Contact.objects.get(id=id)

    if(request.method == 'GET'):
        form= ContactForm(instance= contact)
        context={
            'form':form,
            'id':id
        }
        return render(request, 'contact/edit.html', context)
    
    if(request.method == 'POST'):
        form= ContactForm(request.POST, instance= contact)
        if form.is_valid():
            form.save()
        context={
            'form':form,
            'id':id
        }
        messages.success(request, 'Contacto actualizado')
        return render(request, 'contact/edit.html', context)

def create(request):
    if request.method == 'GET':
        form= ContactForm()
        context= {
            'form':form
        }
        return render(request, 'contact/create.html', context)
    
    if request.method == 'POST':
        form= ContactForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('contact')

def delete(request,id):
    contact=Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact')

import requests
def status_qb(request,circuito):
    servicios= Contact.objects.all()
    #---------Ubicacion--------------
    headers = {
        'QB-Realm-Hostname': 'ignetworks.quickbase.com',
        'User-Agent': '{User-Agent}',
        'Authorization': 'QB-USER-TOKEN b2hjmh_w4i_b2ytd7mdi8jjrpdg8khp8cmwkm6n'
    }
    body = {"from":"bfwgbisz4","select":[25],"where":"{7.CT." + f"'{circuito}'"+"}"}

    print(body)
    # Hacemos una petición para obtener el contenido de la página web
    r = requests.post(
    'https://api.quickbase.com/v1/records/query',
    headers = headers,
    json = body
    )

    resultado = r.json()
    print(resultado)
    status = resultado['data'][0]['25']['value']
    #---------BW--------------

    body1 = {"from":"bfwgbisz4","select":[16],"where":"{7.CT." + f"'{circuito}'"+"}"}
    print(body1)
    r = requests.post(
    'https://api.quickbase.com/v1/records/query',
    headers = headers,
    json = body1
    )
    #print(json.dumps(r.json(),indent=4))
    resultado = r.json()
    print(resultado)
    statusBW = resultado['data'][0]['16']['value']
    
    #CLIENTE CLAVE
    palabras = circuito.split(".")
    print(palabras[0])
    parseo = str(palabras[0])

    if parseo == "VZB" or parseo == "TSY" or parseo == "TTA" or parseo == "TLS" or parseo == "TWS" or parseo == "VTL" or parseo == "BRT" or parseo == "EVO" or parseo == "RNG" or parseo == "GTT" or parseo == "EMB":
        clave="Este cliente ES CLAVE"
    else:
        clave="Este cliente ''NO'' ES CLAVE"
    #------------------------------------------------#

    if(request.method == 'GET'):
        contacts= Contact.objects.filter(name__contains= request.GET.get('search',''))
        context={
            "circuito":circuito,
            "status":status, 
            "statusBW":statusBW,
            "clave":clave,
            "servicios":servicios,
            'contacts':contacts,
        }
        return render(request, 'contact/status.html', context)

    