from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Author

# Create your views here.

class AuthorListView(ListView):
	model = Author
		
class AuthorDetailView(DetailView):
	model = Author