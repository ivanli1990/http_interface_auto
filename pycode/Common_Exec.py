# coding: utf-8
import requests
import os
import time

def batch_Call(robot_testSuite, robot_testCase, testScene, caseNum, testCaseReportPath, execTime):
    '''
    批量执行testScene测试场景下的用例
    :param robot_testSuite: robot testSuite路径
    :param robot_testCase: robot testCase路径
    :param testScene: 测试场景
    :param caseNum: 用例数
    :param testCaseReportPath: 业务用例测试报告路径
    :param execTime: 执行时间
    :return:
    '''
    try:
        for caseNo in range(caseNum):
            testCase = ""
            caseNo = caseNo + 1
            testName = "testcase" + "_" + str(caseNo)
            output_dir = "-d " + testCaseReportPath + "/result_{0}".format(testScene)  # 输出目录
            output_xml = "-o output_{0}_{1}.xml".format(testName, execTime)
            output_log = "-l log_{0}_{1}.html".format(testName, execTime)
            output_report = "-r report_{0}_{1}.html".format(testName, execTime)
            variable = "-v caseNo:" + str(caseNo) + " -v testScene:" + testScene
            testCase = "--test " + robot_testCase
            pybot_cmd = "pybot " + output_dir + " " + output_xml + " " + output_log + " " + output_report + " " + variable + " " +  " " + testCase + " " + robot_testSuite
            os.system(pybot_cmd)  # 执行pybot命令
        return "done"
    except Exception as e:
        return "Error: " + str(e)

def send_HttpRequest(url, data=None, headers=None, method=None):
    '''
    发送http请求
    :param url: 请求的url
    :param data: 请求数据
    :param headers: 请求头
    :param method: 请求方法
    :return: 响应码，响应内容
    '''
    if method == "get":
        response = requests.get(url, data, headers=headers)
    if method == "post":
        response = requests.post(url, data, headers=headers)
    code = str(response.status_code)
    content = response.content.decode("utf-8")  # 转码
    return code, content

def cleanLogs(testScene, testCaseReportPath):
    '''
    删除硬盘中合并前的测试报告
    :param testScene: 测试场景
    :param testCaseReportPath: 业务用例测试报告路径
    :return:
    '''
    testCaseReportPath = testCaseReportPath + "/result_{0}".format(testScene)
    report_files = testCaseReportPath + "/report_testcase*"
    xml_files = testCaseReportPath + "/output_testcase*"
    log_files = testCaseReportPath + "/log_testcase*"
    cmd = "del " + report_files + " " + xml_files + " " + log_files  # windows
    cmd = cmd.replace("/", "\\")
    print(cmd)
    os.system(cmd)

def getCurtime():
    '''
    获取当前时间
    :return: 当前时间
    '''
    return time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))

def mergeReport(testScene, testCaseReportPath, execTime):
    '''
    # 合并报告
    :param testScene: 测试场景
    :param testCaseReportPath: 业务用例测试报告路径
    :param execTime: 执行时间
    :return:
    '''
    try:
        output_dir = "-d " + testCaseReportPath + "/result_{0}".format(testScene)  # 输出目录
        output_xml = "-o output_{0}.xml".format(execTime)
        output_log = "-l log_{0}.html".format(execTime)
        output_report = "-r report_{0}.html".format(execTime)
        # 被合并的报告
        merge_report = testCaseReportPath + "/result_{0}".format(testScene) + "/output_testcase_*.xml"
        name = "--name " + testScene
        rebot_cmd = r"rebot " + output_dir + " " + output_xml + " " + output_log + " " + output_report + " " + name + " "  + merge_report
        os.system(rebot_cmd)  # 执行rebot命令
        return "done"
    except Exception as e:
        return "Error: " + str(e)

if __name__ == "__main__":
    robotTestCase = "sendPostRequest"
    robotTestSuite = r"E:/llf_58TestSuites/jz_webIntergration/robot_code/rfcode/send_Request.txt"
    testScene = "weather"
    testDataFile = "E:\\llf_58TestSuites\\jz_webIntergration\\robot_code\\testData\\testData.xlsx"
    testCaseReportPath = "E:\\llf_58TestSuites\\jz_webIntergration\\robot_code\\report\\TestCaseReport"

    # mergeReport(testScene, testCaseReportPath, getCurtime())
    # cleanLogs(testScene, testCaseReportPath)