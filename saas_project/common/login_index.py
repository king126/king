from  selenium  import  webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
#driver = webdriver.Chrome()
#driver = webdriver.IE()
class Login_And_Out():
    def login(self,user,code):
        driver = webdriver.Firefox()
        driver.get("http://test.shopsys.ivymei.com/login")
        driver.implicitly_wait(30)
        driver.maximize_window()

        driver.find_element_by_xpath(".//*[@class='login-tab-warp']/li[2]").click()

        driver.find_element_by_xpath(".//*[@id='sms-module']/div[1]/input").send_keys(user)

        driver.find_element_by_xpath(".//*[@id='sms-module']/div[2]/input[2]").click()
        #这里有坑，弹窗的确定按钮，每次都会加1,下面使用css定位
        driver.find_element_by_css_selector(".layui-layer-btn0").click()

        driver.find_element_by_xpath(".//*[@id='sms-module']/div[2]/input[1]").send_keys(code)
        driver.find_element_by_xpath(".//*[@id='register']").click()

        t=driver.find_element_by_css_selector("#day-report").get_attribute("value")
        if t == "日结":
            print("首页登录成功")
        else:
            print("登录失败")
        return driver
    def  logout(self):
        # driver.find_element_by_css_selector(".LockLogin>li>span").click()
        driver.quit()
