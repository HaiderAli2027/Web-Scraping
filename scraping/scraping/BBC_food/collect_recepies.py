import requests
from parsel import Selector
from scraping.BBC_food.models.recipe import Recipe
from scraping.scraping.helpers import catch, to__dict

class CollectRecepies:
    def Start_Collection(self, search_term):
        result = requests.get(f'https://www.bbcgoodfoodme.com/search-results/?q={search_term}')
        html = Selector(result.text)
        recipe_nodes = html.xpath("//*[@id='main']/div[1]/div[2]/ul/li")
        
        results = []
        for node in recipe_nodes:
            node_selector = Selector(text=node.get())
            recipe = self.create_recipe(node_selector)
            if recipe:
                results.append(recipe.to_dict())
        
        return results

    @to__dict
    @catch

    def create_recipe(self, html: Selector):
        return Recipe(
            title=html.xpath(".//*[@class='entry-title']/a/text()").get(),
            description=html.xpath(".//*[@class='entry-content']/p/text()").get(),
            difficulity=html.xpath(".//div[3]/div[1]/span/text()").get()
        )
