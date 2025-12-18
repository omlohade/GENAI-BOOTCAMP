# Security & Anti-Scraping Measures

## 1. CAPTCHA

**Purpose**: Block automated bots.

**Types**:

- Image recognition (select traffic lights)
- reCAPTCHA (checkbox + behavior analysis)
- hCaptcha (privacy-focused alternative)

**How to Avoid**:

- Rate limiting (don't spam requests)
- Realistic browser headers
- Human-like behavior (random delays, mouse movements)

**If Triggered**: Manual solving or paid services (not ethical for large scale).

---

## 2. IP Blocking

**Detection**:

- Too many requests from same IP
- Requests without proper headers
- Access patterns (scraping entire site in minutes)

**Prevention**:

- Rate limiting (1-3 second delays)
- Rotating proxies (residential IPs)
- Distributed scraping (multiple machines)

**Response**: 403 Forbidden, 429 Too Many Requests, or silent block (empty responses).

---

## 3. Other Protections

### User-Agent Checking

Server blocks requests without User-Agent or known bot agents.
**Fix**: Use realistic browser User-Agent.

### JavaScript Challenges

Site executes JS to verify browser environment (e.g., checks `navigator` object).
**Fix**: Use Playwright to execute JS.

### Honeypot Traps

Hidden links invisible to humans but visible to bots.
**Avoid**: Don't follow all links blindly.

### Session/Cookie Validation

Site requires cookies from initial page load.
**Fix**: Use `requests.Session()` or Playwright's persistent context.

---

## Ethical Scraping

1. Check `robots.txt` (e.g., `site.com/robots.txt`)
2. Respect rate limits
3. Read Terms of Service
4. Don't scrape personal data
5. Don't resell scraped data without permission
