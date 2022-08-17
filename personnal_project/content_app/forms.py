from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=200)
    message = forms.CharField(widget=forms.Textarea, max_length=1500)

    def __str__(self):
        return self.email