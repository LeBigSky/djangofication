from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')
def base(request):
    return render(request, 'app/base.html')
def about(request):
    return render(request, 'app/about.html')
def book(request):
    return render(request, 'app/book.html')
def menu(request):
    return render(request, 'app/menu.html')
def special(request):
    return render(request, 'app/specials.html')
def gallery(request):
    return render(request, 'app/gallery.html')
def event(request):
    return render(request, 'app/events.html')
def chef(request):
    return render(request, 'app/chefs.html')
def contact(request):
    return render(request, 'app/contact.html')
def chef1(request):
    return render(request, 'app/chef1.html')
def chef2(request):
    return render(request, 'app/chef2.html')
def chef3(request):
    return render(request, 'app/chef3.html')
