import requests
from bs4 import BeautifulSoup

url="https://cyciri.github.io/cyciri/"

def h1_printer(url):
    """
    Print the H1 tag of the given URL
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h1_tag = soup.find('h1')
    print(h1_tag.text)
