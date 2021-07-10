# Instagram Followers Scraper

This project is created with python programming language.

I used Selenium to automate the web and chrome web driver.

## Requirements
1. you must install the necessary libraries like selenium before you run this project. you can use ```pip install selenium```
2. you must download chrome web driver from https://chromedriver.chromium.org/downloads

## After you run the project
1. you will enter your instagram username and password(use dummy account instead of you actual account)
2. then it will ask you which username of instagram you want to scrape and provide only their username. EG. (therock)
3. you will be asked how many number of their followers you want to scrape. you can enter the amount you want. EG(250)

After this it will go through every follower of the username you entered and scrape their username and their followers too and store it in a csv file.

Below there is sample scraped data from followers of kevinhart4real

![insta_scraped_followers_data](https://user-images.githubusercontent.com/65722317/125164242-e5685d00-e199-11eb-9696-2194c05feba4.PNG)

Not only this, but it also downloads the lates 3 images of the username, and creates a folder in their name and puts thier photos in that folder.
