"""
AISA Training Dataset — URL Configuration
All vulnerable endpoints registered here.
AISA parser should detect these routes and map to view classes.
"""

from django.urls import path
from api.views import (
    OrderView,          # IDOR
    PublicOrdersView,   # Missing Auth
    UserProfileView,    # Serializer Leak
    UserOrdersView,     # Unsafe Filter
    AdminDataView,      # Admin Exposure
    TokenView,          # Token Misuse
)
from api.vulnerability_cases.sql_injection_case import OrderSearchView
from api.vulnerability_cases.insecure_file_access_case import FileDownloadView

urlpatterns = [
    # weakness: missing_object_level_auth (IDOR)
    path("api/orders/<int:id>/", OrderView.as_view(), name="order-detail"),

    # weakness: missing_authentication
    path("api/orders/public/", PublicOrdersView.as_view(), name="orders-public"),

    # weakness: serializer_data_overexposure
    path("api/profile/<int:user_id>/", UserProfileView.as_view(), name="user-profile"),

    # weakness: unsafe_queryset_filtering
    path("api/orders/filter/", UserOrdersView.as_view(), name="orders-filter"),

    # weakness: admin_endpoint_no_permission_check (CRITICAL)
    path("api/admin/users/", AdminDataView.as_view(), name="admin-users"),

    # weakness: token_reflection_no_validation
    path("api/token/debug/", TokenView.as_view(), name="token-debug"),

    # weakness: sql_injection (CRITICAL)
    path("api/orders/search/", OrderSearchView.as_view(), name="orders-search"),

    # weakness: path_traversal (CRITICAL)
    path("api/files/download/", FileDownloadView.as_view(), name="file-download"),
]
