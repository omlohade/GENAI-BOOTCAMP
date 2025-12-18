"""
Simple rate limiting to avoid overwhelming servers
Prevents IP blocking and respects server resources
"""
import time
import random

def rate_limit(min_delay=1.0, max_delay=3.0):
    """
    Add random delay between requests
    
    Args:
        min_delay: Minimum seconds to wait
        max_delay: Maximum seconds to wait
    
    Why random delay?
    - Mimics human behavior (not robotic pattern)
    - Reduces detection risk
    - Distributes server load
    """
    delay = random.uniform(min_delay, max_delay)
    print(f"Rate limiting: waiting {delay:.2f} seconds...")
    time.sleep(delay)

def adaptive_rate_limit(response_time, base_delay=1.0):
    """
    Adjust delay based on server response time
    Slower server = longer delay
    """
    # If server is slow, increase delay proportionally
    adjusted_delay = base_delay + (response_time * 0.5)
    time.sleep(min(adjusted_delay, 5.0))  # Cap at 5 seconds
