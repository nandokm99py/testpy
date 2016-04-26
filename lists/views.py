from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.

#home_page = None

def home_page(request):

    return render(request, 'home.html')

    #if request.method == 'POST':
        #new_item_text = request.POST['item_text']
    #    Item.objects.create(text=request.POST['item_text'])
    #    return redirect('/lists/the-only-list-in-the-world/')

    #items = Item.objects.all()

    #return render(request, 'home.html', {'items':items})

    #return HttpResponse('<html><title>To-Do lists</title></html>')
    #pass

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items':items})

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])    
    return redirect('/lists/the-only-list-in-the-world/')
