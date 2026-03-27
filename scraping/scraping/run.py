import importlib


def run_scraper(scraper, args):
    try:
        scraper = importlib.import_module(f'scraping.{scraper}.main')
        entry_point = getattr(scraper,'default')
        return  entry_point(args)

    except ModuleNotFoundError as e:
            print(f'Scraper {scraper} Not found! {e}')
        
