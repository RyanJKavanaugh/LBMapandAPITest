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

class Verify_Idaho_Links(unittest.TestCase):

    def test_LB_Maps(self):

        testcounter = 0
        driver = webdriver.Chrome()

        # Idaho
        urlID = 'http://lb.511.idaho.gov/idlb/'
        driver.get(urlID)

        _inputsID = driver.find_elements_by_xpath('//img')
        for input in _inputsID:
            item = str(input.get_attribute('src'))
            if 'https://maps.googleapis.com/maps/api' in item:
                 print input.get_attribute('src')
                 linkID = input.get_attribute('src')

        rID = requests.get(linkID)
        print rID.status_code

        if  rID.status_code != 200:
            print 'LB Idaho Map Is Down'
          #  testcounter += 1


        # Louisiana
        urlLA = 'https://lb.511la.org/lalb/'
        driver.get(urlLA)
        inputsLA = driver.find_elements_by_xpath('//img')
        for input in inputsLA:
            item = str(input.get_attribute('src'))
            if 'https://maps.googleapis.com/maps/api' in item:
                 print input.get_attribute('src')
                 linkLA = input.get_attribute('src')

        rLA = requests.get(linkLA)
        print rLA.status_code

        if  rLA.status_code != 200:
            print 'LB Loisiana Map Is Down'
            testcounter += 1


        # Nebraska
        urlNE = 'https://lb.511.nebraska.gov/nelb/'
        driver.get(urlNE)
        inputsNE = driver.find_elements_by_xpath('//img')
        for input in inputsNE:
            item = str(input.get_attribute('src'))
            if 'https://maps.googleapis.com/maps/api' in item:
                 print input.get_attribute('src')
                 linkNE = input.get_attribute('src')

        rNE = requests.get(linkNE)
        print rNE.status_code

        if  rNE.status_code != 200:
            print 'LB Nebraska Map Is Down'
            testcounter += 1


        # Iowa
        urlIA = 'https://lb.511ia.org/ialb/'
        driver.get(urlIA)
        inputsIA = driver.find_elements_by_xpath('//img')
        for input in inputsIA:
            item = str(input.get_attribute('src'))
            if 'https://maps.googleapis.com/maps/api' in item:
                 print input.get_attribute('src')
                 linkIA = input.get_attribute('src')

        rIA = requests.get(linkIA)
        print rIA.status_code

        if  rIA.status_code != 200:
            print 'LB Iowa Map Is Down'
            testcounter += 1


        # Sacog
        urlSACOG = 'http://sa.carsstage.org/salbweb/'
        driver.get(urlSACOG)
        inputsSACOG = driver.find_elements_by_xpath('//img')
        for input in inputsSACOG:
            item = str(input.get_attribute('src'))
            if 'https://maps.googleapis.com/maps/api' in item:
                print input.get_attribute('src')
                linkSACOG = input.get_attribute('src')
        rSACOG = requests.get(linkSACOG)
        print rSACOG.status_code

        if  rSACOG.status_code != 200:
            print 'LB Sacramento Map Is Down'
            testcounter += 1


        # Sandag
        urlSAN = 'https://lbw.511sd.com/lbweb/'
        driver.get(urlSAN)
        inputsSAN = driver.find_elements_by_xpath('//img')
        for input in inputsSAN:
            item = str(input.get_attribute('src'))
            if 'https://maps.googleapis.com/maps/api' in item:
                print input.get_attribute('src')
                linkSAN = input.get_attribute('src')
        rSAN = requests.get(linkSAN)
        print rSAN.status_code

        if  rSAN.status_code != 200:
            print 'LB San Fransisco Map Is Down'
            testcounter += 1


        # Minnesota
        urlMN = 'https://lb.511mn.org/mnlb/'
        driver.get(urlMN)
        inputsMN = driver.find_elements_by_xpath('//img')
        for input in inputsMN:
            item = str(input.get_attribute('src'))
            if 'https://maps.googleapis.com/maps/api' in item:
                print input.get_attribute('src')
                linkMN = input.get_attribute('src')

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