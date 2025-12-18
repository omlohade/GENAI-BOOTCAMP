"""
Centralized HTTP headers for web scraping
Mimics real browser behavior to avoid detection
"""

def get_headers():
    """
    Returns browser-like headers to avoid bot detection
    
    Key headers:
    - User-Agent: Identifies as a real browser
    - Accept: Specifies acceptable response types
    - Accept-Language: Browser language preference
    - Accept-Encoding: Compression support
    - DNT: Do Not Track (privacy header)
    - Connection: Keep-alive for performance
    - Referer: Simulate navigation from search engine
    """
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://www.google.com/',
        'Cache-Control': 'max-age=0'
    }

def get_json_headers():
    """Headers for API-like requests expecting JSON response"""
    headers = get_headers()
    headers.update({
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
    })
    return headers
