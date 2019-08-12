from django.shortcuts import render, redirect
#for form upload
from .forms import ContactForm
#from django.views.generic import CreateView
from .models import Contact, Answer
# Create your views here.

#creating contact view using function based views

def contact(request):

    next = request.GET.get('next')
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact = form.save(commit=False)
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        contact.save()
        form = ContactForm()

        if next:
            return redirect(next)
        return redirect('home:index')
    return render(request, 'contact/contact.html', {'form':form})

    #creating a view for answers from contacts
def answer(request):
    context = {
        'answers': Answer.objects.all()
    }
    return render(request, 'contact/answer.html', context)