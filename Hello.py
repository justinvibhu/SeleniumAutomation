# import time

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from PIL import Image
# from Screenshot import Screenshot





# # class driver:
# #     driver, service= None, None
    

# #     def __init__(self, driver:str):
# #         self.service =Service(driver)
# #         self.driver =webdriver.Chrome(service=self.service)

# # # url - open
# #     def open_page(self, url:str):
# #         self.driver.get(url) 
# # # url -close
# #     def close_driver(self):
# #         self.driver.close()


# if __name__=='__main__':
    
    
#     ob = Screenshot.Screenshot()
#     # driver =driver( "C:\Users\Admin\OneDrive\Desktop\Automation\driver\chromedriver.exe")
#     driver =driver( "driver\\chromedriver.exe")
#     driver.open_page("https://www.google.com/")
#     screen_shot =  ob.full_screenshot(driver, save_path= "C:\\Users\\Admin\\OneDrive\\Desktop\\Automation\\Screenshot", image_name='myimage.png', is_load_at_runtime=True,
#                                           load_wait_time=9)
#     screen = Image.open(screen_shot)
#     print(driver.get_window_size())
#     screen.show()
#     time.sleep(10)
#     # driver.open_page("https://www.youtube.com/")
#     # driver.save_screenshot("ss.png")
#     # screenshot = Image.open("ss.png")  
#     # screenshot.show()
#     # time.sleep(4)

#     driver.close()

#     driver.quit()