from . import category
from . import ping
from . import products

labelers = [category.labeler, ping.labeler, products.labeler]

__all__ = ["labelers"]
