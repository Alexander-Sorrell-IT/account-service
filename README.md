# account-service

A tiny Flask service with an admin blueprint. The `/admin/users` route returns
every user record (roles included), so it is gated behind `@login_required`.

```
app/
  auth.py     # login_required decorator
  tokens.py   # session-token verification
  db.py       # user store
  views.py    # admin routes
```
