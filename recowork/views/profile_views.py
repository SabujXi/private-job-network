from django.shortcuts import render


def profile_view(request):
    template = 'recowork/profile.html'
    return render(request, template)
