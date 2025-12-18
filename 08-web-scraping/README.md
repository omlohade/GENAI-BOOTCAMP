# Web Scraping Project

## Why Web Scraping?

**The Problem**: Many websites don't provide APIs to access their data programmatically. To extract structured information (job listings, product prices, news articles), we need to scrape the HTML.

**Real-world scenarios**:

- Job aggregators scraping listings from multiple sites
- Price comparison engines
- Market research and sentiment analysis
- Academic research data collection

---

## Static vs Dynamic Scraping

### Static Scraping (requests + BeautifulSoup)

- **What**: Server sends complete HTML in initial response
- **When to use**: Simple websites where content is in HTML source (View Page Source shows data)
- **How it works**:
  1. Send HTTP GET request
  2. Receive HTML response
  3. Parse HTML with BeautifulSoup
  4. Extract data using CSS selectors

### Dynamic Scraping (Playwright/Selenium)

- **What**: Content loaded by JavaScript after page loads
- **When to use**: Modern SPAs (React, Vue, Angular), infinite scroll, interactive elements
- **How it works**:
  1. Launch headless browser
  2. Execute JavaScript
  3. Wait for dynamic content to render
  4. Extract data from rendered DOM

**Key difference**: Static scraping sees raw HTML; dynamic scraping sees what browser renders.

---

## How HTTP, DOM, and JS Rendering Affect Scraping

### HTTP Protocol

- **Request-Response cycle**: Client sends request → Server sends response
- **Headers matter**: User-Agent, cookies, referer determine what server sends
- **Status codes**: 200 (OK), 403 (Forbidden), 429 (Rate limited), 503 (Blocked)

### DOM (Document Object Model)

- **What**: Tree structure representing HTML
- **Selectors**: CSS (`.class`, `#id`, `tag`) or XPath (`//div[@class="job"]`)
- **Parsing**: BeautifulSoup converts HTML string → navigable tree

### JavaScript Rendering

- **Client-side rendering**: Data fetched via AJAX/fetch, rendered by JS
- **Challenge**: requests library can't execute JavaScript
- **Solution**: Use browser automation (Playwright, Selenium)

---

## Security Challenges

### CAPTCHA

- **Purpose**: Distinguish humans from bots
- **Types**: Image recognition, reCAPTCHA, hCaptcha
- **Handling**:
  - Avoid triggering: Rate limiting, realistic headers
  - Solving: Manual intervention or third-party services (not included here)

### IP Blocking

- **Why**: Server detects suspicious patterns (too many requests, no headers)
- **Prevention**:
  - Rate limiting (random delays)
  - Rotating user agents
  - Proxy rotation (not implemented here)
  - Respecting robots.txt

### Other Protections

- **Session cookies**: Some sites require cookies from initial page load
- **Anti-scraping JS**: Code that detects headless browsers
- **Honeypot traps**: Hidden links that mark bots

---

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers (one-time setup)
playwright install chromium
```

---

## Usage

### Static Scraping

```bash
python scrape_static.py
```

Output: `static_jobs.csv`

### Dynamic Scraping

```bash
python scrape_dynamic.py
```

Output: `dynamic_jobs.csv`

---

## Project Structure

```
08-web-scraping/
├── scrape_static.py      # BeautifulSoup scraper
├── scrape_dynamic.py     # Playwright scraper
├── headers.py            # Browser-like headers
├── rate_limiter.py       # Request throttling
├── requirements.txt      # Dependencies
├── README.md             # This file
└── notes/
    ├── http-protocol.md          # HTTP fundamentals
    ├── dom-parsing.md            # DOM structure & selectors
    ├── javascript-rendering.md   # JS execution challenges
    └── security-handling.md      # CAPTCHA, IP blocking
```

---

## Ethical Considerations

1. **Check robots.txt**: Respect site's scraping policy
2. **Rate limiting**: Don't overwhelm servers
3. **Terms of Service**: Read and comply
4. **Personal data**: Don't scrape private/sensitive information
5. **Attribution**: Credit data sources

---

## Common Issues & Solutions

| Issue         | Cause                   | Solution                       |
| ------------- | ----------------------- | ------------------------------ |
| 403 Forbidden | Missing/invalid headers | Use realistic User-Agent       |
| Empty results | JS-rendered content     | Switch to Playwright           |
| IP blocked    | Too many requests       | Add rate limiting, use proxies |
| Stale data    | Cached responses        | Add cache-busting params       |

---

## Next Steps

- Implement proxy rotation for large-scale scraping
- Add database storage (SQLite/PostgreSQL)
- Create scheduling with cron/Airflow
- Build data pipeline with cleaning/validation
- Add monitoring and error alerts
