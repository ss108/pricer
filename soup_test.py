from bs4 import BeautifulSoup
import requests

def _extract_total(total_el):
    p_link = total_el.contents[0]
    total_text = p_link.contents[0]
    return total_text

def _get_page_for_product(slug):
    page_response = requests.get("https://pcpartpicker.com/part/{s}".format(s = slug))
    page_text = page_response.text
    page = BeautifulSoup(page_text)
    return page

def get_prices_for_product(slug):
    page = _get_page_for_product(slug)
    total_table_data = page.find_all(attrs = {'class': 'total'})
    return [_extract_total(td) for td in total_table_data]




# slug = "asus-video-card-r9270xdc22gd5"

# print page.prettify()

# map(extract_total, totals)

