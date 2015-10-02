import abc

class Source(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_prices(item_code):
        raise NotImplementedError()

    @abc.abstractmethod
    def average_price(item_code):
        raise NotImplementedError()

