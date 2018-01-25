from selenium import webdriver
import time


# eventually figure out how to safely store login data
url = 'https://bbcsulb.desire2learn.com/d2l/login'
chrome_path = 'C:/Users/Kelly/Desktop/webcrawler/chromedriver_win32/chromedriver'

# get username and password
sid = input('Enter your student id')
pw = input('Enter your password')

# create browser
browser = webdriver.Chrome(chrome_path)
browser.get(url)
time.sleep(4)

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

# THEA 113
#thea_113_button= browser.find_element_by_id('d2l-course-tile-anchor')
#thea_113_button.click()
#time.sleep(3)

################################################
# I left off trying to click each of the classes
# but was having trouble finding the right
# element to click
################################################

# idea: try just getting the url instead

# get all a tags
classes = browser.find_elements_by_xpath('//*[@id="d2l-course-tile-anchor"]')
for link in classes:
    class_href = link.get_attribute('href')
    print(class_href)
    print(link.text)

browser.close()
