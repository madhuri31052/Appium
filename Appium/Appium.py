from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
# import os
# os.system("start /B start cmd.exe @cmd /k appium")

dep_caps = {
    "appium:deviceName": "sdk_gphone_x86",
    "platformName": "Android",
    "appium:version": "10",
    "app": "/Users/Madhuri/Downloads/DockAppV5-3.1.0-Aug-18-2022-06-38-generic-staging-debug.apk",
    "appium:appPackage": "com.strongarmtech.dockv5app",
    "appium:appActivity": "com.strongarmtech.dockv5app.athlete.AthleteListActivity",
    "appium:automationName": "UiAutomator2"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dep_caps)
time.sleep(8)

action = ActionChains(driver)
actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
gesture = actions.pointer_action

# Scroll-down
gesture.move_to_location(475, 1417).pointer_down().move_to_location(475, 605).release()
actions.perform()
time.sleep(2)

# Scroll-up
gesture.move_to_location(494, 542).pointer_down().move_to_location(466, 1486).release()
actions.perform()
time.sleep(2)

# Tap hamburger sign
driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='hamburger menu icon']").click()
time.sleep(2)

# Click on diagnostics button
driver.find_element(AppiumBy.ID, "com.strongarmtech.dockv5app:id/sidebarDiagnosticsBtn").click()
time.sleep(2)

# Long press on "Enter Full Name"
gesture.move_to_location(60, 860).pointer_down().pause(3).release()
actions.perform()
time.sleep(2)

# Paste the copied Name
gesture.move_to_location(50, 790).pointer_down().pause(0.1).release()
actions.perform()
time.sleep(2)

driver.quit()

# os.system("taskkill /F /IM cmd.exe")

print("Successful")
