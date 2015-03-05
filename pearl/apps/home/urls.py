from django.conf.urls import url, patterns

from .views import HomeView, FAQView


urlpatterns = patterns(
    '',

    url(r'^faq/$', FAQView.as_view(), name='home_faq'),
    url(r'^$', HomeView.as_view(), name='home_home'),
)
