from django.urls import path

from .views import RedirectShortLinkView, CreateShortLinkView, GetUsageCountOfShortLinkView

urlpatterns = [
    path('usage-count/', GetUsageCountOfShortLinkView.as_view(), name='usage_count'),
    path('<slug:code>/', RedirectShortLinkView.as_view(), name='redirect_to'),
    path('', CreateShortLinkView.as_view(), name='create-link'),
]
