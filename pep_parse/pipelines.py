import csv
from collections import defaultdict

from scrapy.exceptions import DropItem

from pep_parse.settings import BASE_DIR, RESULTS_DIR

FILENAME = 'status_summary_{time}.csv'


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        if 'status' not in item:
            raise DropItem('No status.')
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(self.results_dir/FILENAME,
                  mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Статус', 'Количество'])
            total = 0
            for status, count in self.status_count.items():
                writer.writerow([status, count])
                total += count
            writer.writerow(['Total', total])
