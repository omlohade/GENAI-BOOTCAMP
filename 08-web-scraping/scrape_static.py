"""
Static Web Scraping with requests + BeautifulSoup
Scrapes job listings from a static HTML page
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from headers import get_headers
from rate_limiter import rate_limit

def scrape_static_jobs(url):
    """Scrape job listings from static HTML pages"""
    all_jobs = []
    
    # Add rate limiting
    rate_limit()
    
    # Make request with proper headers
    response = requests.get(url, headers=get_headers(), timeout=10)
    
    if response.status_code != 200:
        print(f"Failed to fetch page: Status {response.status_code}")
        return all_jobs
        
    # Parse HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find job listings - using correct selectors for the demo site
    jobs = soup.find_all('div', class_='card-content')
    
    for job in jobs:
        try:
            # Extract job details
            title = job.find('h2', class_='title')
            company = job.find('h3', class_='subtitle')
            location = job.find('p', class_='location')
            
            job_data = {
                'title': title.text.strip() if title else 'N/A',
                'company': company.text.strip() if company else 'N/A',
                'location': location.text.strip() if location else 'N/A',
                'job_type': 'Full-time'  # Demo site doesn't have this field
            }
            all_jobs.append(job_data)
        except AttributeError as e:
            print(f"Error parsing job: {e}")
            continue
    
    print(f"Scraped {len(jobs)} jobs found")
    
    return all_jobs

def save_to_csv(jobs, filename='static_jobs.csv'):
    """Save scraped data to CSV"""
    df = pd.DataFrame(jobs)
    df.to_csv(filename, index=False)
    print(f"Saved {len(jobs)} jobs to {filename}")

if __name__ == "__main__":
    # Example: Using a demo job board (replace with actual URL)
    TARGET_URL = "https://realpython.github.io/fake-jobs"
    
    print("Starting static web scraping...")
    jobs = scrape_static_jobs(TARGET_URL)
    
    if jobs:
        save_to_csv(jobs)
        print(f"\nTotal jobs scraped: {len(jobs)}")
    else:
        print("No jobs found")
