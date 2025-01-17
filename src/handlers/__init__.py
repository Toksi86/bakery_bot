from . import category
from . import ping

labelers = [category.labeler, ping.labeler]

__all__ = ["labelers"]
