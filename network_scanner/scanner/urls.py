from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("scan-network/", views.scan_network, name="scan_network"),
    path("scan-ports/", views.scan_ports, name="scan_ports"),
    path("traceroute/", views.traceroute, name="traceroute"),
    path("speedtest/", views.speedtest, name="speedtest"),
    path("view-scan-results/", views.view_scan_results, name="view_scan_results"),
    path("update-alias/", views.update_alias, name="update_alias"),
    path(
        "delete_selected_results/",
        views.delete_selected_results,
        name="delete_selected_results",
    ),
]
