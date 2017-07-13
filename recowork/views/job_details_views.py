from django.shortcuts import render


def jobs_details_view(request):
    template = 'recowork/job-details.html'
    return render(request, template)
