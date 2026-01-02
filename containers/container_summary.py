"""

Type            Brackets      Ordered           hashable ? (Immutable ?)             Items must be hashable ? (Immutable ?)

Tuple           ()            Yes               Immutable, if elements hashable         No
List            []            Yes               Mutable                                 No
Set             {}            No                Mutable                                 Yes
Dict            {}            Yes (> 3.6)       Mutable                                 Keys : Yes, Values : No



Time complexity :
===============

* If you want to lookup items by some item that you already got, use a set or dict
* If you want to insert items at arbitary locations avoid using a list


Reference : https://wiki.python.org/moin/TimeComplexity

"""