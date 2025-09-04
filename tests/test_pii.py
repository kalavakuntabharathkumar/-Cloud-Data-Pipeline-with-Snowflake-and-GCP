
import os
from security.pii import tokenize, detokenize

def test_tokenization_roundtrip(monkeypatch):
    monkeypatch.setenv("PII_TOKENIZATION_KEY", "test_key_for_demo_only___")
    secret = "user_12345"
    token = tokenize(secret)
    assert detokenize(token) == secret
