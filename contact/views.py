from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
# Create your views here.

def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message'] + ' email: ' + form.cleaned_data['from_email']
            try:
                send_mail(subject, message, from_email, ['awlodarczyk.work@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect(reverse('contact:success-view'))
    return render(request, "contact/contact_view.html", {'form': form})


def success_view(request):
    return render(request, "contact/success_view.html", {})