from django.shortcuts import render
from .models import MyModel

def page1(request):
    # You can query the database here if needed
    my_objects = MyModel.objects.all()
    return render(request, 'page1.html', {'my_objects': my_objects})

def page2(request):
    return render(request, 'page2.html')