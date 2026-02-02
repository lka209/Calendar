from django.shortcuts import render

def contact(request, contact_id):
    return render(request, 'contact/contact.html', {
        'contact_id': contact_id
    })

def create(request):
    return render(request, 'contact/create.html')

def update(request, contact_id):
    return render(request, 'contact/update.html', {
        'contact_id': contact_id
    })