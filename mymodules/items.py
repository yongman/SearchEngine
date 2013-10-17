from scrapy.item import Item, Field


class Website(Item):
    url = Field()
    title = Field()
    content = Field()

