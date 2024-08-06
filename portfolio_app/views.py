from django.shortcuts import render
from .models import Project
from .forms import ContactForm

# Create your views here.
def home(request):
    projects = Project.objects.all()
    form = ContactForm()

    context = {
        'projects':projects,
       
        'form':form
    }
    return render(request, 'portfolio_app/index.html', context)



