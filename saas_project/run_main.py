# coding:utf-8
import unittest
import HTMLTestRunner
import os
import time

def all_case(case="case"):
    '''加载指定目录下的所有的用例'''
    # 待执行用例的目录
    # case_dir = "D:\\test\\jiekou\\testcase"
    case_dir = os.path.join(os.getcwd(), case)
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到testcase
            testcase.addTests(test_case)
    print (testcase)
    return testcase


if __name__ == "__main__":

    # runner = unittest.TextTestRunner()
    # runner.run(all_case())

    # 报告的路径
    nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(os.getcwd(), "report", nowtime+".html")
    print(report_path)
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'这是接口自动化测试报告',
                                           description=u'用例执行情况：')

    runner.run(all_case())
    fp.close()
