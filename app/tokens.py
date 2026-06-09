import os
import hmac

_SECRET = os.environ.get("SESSION_SECRET", "dev-secret").encode()


def verify_token(authorization: str) -> bool:
    """Constant-time check that the bearer token is a valid session token."""
    if not authorization.startswith("Bearer "):
        return False
    token = authorization[len("Bearer "):]
    expected = hmac.new(_SECRET, b"session", "sha256").hexdigest()
    return hmac.compare_digest(token, expected)
