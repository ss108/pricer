import requests
from bs4 import BeautifulSoup
from utils import to_number
from source import Source

#TODO
# class SearchResult():


class PCPartPicker(Source):
    def __init__():
        self._web_root = "https://pcpartpicker.com/"
        self._part_path = "part/{slug}"
        self._search_path = "search/?live=1&qid=1&q={query}"

    def _get_part_info(part_no):
        result = requests.get(self._web_root + self._search_path.format(query = part_no))
        result_json = result.json()
        return {"slug": result_json["results"][0]["slug"]}

    def _get_page_for_product(slug):
        url = WEB_ROOT + PART_PATH.format(slug = slug)
        page_response = requests.get(url)
        page_text = page_response.text
        page = BeautifulSoup(page_text)
        return page

    def _extract_prices_from_page(product_page):
        total_table_data = product_page.find_all(attrs = {'class': 'total'}) #TODO: use "base"
        prices = [_extract_total(td) for td in total_table_data]
        return filter(lambda p: p != 0, prices) #removes cruft that's not actually a price, but empty html element. Need to make sure not to fail to consider 0 val prices in future.

    def _extract_total(total_el):
        try:
            p_link = total_el.contents[0]
            total_text = p_link.contents[0]
            return to_number(total_text)
        except:
            return 0
