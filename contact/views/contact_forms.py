from django.shortcuts import render
from contact.forms import ContactForm

def create(request):
        if request.method == 'POST':
            print('POST')
            print(request.method)
            print(request.POST.get('first_name'))
            print(request.POST.get('last_name'))
            print()
            context = {
                'form': ContactForm(request.POST)
        }

context = {}
return render(
            request,
            'contact/create.html',
            context
        )

context = {
        'form': ContactForm()
}

print()
print(request.method)
print()

return render(
request,
'contact/create.html',
context
)