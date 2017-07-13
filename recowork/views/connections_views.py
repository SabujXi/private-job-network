from django.shortcuts import render


def connections_view(request):
    template = 'recowork/connections.html'
    return render(request, template)
