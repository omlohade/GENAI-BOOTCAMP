# HTTP Protocol Fundamentals

## What is HTTP?

HyperText Transfer Protocol - communication standard between client and server.

## Request Components

1. **Method**: GET (retrieve), POST (send data), PUT, DELETE
2. **Headers**: Metadata (User-Agent, cookies, content type)
3. **URL**: Target resource location
4. **Body**: Data payload (for POST/PUT)

## Response Components

1. **Status Code**: 200 (success), 404 (not found), 500 (server error)
2. **Headers**: Content type, encoding, cache info
3. **Body**: HTML, JSON, or other content

## Why It Matters for Scraping

- **Headers identify you**: Missing User-Agent = instant bot detection
- **Cookies maintain state**: Some sites require session cookies
- **Status codes guide logic**: Handle 429 (rate limit) differently than 404
- **HTTPS encryption**: Modern sites require SSL/TLS

## Key Headers for Scraping

- `User-Agent`: Pretend to be a real browser
- `Referer`: Shows where you came from (Google, etc.)
- `Accept-Language`: Browser language preference
- `Cookie`: Session/auth tokens
