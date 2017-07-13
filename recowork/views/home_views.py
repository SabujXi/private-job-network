from django.shortcuts import render


def index_view(request):
    template = "recowork/index.html"
    return render(request, template)

