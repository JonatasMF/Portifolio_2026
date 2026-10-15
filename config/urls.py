from django.urls import include, path

from portfolio.views import handler404 as portfolio_handler404

urlpatterns = [
    path("", include("portfolio.urls")),
]

handler404 = portfolio_handler404
