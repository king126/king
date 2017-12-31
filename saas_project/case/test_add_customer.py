import  unittest
import time
from common.login_index import Login_And_Out
from selenium.webdriver.support.wait import WebDriverWait
class Add_Customer(unittest.TestCase):
    def add1(self):
        lao=Login_And_Out()
        driver=lao.login("15500000011","123456")
        WebDriverWait(driver, 50).until(lambda x: x.find_element_by_css_selector(".account.cd-popup-trigger6")).click()
        driver.find_element_by_xpath(".//*[@id='openAccount']/div/div/div[3]/div[1]/ul/li[1]/input").send_keys("haha")
        driver.find_element_by_xpath(".//*[@id='openAccount']/div/div/div[3]/div[1]/ul/li[2]/input").send_keys("154654545456")
        driver.find_element_by_xpath(".//*[@id='openAccount']/div/div/div[3]/div[1]/ul/li[4]/input[1]").click()
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_css_selector("#register-sub")).click()
        time.sleep(0.5)
        driver.find_element_by_css_selector(".layui-layer-btn0").click()
        time.sleep(1)
        # driver.quit()

add_cus=Add_Customer()
add_cus.add1()

if __name__ =="__main__":
    unittest.main()
