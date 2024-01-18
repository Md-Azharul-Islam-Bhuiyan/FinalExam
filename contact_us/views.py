from django.shortcuts import render, redirect
from .models import ContactUs
from django.views.generic import CreateView
from .forms import ContactUsForm
from django.contrib import messages
class ContactUsView(CreateView):
    model = ContactUs
    template_name = 'contact_us/contact_us.html'
    form_class = ContactUsForm
    def get(self, request, *args, **kwargs):
        form = ContactUsForm()
        print("get er modde", form)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        
        form = ContactUsForm(request.POST)
        print("post er bitor")
        if form.is_valid():
            form.save()
            messages.success(request, "Message Successfully Sent")  
            return redirect('home')
        return render(request, self.template_name, {'form': form})
