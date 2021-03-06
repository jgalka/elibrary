from django.shortcuts import render

from django.views.generic import FormView, DetailView

from .models import Message
from .forms import MessageForm, ContactForm

# Create your views here.

#class MessageDetailView(DetailView):
#    model = Message

class MessageAddView(FormView):
    form_class = MessageForm
    template_name = 'contact/message_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save() #bo form jest instancją ModelForm która posiada metodę save
        return super(MessageAddView, self).form_valid(form)


# Create your views here.
