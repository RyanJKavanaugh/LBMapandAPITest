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


display = Display(visible=0, size=(800, 800))
display.start()

# Function to access Agency LB Website and retrieve Google Maps API link
def Get_Google_Maps_API_Link(driver, url):
    try:
        # Access web page
        # test item77
        #print url
        driver.get(url)
        # Gather all elements that have an img tag
        _inputs = driver.find_elements_by_xpath('//img')
        # Print page title for easy reference and review
        print driver.title
        # Loop through all img web elements and find element holding the Google API Link
        for input in _inputs:
            item = str(input.get_attribute('src'))
            #print item
            if '://maps.googleapis.com/maps/api' in item:
                # Return the Google API link
                #return input.get_attribute('src')
                # print 'API Link'
                # print item
                return item
    except Exception as e:
        print url
        print "The site is faulty"


# Function to get the status code for an API request, given the proper link
def Get_Status_code(apiLink):
    try:
        apiRequest = requests.get(apiLink)
        statusCode = apiRequest.status_code
        print statusCode
        return statusCode
    except Exception as e:
        print e
        print
        print apiLink
        print "The API call is faulty"


class Verify_LB_Web_Maps(unittest.TestCase):


    def test_LB_Maps(self):
        driver = webdriver.Chrome()
        testcounter = 0

        # Idaho LB Web Test ( With comments that apply for each of the following agencies)
        urlID = 'http://lb.511.idaho.gov/idlb/'
        # Get Map link that connects with Google API
        apiLink = Get_Google_Maps_API_Link(driver, urlID)
        # Get the status of the request to the Google API
        statusCodeID = Get_Status_code(apiLink)

        # If the map is down, then the test will fail and trigger an email in Jenkins
        if  statusCodeID != 200:
            print 'LB Idaho Map Is Down'
            testcounter += 1


        # Louisiana
        urlLA = 'https://lb.511la.org/lalb/'
        linkLA = Get_Google_Maps_API_Link(driver, urlLA)
        statuscodeLA = Get_Status_code(linkLA)

        if statuscodeLA != 200:
            print 'LB Loisiana Map Is Down'
            testcounter += 1


        # Nebraska
        urlNE = 'https://lb.511.nebraska.gov/nelb/'
        linkNE = Get_Google_Maps_API_Link(driver, urlNE)
        statuscodeNE = Get_Status_code(linkNE)

        if  statuscodeNE != 200:
            print 'LB Nebraska Map Is Down'
            testcounter += 1


        # Iowa
        urlIA = 'https://lb.511ia.org/ialb/'
        linkIA = Get_Google_Maps_API_Link(driver, urlIA)
        statuscodeIA = Get_Status_code(linkIA)

        if  statuscodeIA != 200:
            print 'LB Iowa Map Is Down'
            testcounter += 1


        # Sacog
        urlSACOG = 'https://lb.riverregion511.org/salb/'
        linkSACOG = Get_Google_Maps_API_Link(driver, urlSACOG)
        statuscodeSACOG = Get_Status_code(linkSACOG)

        if  statuscodeSACOG != 200:
            print 'LB Sacramento Map Is Down'
            testcounter += 1


        # Sandag
        urlSAN = 'https://lbw.511sd.com/lbweb/'
        linkSAN = Get_Google_Maps_API_Link(driver, urlSAN)
        statuscodeSAN = Get_Status_code(linkSAN)

        if  statuscodeSAN != 200:
            print 'LB San Fransisco Map Is Down'
            testcounter += 1


        # Minnesota
        urlMN = 'https://lb.511mn.org/mnlb/'
        linkMN = Get_Google_Maps_API_Link(driver, urlMN)
        statuscodeMN = Get_Status_code(linkMN)

        if  statuscodeMN != 200:
            print 'LB Minnesota Map Is Down'
            testcounter += 1


        driver.quit()


        if testcounter > 0:
            assert False


if __name__ == '__main__':
    unittest.main()