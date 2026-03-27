from parsel import Selector
import requests

result =  requests.get(f'https://www.bbcgoodfoodme.com/search-results/?q=pizza')
html = Selector(result.text)
with open ('test.html','w') as f:
   f.write(result.text)
recipe_node = html.xpath("//*[@id='main']/div[1]/div[2]/ul").get()
print(recipe_node)

#/div/div[5]/div/div[1]/div[1]/div[1]/div[2]/article/div[2]