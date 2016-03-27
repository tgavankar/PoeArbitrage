from bs4 import BeautifulSoup
import urllib2
import re
import collections
import itertools
import time

curr = {
'alt': 1,
'fus': 2,
'alch': 3,
'c': 4,
'gcp': 5,
'ex': 6,
'chrom': 7,
'jew': 8,
'chance': 9,
'chis': 10,
'scouring': 11,
'blessed': 12,
'regret': 13,
'regal': 14,
'divine': 15,
'vaal': 16,
'wisdom': 17,
'portal': 18,
'armor': 19,
'blacksmith': 20,
'glass': 21,
'trans': 22,
'aug': 23,
#'mirror': 24,
#'etern': 25,
'coin': 26,
}

curr = collections.OrderedDict(sorted(curr.items(), key=lambda t: t[1]))

url = 'http://currency.poe.trade/search?league=Perandus&online=&want=%s&have=%s'

def web_html(want, have):
  response = urllib2.urlopen(url % (curr[want], curr[have]))
  html = response.read()
  return html

def local_html():
  return open("test.html")

def extract_cost_ratio(div):
  i = float(div["data-buyvalue"]) / float(div["data-sellvalue"])
  return i

def extract_online(soup):
  print soup.find(text='online', class_='success label').parent.attrs

def get_val(plist):
  minp = min(plist)
  avg = sum(plist) / float(len(plist))
  return "%s (%s)" % (minp, avg)

def main():
  for have in curr.keys():
    soup = BeautifulSoup(web_html('c', have), "html.parser")
    print '%s ' % have + get_val([extract_cost_ratio(i) for i in soup.find_all("div", {"class":"displayoffer"})][:5])
    #time.sleep(0.5)

if __name__ == "__main__":
  main()

