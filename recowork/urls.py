from django.conf.urls import url
from recowork.views.home_views import (
    index_view
)

from recowork.views.connections_views import (
    connections_view
)

from recowork.views.find_jobs_views import (
    find_jobs_view
)

from recowork.views.job_details_views import (
    jobs_details_view
)

from recowork.views.preference_views import (
    preferences_view
)

from recowork.views.profile_views import (
    profile_view
)

urlpatterns = [
    url(r"^$", index_view, name="home"),
    url(r"^connections$", connections_view, name="connections"),
    url(r'^find-jobs$', find_jobs_view, name='find_jobs'),
    url(r'^job-details$', jobs_details_view, name='job_details'),
    url(r'^preferences$', preferences_view, name='preferences'),
    url(r'^profile$', profile_view, name='profile')
]
