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
        urlID = 'http://crc-prod-id-wf-elb-382957924.us-west-2.elb.amazonaws.com/idlb/'
        driver.get(urlID)
        mapIdaho = driver.find_element_by_xpath("//*[@id='j_idt141']/img")
        linkID = mapIdaho.get_attribute('src')

        rID = requests.get(linkID)
        print rID.status_code

        if  rID.status_code != 200:
            print 'LB Idaho Map Is Down'
          #  testcounter += 1

        # Louisiana
        urlLA = 'https://lb.511la.org/lalb/'
        driver.get(urlLA)
        mapLA = driver.find_element_by_xpath('//*[@id="j_idt155"]/img')
        linkLA = mapLA.get_attribute('src')

        rLA = requests.get(linkLA)
        print rLA.status_code

        if  rLA.status_code != 200:
            print 'LB Loisiana Map Is Down'
            testcounter += 1

        # Nebraska
        urlNE = 'https://lb.511.nebraska.gov/nelb/'
        driver.get(urlNE)
        mapNE = driver.find_element_by_xpath('//*[@id="j_idt346"]/img')
        linkNE = mapNE.get_attribute('src')

        rNE = requests.get(linkNE)
        print rNE.status_code

        if  rNE.status_code != 200:
            print 'LB Nebraska Map Is Down'
            testcounter += 1

        # Iowa
        urlIA = 'https://lb.511ia.org/ialb/'
        driver.get(urlIA)
        mapIA = driver.find_element_by_xpath('//*[@id="j_idt383"]/img')
        linkIA = mapIA.get_attribute('src')

        rIA = requests.get(linkIA)
        print rIA.status_code

        if  rIA.status_code != 200:
            print 'LB Iowa Map Is Down'
            testcounter += 1

        # Sacog
        urlSACOG = 'http://sa.carsstage.org/salbweb/'
        driver.get(urlSACOG)
        mapSACOG = driver.find_element_by_xpath('//*[@id="j_idt122"]/img')
        linkSACOG = mapSACOG.get_attribute('src')

        rSACOG = requests.get(linkSACOG)
        print rSACOG.status_code

        if  rSACOG.status_code != 200:
            print 'LB Sacramento Map Is Down'
            testcounter += 1

        # Sandag
        urlSAN = 'https://lbw.511sd.com/lbweb/'
        driver.get(urlSAN)
        mapSAN = driver.find_element_by_xpath('//*[@id="j_idt150"]/img')
        linkSAN = mapSAN.get_attribute('src')

        rSAN = requests.get(linkSAN)
        print rSAN.status_code

        if  rSAN.status_code != 200:
            print 'LB San Fransisco Map Is Down'
            testcounter += 1

        # Minnesota
        urlMN = 'https://lb.511mn.org/mnlb/'
        driver.get(urlMN)
        #imageWait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='j_idt369']/img")))
        try:
            mapMN = driver.find_element_by_xpath('//*[@id="j_idt166"]/img')
        except:
            try:
                mapMN = driver.find_element_by_xpath('//*[@id="j_idt368"]/img')
            except:
                try:
                    mapMN = driver.find_element_by_xpath('//*[@id="j_idt365"]/img')
                except:
                    pass

        linkMN = mapMN.get_attribute('src')

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