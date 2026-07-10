# Authentication — Q&A (todoapp)

Password hashing and JWT-based auth.

---

### Q: Why store a hashed password (and why bcrypt over SHA-256)? How does the server trust a JWT without a DB lookup?

**A (hashing):** A hash is **one-way** — verify a login by hashing the input and comparing;
can't reverse it to the password. So a DB breach doesn't expose usable passwords.

*Which* hash matters:
- **SHA-256/MD5 are wrong for passwords** — designed to be **fast** → attacker tries
  billions of guesses/sec on a GPU (brute force, rainbow tables).
- **bcrypt/argon2/scrypt are deliberately slow + adaptive** — a **work factor/cost** you can
  raise over time, making each guess expensive.
- bcrypt **salts automatically** (random salt per password baked into the hash) → same
  password → different hashes → defeats rainbow tables and hides shared passwords.

So: hashing protects against theft; a **slow, salted** hash protects against **cracking**.

**A (JWT trust):** The token is **cryptographically signed** by the server, so each request
just **re-verifies the signature** with the server's secret — valid + unexpired ⇒ the claims
(user id, roles) are trustworthy, no DB hit.

JWT = `header.payload.signature`:
- **payload** = claims (`sub`, roles, `exp`) — only base64, **not encrypted**; anyone can
  read it → **never put secrets in a JWT**.
- **signature** = `HMAC(header+payload, secret)` (or RSA). Tampering with the payload breaks
  the signature → verification fails.

It's **stateless/self-contained**: only the server's secret can produce a valid signature,
so no session store / per-request DB query needed.

**Follow-up — downside of stateless JWT:** hard to **revoke**. A DB session can be deleted
instantly; a signed JWT is valid until `exp`. Mitigate with **short-lived access tokens +
refresh tokens** and/or a **denylist** (reintroduces some state). Trade-off: stateless &
scalable vs. hard to revoke.

**Where in the project:** auth/login flow (see `docs/authentication.png`).

---
