from django.shortcuts import render

# Create your views here.

def categories(request) : 
    add_category = {
        'category' : categories.objects.all()
    }
    return render(request,'categories/base.html', add_category )

