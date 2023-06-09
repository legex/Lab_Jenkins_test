import requests
from bs4 import BeautifulSoup
from datetime import*
import re
import sslbypass

class URLAccess():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def urlaccessed(url):
        try:
            req=sslbypass.get_legacy_session().get(url)
            return req.status_code
        except ConnectionError:
            return "404 Not found"


if __name__== '__main__':
    run=URLAccess.urlaccessed(url="https://www.youtube.com")
    print(run)
