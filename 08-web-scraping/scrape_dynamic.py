"""
Dynamic Web Scraping with Playwright
Scrapes JavaScript-rendered content
"""
from playwright.sync_api import sync_playwright
import pandas as pd
import time
from rate_limiter import rate_limit

def scrape_dynamic_jobs(url, max_scroll=3):
    """Scrape jobs from JavaScript-rendered pages"""
    all_jobs = []
    
    with sync_playwright() as p:
        # Launch browser (headless=False to see what's happening)
        browser = p.chromium.launch(headless=True)
        
        # Create context with realistic user agent
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        
        page = context.new_page()
        
        print(f"Navigating to {url}...")
        page.goto(url, wait_until='networkidle')
        
        # Wait for content to load
        page.wait_for_selector('.card-content', timeout=10000)
        
        # Scroll to load more content (if infinite scroll)
        for i in range(max_scroll):
            page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(1)  # Wait for new content
            print(f"Scroll {i+1}/{max_scroll}")
        
        # Extract job data using JavaScript
        jobs = page.evaluate("""
            () => {
                const jobElements = document.querySelectorAll('.card-content');
                return Array.from(jobElements).map(job => ({
                    title: job.querySelector('.title')?.textContent.trim() || 'N/A',
                    company: job.querySelector('.subtitle')?.textContent.trim() || 'N/A',
                    location: job.querySelector('.location')?.textContent.trim() || 'N/A',
                    job_type: 'Full-time'
                }));
            }
        """)
        
        all_jobs.extend(jobs)
        print(f"Extracted {len(jobs)} jobs")
        
        browser.close()
    
    return all_jobs

def save_to_csv(jobs, filename='dynamic_jobs.csv'):
    """Save scraped data to CSV"""
    df = pd.DataFrame(jobs)
    df.to_csv(filename, index=False)
    print(f"Saved {len(jobs)} jobs to {filename}")

if __name__ == "__main__":
    # Example target (replace with actual dynamic site)
    TARGET_URL = "https://realpython.github.io/fake-jobs"
    
    print("Starting dynamic web scraping with Playwright...")
    rate_limit()
    
    jobs = scrape_dynamic_jobs(TARGET_URL, max_scroll=2)
    
    if jobs:
        save_to_csv(jobs)
        print(f"\nTotal jobs scraped: {len(jobs)}")
    else:
        print("No jobs found")
