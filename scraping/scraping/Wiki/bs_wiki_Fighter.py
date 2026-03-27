from parsel import Selector
from requests import get
import re
import dateparser

def get_opponents_with_info(html):
   opponents = get_Opponents(html)
   for o in opponents:
      if link := o.get("link"):
         response =get(link)
         o['info'] = get_information(response.text)
      
   return opponents
            
 
def get_Opponents(html):
   selector =  Selector(text=html)
   match = selector.xpath('//table[@class="wikitable"]')[0]
   trs = match.xpath(".//tr")
  
     
   opponents = []

   for tr in trs[1:]:
      opponent = {
         'link':None,
         'name': None,
         'OutCome':None,
      }
      opponent['OutCome'] = tr.xpath("./td[1]/text()").get().strip('\n')
      opponent_node = tr.xpath("./td[3]")
      anchors = opponent_node.xpath('a')
      if len(anchors)== 1:
         a = anchors[0]
         href = a.xpath("@href").get()
         opponent['link'] = f"https://en.wikipedia.org{href}"
         opponent_name = a.xpath("text()").get()
      else:
         opponent_name = opponent_node.xpath("text()").get()

         
      opponent['name'] = opponent_name.strip('\n')
      opponents.append(opponent)
        
   return opponents


def get_information(html):
   selector = Selector(text=html)
   trs = selector.xpath('//table[@class="infobox vcard"]/tbody/tr')
  

   
   information = {

         'name': None,
         'image': None,
         'nickName':None,
      
         'Height':None,
         'Weight':None,
         'Birth':None,
         # 'Style':None,
      }

   information['name'] =trs[0].xpath(".//span/text()").get()
   image = trs[1].xpath(".//a/@href").get()
   information['image'] =f"https://en.wikipedia.org{image}"
   for tr in trs[2:]:
      
      key : str = tr.xpath('./th/text()').get()
      value = tr.xpath('./td/text()').get()
      
      # anc = tr.xpath('./td/a/text()').get()
      
      if key is None or value is None:
         continue

      if key.startswith('Nickname'):
         information['nickName'] = value
      
      elif key.startswith('Height'):
         match = re.search('(?P<imperic>\d.ft \d{1,2}.in) \((?P<metric>[\d.]+.c?m)\)',value)

         if match is None:
            print("Failed height match",value)
            continue
         information['Height']= {
             'imperial':match.group('imperic').replace('\u00a0',' '),
            'Metric':match.group('metric').replace('\u00a0',' '),

         }

      elif key.startswith('Weight'):
         match = re.search('(?P<imperic>\d{1,3}.lb) \((?P<metric>\d{1,3}.kg); (?P<eng>[\d.]+.st(?: \d.lb)?)\)',value)
         if match is None:
            print("Failed weight match",value)
            continue
         information['Weight']= {
             'imperial':match.group('imperic').replace('\u00a0',' '),
             'Metric':match.group('metric').replace('\u00a0',' '),
             'eng':match.group('eng').replace('\u00a0',' '),
            # 'imperial':imp,
            # 'Metric':metric,

         }
      elif key.startswith('Born'):
         Born_section = (tr.xpath('./td').get())
         match = re.search('<\/span>(?P<date>[\w ,]+)<span',Born_section)
         if match is None:
            continue
         
         information['Birth'] =  str(dateparser.parse(match.group('date')))
         
        
         


         
      # elif key.startswith('Style'):
      #    information['Style'] = anc
      
      
      
   return information


# **********  code By Haider  ***********

# def get_information(html):
#    selector = Selector(text=html)
#    match = selector.xpath("//table[1]//tbody")[0]
#    trs = match.xpath(".//tr")

#    info = []
#    information = {

#          'Name': None,
#          'NickName':None,
#          'Nationality':None,
#          'Height':None,
#          'Weight':None,
#          'Style':None,
#       }

#    for tr in trs:
      
#       information['Name'] =tr.xpath("//tr[1]/th/span/text()").get().strip('\n')
#       information['NickName'] =tr.xpath("//tr[5]/td/text()").get().strip('\n')
#       information['Nationality'] = tr.xpath("//tr[6]/td/text()").get().strip('\n')
#       information['Height'] = tr.xpath("//tr[7]/td/text()").get().strip('\n')
#       information['Weight'] = tr.xpath("//tr[8]/td/text()").get().strip('\n')

#       info_node = tr.xpath("//tr[11]/td")
#       anc = info_node.xpath("a")
#       a_text = anc.xpath("text()").get()

#       information['Style'] = a_text
      
#    return information
    



   