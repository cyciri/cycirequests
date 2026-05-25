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

def h2_printer(url):
    """
   Print all the H2 tags of the given URL, in a list format.
   """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h2_tags = soup.find_all('h2')
    print(h2_tags)
