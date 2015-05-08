import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
    
#1 function to take list of numbers low and high
def lowHigh(list, low, high):
    for index in range(len(list)):
        if list[index] <= high and list[index] >= low:
            return True
    return False
myList = [1,4,8,2,9]
print lowHigh(myList, 2, 10) 


#2 function used in test case
def contains(list, value):
    for index in range(len(list)):
        if list[index] == value:
            return True
    return False

#2 Python Test cases
class MidtermStudy(unittest.TestCase):
    def testContains1(self):
        self.assertTrue(contains(['a','b','c'], 'a'))
    def testContains2(self):
        self.assertFalse(contains([2,4,6,8], 1))
        
# run tests
if __name__ == '__main__':
    unittest.main()
    
#3 Robot Test cases
# *** Variables ***
# ${RESULT}
#
# *** Test Cases ***
#
# HasOld
#     ${RESULT}=          Evaluate            'abracadabra'.replace('ab','oak')
#     Should Match        ${RESULT}           'oakracadoakra'
#
# DoesNotHaveOld
#     ${RESULT}=          Evaluate            'cat'.replace('u','v')
#     Should Match        ${RESULT}           'cat'

#4 Selenium Test
class SeleniumTesting(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def testingEon(self):
        driver = self.driver
        driver.get('www.testpage.com')
        try:
            home = driver.find_element_by_id('home')
            driver.send_keys('Hayward')
            driver.send_keys(Keys.RETURN)
            assert 'Eon Coffee' in driver.page_source
        except NoSuchElementException:
            fail("element not found")
        try:
            location = driver.find_element_by_id('location')
        except NoSuchElementException:
            fail("element not found")
    
    def tearDown(self):
        self.driver.quit()