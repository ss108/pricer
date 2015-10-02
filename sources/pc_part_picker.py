import requests
from bs4 import BeautifulSoup
from utils import to_number, average
from source import Source

#TODO
# class SearchResult():


class PCPartPicker(Source):
    def __init__():
        self._web_root = "https://pcpartpicker.com/"
        self._part_path = "part/{slug}"
        self._search_path = "search/?live=1&qid=1&q={query}"

    def _get_part_info(self, part_no):
        """
        Makes request to PCPartPicker for basic info about parts that match the query. For our purposes for the time being, we will assume the first result is correct. The only
        field we are interested in is the "slug"
        :param part_no:
        """
        result = requests.get(self._web_root + self._search_path.format(query = part_no))
        result_json = result.json()
        return {"slug": result_json["results"][0]["slug"]} #TODO: What if no results?

    def _get_page_for_product(self, slug):
        """
        Returns BeautifulSoup instance of product page for product with given slug.
        """
        url = self._web_root + self._part_path.format(slug = slug)
        page_response = requests.get(url)
        page_text = page_response.text
        page = BeautifulSoup(page_text)
        return page

    def _extract_prices_from_page(self, product_page):
        total_table_data = product_page.find_all(attrs = {'class': 'total'}) #TODO: use "base"
        prices = [_extract_total(td) for td in total_table_data]
        return filter(lambda p: p != 0, prices) #removes cruft that's not actually a price, but empty html element. Need to make sure not to fail to consider 0 val prices in future.

    def _extract_total(self, total_el):
        try:
            p_link = total_el.contents[0]
            total_text = p_link.contents[0]
            return to_number(total_text)
        except:
            return 0

    def get_all_prices(self, part_no):
        part_info = self._get_part_info(part_no)
        page = self._get_page_for_product(part_info["slug"])
        return self._extract_prices_from_page(page)

    def calc_average_price(self, part_no):
        prices = self.get_all_prices(part_no)
        return average(prices) 


