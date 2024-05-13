
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        
    def add_children(self, obj):
        self.children.append(obj)
    
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os

ALL_SITES = [
                 "http://www.stregistrafford.org/",
                 "http://www.saintsebastianchurch.org/",
                 "http://www.sssbv.org/",
                 "http://www.stmup.org/",
                 "http://theaccentonline.org/",
                 ]

IGNORE_SET = ["#genesis-footer-widgets", "#genesis-footer-content", "uploads", "cdn-cgi", 
              "school-calendar", "#genesis-content", "parish-calendar", "author", ".pdf",
              "?format", "?mcat", "calendar", "lunch-menu-cafe-schedule"]
from collections import deque
import time

class Site:
    @staticmethod
    def get_all_links(url, base_url, delay=1):
        """
        Function to fetch all unique links from a webpage within the same domain
        """
        visited = set()
        queue = deque([url])
        unique_links = set()

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
            }

            while queue:
                current_url = queue.popleft()
                if current_url in visited:
                    continue

                visited.add(current_url)

                response = requests.get(current_url, headers=headers, allow_redirects=True)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')

                    for link in soup.find_all('a'):
                        href = link.get('href')
                        if href and not any(keyword in href for keyword in IGNORE_SET):
                            full_url = urljoin(current_url, href)
                            parsed_url = urlparse(full_url)
                            if parsed_url.netloc == base_url.netloc and full_url not in visited:
                                queue.append(full_url)
                                unique_links.add(full_url)
                                print("Added link:", full_url)
                
                # Introduce a delay between requests
                time.sleep(delay)

        except requests.RequestException as e:
            print(f"Request Error occurred: {e}")
        except Exception as e:
            print(f"Error occurred: {e}")

        return unique_links


    @staticmethod
    def get_filename_from_url(url):
        """
        Function to generate a filename from the site URL
        """
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.replace('.', '_')
        return f"{domain}_unique_links.txt"

    @staticmethod
    def write_to_file(links, url):
        """
        Function to write links to a text file named after the site URL
        """
        filename = Site.get_filename_from_url(url)
        with open(filename, 'w') as file:
            for link in links:
                file.write(link + '\n')

if __name__ == "__main__":
    for site in ALL_SITES: 
        website_url = site
        base_url = urlparse(website_url)
        
        all_links = Site.get_all_links(website_url, base_url)
        
        Site.write_to_file(all_links, website_url)
        print(f"Unique links for {website_url} written to {Site.get_filename_from_url(website_url)}")
