import scrapy


class LightingSpider(scrapy.Spider):
    name = "lighting_spider"
    allowed_domains = ["https://www.divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]  # Замените на реальный URL категории освещения

    custom_settings = {
        'DOWNLOAD_DELAY': 1,  # Задержка между запросами в секундах
        'FEED_EXPORT_ENCODING': 'utf-8',  # Кодировка для экспорта
    }

    def parse(self, response):
        """
        Парсинг страницы с продуктами освещения.
        """
        # Извлечение списка продуктов на странице
        products = response.css("div._Ud0k")  # Замените на актуальный CSS-селектор

        for product in products:
            name = product.css("div.lsooF span::text").get()
            price = product.css("div.pY3d2 span::text").get()
            relative_link = product.css("a").attrib["href"]
            link = response.urljoin(relative_link)

            yield {
                'Название': name.strip() if name else None,
                'Цена': price.strip() if price else None,
                'Ссылка': link,
            }

        # Обработка пагинации
      #  next_page = response.css("a.pagination-next::attr(href)").get()
     #  if next_page:
      #      yield response.follow(next_page, callback=self.parse)
