from selenium import webdriver
import time
import sys


# Get the URL from command line argument
url = sys.argv[1]
# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get(url)
time.sleep(20)


# Validate the title
#expected_title = ""
actual_title = driver.title
print (" le titre est :", actual_title)

#if expected_title == actual_title:
    #print("Title validation successful!")
#else:
    #print("Title validation failed. Expected:", expected_title, "Actual:", actual_title)
time.sleep(10)
# Close the browser
driver.quit()


#java -jar jenkins.war --httpPort=8084
