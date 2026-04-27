# 🎯 AISA Vulnerable Django App — Training Dataset

> **⚠️ FOR TRAINING & TESTING ONLY — DO NOT DEPLOY TO PRODUCTION ⚠️**

A deliberately vulnerable Django REST API designed as a labeled training dataset for **AISA** (AI Security Analysis). Modeled after OWASP WebGoat / DVWA but built specifically for ML model training and ReconAgent detection.

---

## 📁 Structure

```
vuln_django_app/
├── api/
│   ├── models.py                    # Sensitive data models (Order, UserProfile, AuditLog)
│   ├── serializers.py               # Overexposed serializers (fields="__all__")
│   ├── views.py                     # Aggregated view imports
│   ├── urls.py                      # All vulnerable endpoints registered
│   └── vulnerability_cases/
│       ├── __init__.py              # VULNERABILITY_INDEX — machine-readable manifest
│       ├── idor_case.py             # #1: IDOR / Missing Object-Level Auth
│       ├── auth_missing_case.py     # #2: Missing Authentication
│       ├── serializer_leak_case.py  # #3: Overexposed Serializer
│       ├── unsafe_filter_case.py    # #4: Unsafe Queryset Filtering
│       ├── admin_exposure_case.py   # #5: Admin Endpoint No Permission Check
│       └── token_misuse_case.py     # #6: Token Reflection / Misuse
├── aisa_labels.json                 # 🤖 ML training labels + attack chains
└── manage.py
```

---

## 🔴 Vulnerabilities Included

| # | File | `weakness_label` | CWE | OWASP | Severity | Confidence |
|---|------|-----------------|-----|-------|----------|------------|
| 1 | `idor_case.py` | `missing_object_level_auth` | CWE-639 | API1:2023 | HIGH | 0.85 |
| 2 | `auth_missing_case.py` | `missing_authentication` | CWE-306 | API2:2023 | HIGH | 0.91 |
| 3 | `serializer_leak_case.py` | `serializer_data_overexposure` | CWE-213 | API3:2023 | HIGH | 0.92 |
| 4 | `unsafe_filter_case.py` | `unsafe_queryset_filtering` | CWE-285 | API1:2023 | MEDIUM | 0.80 |
| 5 | `admin_exposure_case.py` | `admin_endpoint_no_permission_check` | CWE-862 | API5:2023 | CRITICAL | 0.95 |
| 6 | `token_misuse_case.py` | `token_reflection_no_validation` | CWE-598 | API2:2023 | MEDIUM | 0.78 |

---

## 🧠 AISA Expected Output

After scanning this repo, AISA should produce:

### Node Counts
```
endpoints  : 6
models     : 3  (Order, UserProfile, AuditLog)
auth_flows : 0  (none configured — intentional)
```

### Sample Detection
```json
{
  "type": "missing_object_level_auth",
  "confidence": 0.85,
  "source": "ml_model",
  "file": "api/vulnerability_cases/idor_case.py",
  "line": "order = Order.objects.get(id=id)"
}
```

### Attack Chain
```
PublicOrdersView (missing_auth)
  → OrderView (IDOR)
    → AdminDataView (no permission check)
      → Full user database dump
```

---

## 🤖 ML Training Usage

Each case file contains docstring metadata:
```python
"""
weakness_label: missing_object_level_auth
cwe: CWE-639
confidence_hint: 0.85
chain_hint: PublicIDOR → AnyUserAccessAnyOrder → DataLeak
"""
```

The `aisa_labels.json` file provides the complete structured training dataset with:
- `weakness_label` per vulnerability
- `detection_pattern` for the ML feature extractor
- `attack_chains` for StrategistAgent training
- `confidence_hint` for model calibration

---

## 🛠 Setup (for local testing only)

```bash
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

---

## 🧪 Webhook Test
Test commit for webhook validation — webhook trigger check 2026-04-20.
Additional test commit to verify continuous webhook delivery.
Third random commit to re-verify webhook delivery on 2026-04-26.
Final retry commit to trigger webhook after previous failure on 2026-04-26.
Extra webhook test commit generated on 2026-04-27.
---

## ✅ Design Principles

- **One vulnerability per file** — clean training signal, no mixed patterns
- **Isolated, labeled patterns** — each file = one CWE
- **Realistic code** — looks like real Django, not contrived examples
- **Machine-readable labels** — both in docstrings and `aisa_labels.json`
