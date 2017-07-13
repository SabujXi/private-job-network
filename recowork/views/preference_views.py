from django.shortcuts import render


def preferences_view(request):
    template = 'recowork/preferences.html'
    return render(request, template)
