from django.shortcuts import render
from django import forms
#from django.urls import reverse

from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# def create(request):
#     return render(request, "encyclopedia/create.html", {
#         "entries": util.save_entry(title, content)
#     })
#
# def random(request):
#     return render(request, "encyclopedia/random.html", {
#         "entries": util.get_entry(title)
#     })


def css(request,title):
    return render(request,"encyclopedia/index.html", {
        "title": util.get_entry(title)
    })
