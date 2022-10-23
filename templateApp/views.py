from json import load
from django.shortcuts import render

# Create your views here.

def indexDisplay(request):
    data = {"logo":"https://img1.freepng.es/20180711/fol/kisspng-django-web-development-web-framework-python-softwa-django-5b45d913c5b252.5696191815313042118098.jpg"}
    return render(request, 'templatesApp/index.html',data)

def electronicos(request):
    data = {"producto":"Electronicos",
            "img1":"https://assets.stickpng.com/images/5a1ac46ef65d84088faf132c.png","prod1":"mac",
            "img2":"https://marcas-logos.net/wp-content/uploads/2020/01/iPhone_logo.png","prod2":"iphone",
            "img3":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Playstation_logo_colour.svg/800px-Playstation_logo_colour.svg.png","prod3":"playstation"}
    return render(request, 'templatesApp/productos.html',data)