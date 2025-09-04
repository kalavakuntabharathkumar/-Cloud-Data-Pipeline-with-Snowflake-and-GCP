
import base64
import os
from cryptography.fernet import Fernet

def _get_key():
    key_b64 = os.getenv("PII_TOKENIZATION_KEY")
    if not key_b64:
        raise RuntimeError("PII_TOKENIZATION_KEY missing")
    # If user provided plain text, pad/encode to 32 urlsafe bytes
    try:
        key = base64.urlsafe_b64decode(key_b64)
        if len(key) != 32:
            # re-derive from provided string
            key = base64.urlsafe_b64encode(key_b64.encode("utf-8"))[:44]  # len 32 bytes encoded ~44 chars
            key = base64.urlsafe_b64decode(key + b"=" * ((4 - len(key)%4)%4))
    except Exception:
        key = base64.urlsafe_b64encode(key_b64.encode("utf-8"))
    # Make sure final key length 32 bytes
    fkey = base64.urlsafe_b64encode(base64.urlsafe_b64decode(base64.urlsafe_b64encode(key))[:32])
    return fkey

def tokenize(value: str) -> str:
    f = Fernet(_get_key())
    return f.encrypt(value.encode("utf-8")).decode("utf-8")

def detokenize(token: str) -> str:
    f = Fernet(_get_key())
    return f.decrypt(token.encode("utf-8")).decode("utf-8")
