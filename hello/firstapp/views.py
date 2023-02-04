from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return render(request, "firstapp/home.html")
    header = "Персональные данные"                      # обычная переменная
    langs = ["Английский", "Немецкий", "Испанский"]     # массив
    user = {"name": "Максим", "age": 30}                # словарь
    addr = ("Виноградная", 23, 45)                      # кортеж
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, "index.html", context=data)

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def products(request, productid=1):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория: {1}</h2>"\
        .format(productid, category)
    return HttpResponse(output)

def users(request, id=1, name="Максим"):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3>"\
        .format(id, name)
    return HttpResponse(output)
