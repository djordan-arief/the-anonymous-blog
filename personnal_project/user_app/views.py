from django.shortcuts import redirect, render
from user_app.models import Profile
from .forms import ContactForm
from django.core.mail import send_mail
from personnal_project import settings


def profilepage(request):
    profile = Profile.objects.all()
    return render(request, 'user_app/profile.html', {'profile': profile})
    

def contactpage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = f'From: {email}\n\n {form.cleaned_data["message"]}'
            print(subject)
            print(message)
            send_mail(
                subject, 
                message,
                from_email= email, 
                recipient_list= ['djordan.rief@gmail.com'], 
                fail_silently=False)
            return redirect('contact-page')

    else: 
        form = ContactForm()
    return render(request, 'user_app/contact.html', {'form': form})

