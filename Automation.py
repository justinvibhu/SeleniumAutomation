from Screenshot import Screenshot
from selenium import webdriver
import time

ob = Screenshot.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot/tree/master/test"
driver.get(url)
# img_url = ob.full_screenshot(driver, save_path=r'.//Screenshot', image_name='myimage.png', is_load_at_runtime=True,
#                                           load_wait_time=3)

driver.get_screenshot_as_file("Screenshot//Scrscreenshot1.png")
time.sleep(2)



#   url 2
# print(img_url)
# hide_elements = ['class=position-relative js-header-wrapper ']
url2 = "https://www.google.com/"
driver.get(url2)
# img_url = ob.full_screenshot(driver, save_path=r'.//Screenshot', image_name='myimage2.png', is_load_at_runtime=True,
#                                             hide_elements=hide_elements,)

driver.get_screenshot_as_file("Screenshot//Scrscreenshot2.png")
driver.close()

driver.quit()