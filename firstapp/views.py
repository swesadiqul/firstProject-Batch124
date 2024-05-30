from django.shortcuts import render, redirect
from firstapp.forms import ContactForm
from django.contrib import messages
from firstapp.models import Contact
from django.db.models import Q


# Create your views here.
def index(request):
    name = 'Hi!'
    return render(request, 'index.html', {'name': name})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for contacting with us.')
            return redirect('/')
        else:
            messages.error(request, 'Invalid data.')
            return redirect('contact')
        
    form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


def contact_delete(request, pk=None):
    contacts = Contact.objects.get(pk=pk)
    contacts.delete()
    messages.warning(request, "Contact successfully deleted!.")
    return redirect('contact_list')


def contact_edit(request, pk=None):
    contact = Contact.objects.get(pk=pk)
    if request.method == "POST":
        form = ContactForm(instance=contact, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')

        else:
            print('Form is invalid.')

    form = ContactForm(instance=contact)
    
    return render(request, 'contact.html', {'form': form})


def contact_view(request, pk=None):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'contact_view.html', {'contact': contact})


def contact_search(request):
    if request.method == 'GET':
        query = request.GET.get('q', None)

        contacts = Contact.objects.filter(
            Q(name__icontains=query) | 
            Q(email__icontains=query) | 
            Q(phone__icontains=query) | 
            Q(subject__icontains=query) | 
            Q(message__icontains=query)
        )
    return render(request, 'contact_search.html', {'contacts': contacts})


def contact_filter(request):
    q = request.GET.get('q')

    contacts = Contact.objects.filter(name__startswith=q)
    return render(request, 'contact_search.html', {'contacts': contacts})