from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
from pprint import pprint
from bs4 import  BeautifulSoup
import json
import jsonpickle
import xlrd
import requests
from pyvirtualdisplay import Display


# display = Display(visible=0, size=(800, 800))
# display.start()

# Function to access Agency LB Website and retrieve Google Maps API link
def get_Google_Maps_API_Link(driver, url):
    # Access web page
    driver.get(url)
    # Gather all elements that have an img tag
    _inputs = driver.find_elements_by_xpath('//img')
    # print page title for easy reference and review
    print driver.title
    # Loop through all img web elements and find element holding the Google API Link
    for input in _inputs:
        item = str(input.get_attribute('src'))
        if 'https://maps.googleapis.com/maps/api' in item:
            # Return the Google API link
            apiLink = input.get_attribute('src')
    apiRequest = requests.get(apiLink)
    statusCode = apiRequest.status_code
    return statusCode

class Verify_LB_Web_Map(unittest.TestCase):


    def test_LB_Maps(self):
        driver = webdriver.Chrome()
        testcounter = 0

        # Idaho LB Web Test
        urlID = 'http://lb.511.idaho.gov/idlb/'
        # Get Map link that connects with Google API
        IDStatusCode = get_Google_Maps_API_Link(driver, urlID)
        print IDStatusCode

        # If the map is down, then the test will fail and trigger an email in Jenkins
        if  IDStatusCode != 200:
            print 'LB Idaho Map Is Down'
            testcounter += 1

        # Louisiana
        urlLA = 'https://lb.511la.org/lalb/'
        LAStatusCode = get_Google_Maps_API_Link(driver, urlLA)
        print LAStatusCode

        if  LAStatusCode != 200:
            print 'LB Loisiana Map Is Down'
            testcounter += 1

        # Nebraska
        urlNE = 'https://lb.511.nebraska.gov/nelb/'
        linkNE = get_Google_Maps_API_Link(driver, urlNE)
        rNE = requests.get(linkNE)
        print rNE.status_code

        if  rNE.status_code != 200:
            print 'LB Nebraska Map Is Down'
            testcounter += 1

        # Iowa
        urlIA = 'https://lb.511ia.org/ialb/'
        linkIA = get_Google_Maps_API_Link(driver, urlIA)
        rIA = requests.get(linkIA)
        print rIA.status_code

        if  rIA.status_code != 200:
            print 'LB Iowa Map Is Down'
            testcounter += 1

        # Sacog
        urlSACOG = 'http://sa.carsstage.org/salbweb/'
        linkSACOG = get_Google_Maps_API_Link(driver, urlSACOG)
        rSACOG = requests.get(linkSACOG)
        print rSACOG.status_code

        if  rSACOG.status_code != 200:
            print 'LB Sacramento Map Is Down'
            testcounter += 1

        # Sandag
        urlSAN = 'https://lbw.511sd.com/lbweb/'
        linkSAN = get_Google_Maps_API_Link(driver, urlSAN)
        rSAN = requests.get(linkSAN)
        print rSAN.status_code

        if  rSAN.status_code != 200:
            print 'LB San Fransisco Map Is Down'
            testcounter += 1

        # Minnesota
        urlMN = 'https://lb.511mn.org/mnlb/'
        linkMN = get_Google_Maps_API_Link(driver, urlMN)
        rMN = requests.get(linkMN)
        print rMN.status_code

        if  rSAN.status_code != 200:
            print 'LB Minnesota Map Is Down'
            testcounter += 1

        driver.quit()

        if testcounter > 0:
            assert False


if __name__ == '__main__':
    unittest.main()