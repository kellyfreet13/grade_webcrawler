from selenium import webdriver
import time

# eventually prompt user in window
url = 'https://bbcsulb.desire2learn.com/d2l/login'
chrome_path = './chromedriver_win32/chromedriver'

# get username and password
sid = input('Enter your student id: ')
pw = input('Enter your password: ')

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

# get all a tags for my classes
classes = browser.find_elements_by_xpath('//*[@id="d2l-course-tile-anchor"]')
print('Amount of classes: '+str(len(classes)))

# get an array of href so there is no 'stale' element. The hrefs
# will remain the same even though an element may be reloaded
class_urls = []
class_names = []
for my_class in classes:
    class_urls.append(my_class.get_attribute('href'))

    # get class name
    class_name_split = my_class.text.split(' ', 2)
    class_name_short = class_name_split[0] + ' ' + class_name_split[1]
    class_names.append(class_name_short)

# navigate to each class
for url in class_urls:
    time.sleep(3)
    browser.get(url)
    time.sleep(3)

    # navigate to grades for each page
    nav_items = browser.find_elements_by_class_name('d2l-navigation-s-link')
    for item in nav_items:
        if item.text == 'Grades':
            grade_url = item.get_property('href')

    # navigate to the grades section
    browser.get(grade_url)


for name in class_names:
    print(name)

browser.close()
