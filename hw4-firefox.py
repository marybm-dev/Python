'''
    Maria Martinez
    Spring '15
    Selenium Testing with Firefox
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# function to verify all elements in a list are unique
def unique_list(titlesList):
    titles = list()
    for title in titlesList:
        if title in titles: return False
        titles.append(title)
    return True

# function to check if queryText is found on the pageSource
def find_in_search(queryText, pageSource):
    return queryText in pageSource

# function to check that all results are true in a given list
def results_true(resultList):
    for result in resultList:
        if not result: return False
    return True

# class for test cases
class DirectReliefFirefoxTest(unittest.TestCase):
    
    # set up the driver needed for Selenium Firefox testing
    def setUp(self):
        self.driver = webdriver.Firefox()
    
    # test case goes to 5 different pages, collects page titles from title tags
    # calls unique_list function to verify that all 5 titles collected are unique
    def test_title_unique(self):
        pageTitles = list()
        pageURLs = ['http://www.directrelief.org', 'http://www.directrelief.org/focus/', 'http://www.directrelief.org/usa/', 'http://www.directrelief.org/international/', 'http://www.directrelief.org/emergency/' ]
        driver = self.driver
        # make an array of the page titles for these URLs
        for page in pageURLs:
            driver.get(page)
            title = driver.find_element_by_tag_name('title')
            pageTitles.append(title)

        # verify all page titles in the array are unique
        self.assertTrue(unique_list(pageTitles))

    # goes to fake page and verifies the page is not found
    def test_page_not_found(self):
        driver = self.driver
        driver.get('http://www.directrelief.org/about.html')
        # if page exists this fails, otherwise this passes since the page source will display "Page Not Found"
        assert "Page Not Found" in driver.page_source
    
    # test the search engine on this site
    def test_search_found(self):
        driver = self.driver
        driver.get('http://www.directrelief.org')
        # get the search box element to enter a search query
        searchBox = driver.find_element_by_name('s')
        searchBox.send_keys('latin')
        # hit return to perform search
        searchBox.send_keys(Keys.RETURN)
        resultLinks = driver.find_elements_by_xpath('//h3/a[@href]')
        # make a list to see if the word "latin" is found on the page
        found = list()
        # iterate through to check that at least 3 results contain "latin" on the page
        counter = 1
        for link in resultLinks:
            # store the original window
            window_before = driver.window_handles[0]
            newWindow = webdriver.ActionChains(driver)
            # open the link in a new window
            newWindow.key_down(Keys.SHIFT).click(link).key_up(Keys.SHIFT).perform()
            window_after = driver.window_handles[counter]
            WebDriverWait(self.driver,10)
            # add the results to the found array
            found.append(find_in_search('latin', driver.page_source))
            # return to the results page after a brief pause
            sleep(2)
            driver.switch_to_window(window_before)
            # increment the counter, exit after we've checked 3 pages
            counter += 1
            if counter > 3:
                break
        # if the word "latin" was not found then this test fails
        self.assertTrue(results_true(found))
    
    # test multi-word search found
    def test_search_multi_word_found(self):
        driver = self.driver
        driver.get('http://www.directrelief.org')
        # get the search box element to enter a search query
        searchBox = driver.find_element_by_name('s')
        searchBox.send_keys('latin america')
        # hit return to perform search
        searchBox.send_keys(Keys.RETURN)
        multiResultLinks = driver.find_elements_by_xpath('//h3/a[@href]')
        # make a list to see if the word "latin" is found on the page
        foundMulti = list()
        # iterate through each page to check
        counter = 1
        for multiLink in multiResultLinks:
            # store the original window
            window_before = driver.window_handles[0]
            newWindow = webdriver.ActionChains(driver)
            # open the link in a new window
            newWindow.key_down(Keys.SHIFT).click(multiLink).key_up(Keys.SHIFT).perform()
            window_after = driver.window_handles[counter]
            WebDriverWait(self.driver,10)
            foundMulti.append(find_in_search('latin america', driver.page_source))
            # return to the results page after a brief pause
            sleep(2)
            driver.switch_to_window(window_before)
            # increment the counter, exit after we've checked 3 pages
            counter += 1
            if counter > 3:
                break
        # if the words "latin america" were found then this test does not fail
        self.assertTrue(results_true(foundMulti))
    
    # test search result not found
    def test_search_not_found(self):
        driver = self.driver
        driver.get('http://www.directrelief.org')
        # get the search box element to enter a search query
        searchBox = driver.find_element_by_name('s')
        searchBox.send_keys('Kardashian')
        # hit return to perform search
        searchBox.send_keys(Keys.RETURN)
        # if the search query returns no results then page will display "Didn't find what you were looking for?"
        assert "Didn't find what you were looking for?" in driver.page_source
    
    # close the driver
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


