from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render

<<<<<<< HEAD
from lists.forms import ExistingListItemForm, ItemForm
=======
from lists.forms import ItemForm, ExistingListItemForm
>>>>>>> a2df7a7025ef75a243b6a6a33d46ce41ff8160b5
from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
<<<<<<< HEAD
            #form.save(for_list=list_)
            form.save()
=======
            form.save()
            #form.save(for_list=list_)
>>>>>>> a2df7a7025ef75a243b6a6a33d46ce41ff8160b5
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})        

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})
