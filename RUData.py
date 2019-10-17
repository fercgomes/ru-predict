import requests
import urllib.request
import time
from bs4 import BeautifulSoup

placeholder = {
    {
        "timestamp": "",
        "dataRU1": [],
        "dataRU2": [],
        "dataRU3": [],
        "dataRU4": [],
        "dataRU5": [],
        "dataRU6": [],
        "dataRU7": [],
    },
}

class RUData:

    def __init__(self, url="http://www.ufrgs.br/ufrgs/ru", dataFile="past_data.json"):
        self.url = url
        self.dataFile = dataFile

    def getDataFromURL(self):
        assert(self.url is not "")
        assert(self.dataFile is not "")

        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

    
