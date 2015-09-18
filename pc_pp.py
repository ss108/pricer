import requests
from bs4 import BeautifulSoup
from utils import to_number

WEB_ROOT = "https://pcpartpicker.com/"
PART_PATH = "part/{slug}"
SEARCH_PATH = "search/?live=1&qid=1&q={query}"

def get_part_info(part_no):
    result = requests.get(WEB_ROOT + SEARCH_PATH.format(query = part_no))
    result_json = result.json()
    return {"slug": result_json["results"][0]["slug"]}

def get_average_price(part_no):
    slug = get_part_info(part_no)["slug"]
    product_page = _get_page_for_product(slug)
    prices = _extract_prices_from_page(product_page)
    return (sum(prices)/len(prices))

def _get_page_for_product(slug):
    url = WEB_ROOT + PART_PATH.format(slug = slug)
    print url
    page_response = requests.get(url)
    page_text = page_response.text
    page = BeautifulSoup(page_text)
    return page

def _extract_prices_from_page(product_page):
    total_table_data = product_page.find_all(attrs = {'class': 'total'}) #TODO: use "base"
    return [_extract_total(td) for td in total_table_data]

def _extract_total(total_el):
    try:
        p_link = total_el.contents[0]
        total_text = p_link.contents[0]
        return to_number(total_text)
    except:
        return 0
