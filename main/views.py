from django.shortcuts import render
from main.models import Album, Foto
from  main.forms import RecallForm

context_dict = {}
foto_dict = {}

def index(request):
    return render(request, 'main/index.html')

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
    if album_list.count() == 1:
        context_dict['photos'] = Foto.objects.filter(album=album_list)
    context_dict['title'] = album_list[0].categories
    return render(request, 'main/categories.html', context_dict)

def albums(request, album_id):
    album = Album.objects.get(id=album_id)
    foto_dict['photos'] = Foto.objects.filter(album= album)
    foto_dict['album_info'] = album
    return render(request, 'main/albums.html', foto_dict)

def add_recall(request):
    if request.method == 'Post':
        form = RecallForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return contact(request)
        else:
            print(form.errors)
    else:
        form = RecallForm()

    return render(request, 'main/add_recall.html', {'form' : form})

def price_wedding(request):
    return render(request, 'main/price-wedding.html')

def price_portret(request):
    return render(request, 'main/price-portret.html')


