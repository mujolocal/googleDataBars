from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
# import pandas as pd
# import os
class BarScrape(object):
    """docstring for barMetric."""
    day_o_week_re = re.compile("Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday")
    numbers = re.compile("[0-9]+")
    times = re.compile("[0-9]+\s(AM|PM)")
    day_and_hour_metric = []
    fileName = "saxbys_drexel"
    url = "https://www.google.com/search?source=hp&ei=3SkUW8jrOsbN0wKeqq9Y&q=drexel+saxbys&oq=drexel+&gs_l=psy-ab.3.0.35i39k1j0i20i264k1l2j0l7.5386.14221.0.16622.25.19.5.0.0.0.190.1928.0j12.13.0....0...1c.1.64.psy-ab..7.18.2145.6..0i131k1j0i131i20i264k1j0i10k1.191.qUmuac6AYkA"
    def __init__(self):
        pass

    def getFullRenderedHtml(self,fileName = "saxbys_drexel", url= None):
        self.fileName = fileName
        if url != None:
            self.url = url
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get(self.url)
        elem = driver.find_element_by_xpath("//*")
        file = open(self.fileName,'w')
        file.write(elem.get_attribute("outerHTML"))
        file.close()
        driver.quit()

    def getHours(self,fileName=None):
        if fileName != None:
            self.fileName = fileName
        file = open(self.fileName, 'r')
        soup = BeautifulSoup(file.read(),"html.parser")
        file.close()
        ecodF = soup.find(class_= "ecodF")
        while ecodF != None:
            # get day of week
            day = re.search(self.day_o_week_re,ecodF['aria-label']).group()
            print(day)
            # set first instance if one exists
            lubh_bar = ecodF.find(class_="lubh-bar")
            hours = []
            values = []
            while lubh_bar != None:
                # get value for hour
                try:
                    values.append(int(re.search(self.numbers,lubh_bar['style']).group()))
                    # get hour of day
                    hours.append(re.search(self.times,lubh_bar['aria-label']).group())
                except Exception as e:
                    pass

                #go to next sibling
                lubh_bar = lubh_bar.find_next_sibling()
            # add day and hours to day and hours
            self.day_and_hour_metric.append([day,hours,values])
            # cycle through siblings
            ecodF = ecodF.find_next_sibling()


if __name__ == '__main__':
    # getFullRenderedHtml()
    getHours()
