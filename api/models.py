"""
AISA Training Dataset — Models
Labels: data_model, sensitive_fields
"""

from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    """
    vulnerability_label: sensitive_model
    notes: Contains financial + PII fields, used in IDOR and serializer leaks
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()           # PII
    credit_card_last4 = models.CharField(max_length=4)  # sensitive
    status = models.CharField(max_length=50, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order#{self.id} by {self.user}"


class UserProfile(models.Model):
    """
    vulnerability_label: sensitive_model
    notes: Contains SSN, token — targets for overexposed serializer
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=11, blank=True)       # highly sensitive
    api_token = models.CharField(max_length=64, blank=True)  # auth secret
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"Profile of {self.user}"


class AuditLog(models.Model):
    """
    vulnerability_label: sensitive_model
    notes: Internal log — should never be publicly exposed
    """
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    action = models.TextField()
    ip_address = models.GenericIPAddressField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log@{self.timestamp}"
