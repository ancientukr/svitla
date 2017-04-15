from django.shortcuts import render
from mongoengine import DoesNotExist

from main.models import Album, Foto, SliderPhoto
from  main.forms import RecallForm
from django.http import HttpResponse

context_dict = {}
foto_dict = {}
slider_context = {}
album_id = 0

def index(request):
    slide_list = SliderPhoto.objects.filter()
    slider_context["slides"] = slide_list
    return render(request, 'main/index.html', slider_context)

def info(request):
    return render(request,'main/info.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def faq(request):
    return render(request, 'main/faq.html')

def price(request):
    return render(request, 'main/price.html')

def categories(request, type_foto):
    album_list = Album.objects.filter(categories=type_foto)
    context_dict['album'] = album_list
    context_dict['title'] = album_list[0].categories
    return render(request, 'main/categories.html', context_dict)

def albums(request, album_id):
    album = Album.objects.get(id=album_id)
    foto_dict['photos'] = Foto.objects.filter(album= album)
    foto_dict['album_info'] = album

    try:
        foto_dict['next'] = Album.objects.get(id=album_id).get_next_by_data().id
    except Exception:
        foto_dict['next']= 0

    try:
        foto_dict['previous'] = Album.objects.get(id=album_id).get_previous_by_data().id
    except Exception:
        foto_dict['previous'] = 0

    return render(request, 'main/albums.html', foto_dict)

def add_recall(request):
    if request.method == 'POST':
        form = RecallForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('ok')
        else:
            return HttpResponse('not ok')
    else:
        form = RecallForm()

    return render(request, 'main/add_recall.html', {'form' : form})

def price_wedding(request):
    return render(request, 'main/price-wedding.html')

def price_portret(request):
    return render(request, 'main/price-portret.html')

def nex_page(request):
    album = Album.objects.get(id=album_id).get_next_by_data()
    foto_dict['photos'] = Foto.objects.filter(album=album)
    foto_dict['album_info'] = album
    return render(request, 'main/albums.html', foto_dict)


