# Imports
import requests
from bs4 import BeautifulSoup

# Main function
def scraper():
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
    for python_job in python_jobs:
        print(python_job.text.strip())

# Start
scraper()