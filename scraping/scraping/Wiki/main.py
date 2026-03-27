        
def default(args):
   from requests import get
   import json
   import sys
   # from bs_select_opponents import get_Opponents
   from scraping.Wiki.bs_wiki_Fighter import get_Opponents,get_information,get_opponents_with_info
   if len(args) ==0:
      raise Exception("missing Something.......")
   target = args[0]
   url = args[1]
   output =args[2]

   handler = None
   if target =='oppon':
      handler = get_Opponents
   elif target == 'oppon+info':
      handler = get_opponents_with_info
   elif target == 'info':
      handler = get_information

   response =get(url)
   results = handler(response.text)
   return results
   # #json_payload = json.dumps(results,ensure_ascii = False)
   # json_payload = json.dumps(results)

   # with open(f'{output}.json','w', encoding= 'utf-8') as F:
   #    #F.write(json_payload.encode('ascii','ignore').decode('utf-8'))
   #    F.write(json_payload)

