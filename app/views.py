from django.shortcuts import render

# Create your views here.
def first_jinja(request):
    d={'name':'sai'}
    return render(request,'first_jinja.html',context=d)

