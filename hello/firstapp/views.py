from django.http import *
from django.shortcuts import render
from .forms import UserForm

def index(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse(f"<h2>Имя введено корректно - "
                                f"{name}</h2>")
    return render(request, "firstapp/index.html",
                  {"form": userform})
