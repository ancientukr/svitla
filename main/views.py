from django.shortcuts import render
from main.models import Album, Foto

def index(request):
    albums_list = Album.objects.all()
    context_dict = {'Albums': albums_list}
    return render(request, 'main/index.html', context_dict)
