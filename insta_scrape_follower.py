from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from getpass import getpass
import time
import csv
import os
import wget

# enter your username and password
enter_user = input("enter your instagram username")
enter_pass = getpass()

# opening url
driver = webdriver.Chrome('') # you will enter you web driver path here
driver.get('https://instagram.com')

# creating a function for timesleep
def timesleep(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}'.format(secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        print("wait", t, " seconds")
    print("done")

timesleep(10)

# finding username and password input fields
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# sending the names into the input field in instagram
username.send_keys(enter_user)
password.send_keys(enter_pass)

# finding button login
login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# wait for 10 seconds after clicking login button
timesleep(10)

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

timesleep(5)

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

timesleep(1)
print("you are now logged in")

# input username to scrape their followers
print("enter username to be scraped")
searchusername = input()

print("how many of their followers data you want to scrape")
num_f = int(input())

# constructing url from inputed field inorder to scrape the followers
consurl = "https://instagram.com/" + searchusername
driver.execute_script(f'''window.open("{consurl}", "_blank");''')
driver.close()

driver.switch_to.window(driver.window_handles[0])

timesleep(10)

ul = driver.find_element_by_class_name("k9GMp")
li = ul.find_elements_by_tag_name("li")
li[1].click()

timesleep(3)

# followers container
fc = driver.find_element_by_class_name("PZuss")

# get each follower
ef = fc.find_elements_by_tag_name("li")


# loop through each followers and scrape their data and return back finally save it to .csv file
lists = []

for i in ef[0:num_f]:
    i = i.find_element_by_class_name("MqpiF")
    temp_username = i.text
    construct_url = "https://instagram.com/" + i.text
    driver.execute_script(f'''window.open("{construct_url}", "_blank");''')
    driver.switch_to.window(driver.window_handles[1])
    timesleep(10)
    ul = driver.find_element_by_class_name("k9GMp")
    li = ul.find_elements_by_tag_name("li")
    number = li[1].find_element_by_class_name("g47SY")
    dict = {"username":temp_username, "followers":number.text}
    lists.append(dict)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

with open('data.csv', 'w', newline='') as file:
    fieldnames = ['username', 'followers']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(lists)):
        writer.writerow(lists[i])

close = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]")
close.click()

images_container = driver.find_element_by_class_name("ySN3v")
first_row = images_container.find_element_by_class_name("Nnq7C")
images = first_row.find_elements_by_tag_name("img")

path = os.getcwd()
path = os.path.join(path, searchusername)
os.mkdir(path)

counter = 0
for i in range(len(images)):
    save_as = os.path.join(path, str(counter) + '.jpg')
    image = images[i].get_attribute('src')
    wget.download(image, save_as)
    counter += 1
