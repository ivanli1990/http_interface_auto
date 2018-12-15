# coding: utf-8
import xlrd
def getTestData(testDataFile, testScene, host, caseNo):
    '''
    从excel中获取测试数据
    :param testDataFile: 测试数据文件
    :param testScene: 测试场景
    :param host: 服务器主机
    :param caseNo: 用例No
    :param method: 请求方法
    :return: url，用例No，用例名称，请求参数，预期返回码，预期响应内容
    '''
    caseNo = int(caseNo)
    data = xlrd.open_workbook(testDataFile)
    table = data.sheet_by_name(testScene)
    cols = table.ncols

    resource_path = table.cell(1, 1).value  # 文件路径
    url = "http://" + host + resource_path  # 访问的url
    method = table.cell(2, 1).value  # 请求方法

    dict_params = {}
    for i in range(cols):
        dict_params[table.cell(3, i).value] = table.cell(caseNo+3, i).value

    caseNo = dict_params.pop("caseNo")
    caseName = dict_params.pop("caseName")
    expectCode = dict_params.pop("reponse_code")
    expectContent = dict_params.pop("expect_content")
    testName = "TestCase" + caseNo + "_" + caseName

    return method, url, caseNo, testName, dict_params, expectCode, expectContent

def getTestCaseNum(testDataFile, testScene):
    '''
    获取testScene测试场景中的测试用例数
    :param testDataFile: 测试数据文件
    :param testScene: 测试场景
    :return: 测试用例数
    '''
    data = xlrd.open_workbook(testDataFile)
    table = data.sheet_by_name(testScene)
    rows = table.nrows
    return rows-4

def getTestHttpMethod(testDataFile, testScene):
    '''
    获取testScene测试场景的请求方法
    :param testDataFile: 测试数据文件
    :param testScene: 测试场景
    :return: 请求方法
    '''
    data = xlrd.open_workbook(testDataFile)
    table = data.sheet_by_name(testScene)
    method = table.cell(2, 1).value  # 请求方法
    return method

if __name__ == "__main__":
    testDataFile = "E:\\llf_58TestSuites\\jz_webIntergration\\robot_code\\testData\\testData.xlsx"
    testScene = "getAreasByCityId"
    host = "jingzhun.58.com"
    method, url, caseNo, testName, dict_params, expectCode, expectContent = getTestData(testDataFile, testScene, host, 2)
    print(url)
    print(testName)
    # print(expectReuslt)