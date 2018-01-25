from selenium import webdriver
import time
import re

NUM_CLASSES = 5

# eventually figure out how to safely store login data
url = 'https://bbcsulb.desire2learn.com/d2l/login'
chrome_path = 'C:/Users/Kelly/Desktop/webcrawler/chromedriver_win32/chromedriver'


# get username and password
sid = input('Enter your student id: ')
pw = input('Enter your password: ')

# create browser
browser = webdriver.Chrome(chrome_path)
browser.get(url)
time.sleep(4)
home_url = browser.current_url

# get page data
user = browser.find_element_by_id('userName')
pwrd = browser.find_element_by_id('password')
sbmt = browser.find_element_by_class_name('d2l-button')

# submit page data
user.send_keys(sid)
pwrd.send_keys(pw)
time.sleep(2)
sbmt.click()
time.sleep(5)

# go to view all courses
view_all_courses = browser.find_element_by_id('viewAllCourses')
view_all_courses.click()
time.sleep(5)

# get all a tags for my classes
classes = browser.find_elements_by_xpath('//*[@id="d2l-course-tile-anchor"]')
for i in range(NUM_CLASSES):
    curr_url = browser.current_url
    print('Current url: '+curr_url)

    class_href = classes[i].get_attribute('href')

    # get class name
    class_name_short = classes[i].text.split(' ', 2)
    print(class_name_short)
    print(class_href)

    #################################################
    # There is a problem where the browser doesn't
    # recognize the element I got after clicking
    # viewAllCourses. Figure out how to find the
    # correct elements from the home page, I'm
    # guessing this should fix the issue.
    #################################################

    browser.get(class_href)
    time.sleep(4)
    browser.back()
    print('after clicking back, url is: '+browser.current_url)

browser.close()
