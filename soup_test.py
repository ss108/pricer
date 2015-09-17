from bs4 import BeautifulSoup
import requests

def extract_total(total_el):
    p_link = total_el.contents[0]
    total_text = p_link.contents[0]
    print total_text


slug = "asus-video-card-r9270xdc22gd5"

page_response = requests.get("https://pcpartpicker.com/part/{s}".format(s = slug))
page_text = page_response.text
page = BeautifulSoup(page_text)
# print page.prettify()
totals = page.find_all(attrs = {'class': 'total'})

map(extract_total, totals)

