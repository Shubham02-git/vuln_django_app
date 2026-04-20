"""
AISA Training Dataset — Serializers
Vulnerability: Overexposed Serializer (fields = "__all__")

weakness_label: serializer_data_overexposure
cwe: CWE-213 (Exposure of Sensitive Information Due to Incompatible Policies)
confidence_hint: 0.92
chain_hint: serializer_leak → sensitive_field_exposure → data_breach
"""

from rest_framework import serializers
from .models import Order, UserProfile, AuditLog


# ============================================================
# VULNERABILITY: SERIALIZER OVEREXPOSURE
# All fields exposed including: ssn, api_token, credit_card_last4
# AISA should flag: fields="__all__" on sensitive models
# ============================================================

class OrderSerializer(serializers.ModelSerializer):
    """
    weakness_label: serializer_overexposure
    notes: Exposes credit_card_last4, address — PII fields
    """
    class Meta:
        model = Order
        fields = "__all__"   # ❌ VULNERABILITY: exposes all fields including PII


class UserProfileSerializer(serializers.ModelSerializer):
    """
    weakness_label: serializer_overexposure
    severity: CRITICAL
    notes: Exposes ssn and api_token — auth secrets + PII
    """
    class Meta:
        model = UserProfile
        fields = "__all__"   # ❌ CRITICAL: ssn + api_token exposed


class AuditLogSerializer(serializers.ModelSerializer):
    """
    weakness_label: internal_data_exposure
    notes: Internal audit log should never be serialized to API responses
    """
    class Meta:
        model = AuditLog
        fields = "__all__"   # ❌ VULNERABILITY: internal system data exposed
