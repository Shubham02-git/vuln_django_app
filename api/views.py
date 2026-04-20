"""
AISA Training Dataset — Main Views (aggregated)
Each view = ONE isolated vulnerability pattern.

Import these into urls.py for full endpoint coverage.
"""

from .vulnerability_cases.idor_case import OrderView
from .vulnerability_cases.auth_missing_case import PublicOrdersView
from .vulnerability_cases.serializer_leak_case import UserProfileView
from .vulnerability_cases.unsafe_filter_case import UserOrdersView
from .vulnerability_cases.admin_exposure_case import AdminDataView
from .vulnerability_cases.token_misuse_case import TokenView

__all__ = [
    "OrderView",
    "PublicOrdersView",
    "UserProfileView",
    "UserOrdersView",
    "AdminDataView",
    "TokenView",
]
