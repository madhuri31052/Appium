from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
  
user = os.environ.get("BROWSERSTACK_USER")
key = os.environ.get("BROWSERSTACK_KEY")

desired_cap = {
    # Set your access credentials
    "browserstack.user": user,
    "browserstack.key": key,
    # Set URL of the application under test
    "app" : "bs://b564466666387a44affcd8f6f4acd61a265f3880",
  
    # Specify device and os_version for testing
    "device" : "Google Pixel 5",
    "os_version" : "10.0",
      
    # Set other BrowserStack capabilities
    "project" : "dock test", 
    "build" : "browserstack-build-1",
    "name" : "dock_test"
}
  
# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_cap
)

print("Entered")

# Click on Next button
search_element1 = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, 
 "com.strongarmtech.dockv5app:id/nextButton"))
 )
search_element1.click()

# Click on Begin button
search_element2 = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, 
 "com.strongarmtech.dockv5app:id/nextButton"))
 )
search_element2.click()

# # Click on Next button
# search_element3 = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ID, 
#  "com.strongarmtech.dockv5app:id/next"))
#  )
# search_element3.click()


#com.strongarmtech.dockv5app:id/dns_test_message
# # Tap hamburger sign
# search_element1 = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ID, 
# "com.strongarmtech.dockv5app:id/menuIcon"))
# )
# search_element1.click()

# # Click on diagnostics button
# search_element2 = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ID, 
# "com.strongarmtech.dockv5app:id/sidebarDiagnosticsBtn"))
# )
# search_element2.click()
  
# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()

print("Success")