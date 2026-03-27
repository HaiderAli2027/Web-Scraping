from scraping.BBC_food.collect_recepies import CollectRecepies


def default(args):
    search_term = args[0]
    return CollectRecepies().Start_Collection(search_term)