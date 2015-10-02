import abc

class Source(object):
    """
    Maybe make child class like "APISource" or "ScrapeSource"
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_all_prices(self, item_code):
        raise NotImplementedError()

    @abc.abstractmethod
    def calc_average_price(self, item_code):
        raise NotImplementedError()

