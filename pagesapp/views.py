from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render (request,'pagesapp/home.html')

def contact_view(request):
    return render (request,'pagesapp/contact.html')

def about_view(request):
    return render (request,'pagesapp/about.html')