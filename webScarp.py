#!/usr/bin/env python
# This module deals with scraping the href of videos and 
# server urls from a web page.
# Modules used for development are Python3.6 & Selenium



from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

"""
This class contains the main function used for scraping through the web page and extracting the video sources and 
hyper links
"""
class scarpThroughWeb:
   """
   Steps to extract
   1. Get the Chrome Driver & get the chrome driver .crx file
   2. Get the web page using the driver
   3. Find the html division with class attribute as 'serversList'
   4. If that division exists then get the lst of all the servers 
   5. Now we are good with all the video source serversList
   6. Next we click on the link and thish taes us to the page where all the hyperlinks are present 
   7. We have our chunk of website urls ready
   8. We find iframes and add it to the list
   """
   def scrapWeb(self):
      try:
        options = webdriver.ChromeOptions()
        options.add_extension(r'C:\Users\Chandrani\Documents\PythonSeleniumScripts\selepy1.crx')
        driver = webdriver.Chrome(chrome_options = options)
        driver.set_page_load_timeout(40)
        driver.get("https://cima4k.tv/%D9%85%D8%B3%D9%84%D8%B3%D9%84-the-flash-%D8%A7%D9%84%D9%85%D9%88%D8%B3%D9%85-%D8%A7%D9%84%D8%B1%D8%A7%D8%A8%D8%B9-%D8%A7%D9%84%D8%AD%D9%84%D9%82%D8%A9-9-%D8%A7%D9%84%D8%AA%D8%A7%D8%B3%D8%B9%D8%A9/?view=1")
        time.sleep(5)
        urls = []
        sources = []

        if driver.find_elements_by_xpath("//*[(contains(@class,'serversList'))]"):
            buttons = driver.find_elements_by_xpath("//ul[contains(@class,'serversList')]/li")
            path = os.getcwd()
            print(path)
            f = open(os.path.join(path + "serverList"),'w')
            f.write(str(buttons))
            time.sleep(2)
            f.close()
            print(buttons)
            if buttons:
                for button in buttons:
                    button.click()
                    time.sleep(2)
                    hrefs = driver.find_elements_by_xpath("//*[contains(@class,'tab')]//a")
                    for ref in hrefs:
                       sources.append(ref.get_attribute('href'))
                       f = open(os.path.join(path + "hyperLinks"),'w')
                       f.write(str(sources))
                       f.close()


            iframes = driver.find_elements_by_xpath("//*[contains(@id,'_atssh')]//iframe")
            print(str(iframes))
            print("End of the main function")
      except Exception as e:
           print(e)
      finally:
           driver.close()
      return sources
        
if __name__ == "__main__":
    # Get the scarpThroughWeb class object 
    scrapObj = scarpThroughWeb()
    # Call the scrapWeb function of the class 
    urls = scrapObj.scrapWeb()
    print(" ")
    # Print all the sources
    for url in urls:
        print(url)
    print("End of the program")