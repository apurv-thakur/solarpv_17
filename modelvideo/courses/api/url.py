from django.urls import path
from . import views

app_name = "solar"
urlpatterns = [
    path("solar/", views.OrganizationListView.as_view(), name="organization_list"),
    path(
        "solar/<pk>/",
        views.OrganizationDetailView.as_view(),
        name="organization_detail",
    ),
]
