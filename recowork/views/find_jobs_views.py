from django.shortcuts import render


def find_jobs_view(request):
    template = 'recowork/find-jobs.html'
    return render(request, template)
