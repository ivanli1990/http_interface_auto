# coding: utf-8
from Common_Exec import send_HttpRequest
from Common_Excel import getTestData
import requests
import json
if __name__ == "__main__":
    host = "jingzhunapi.58.com"
    headers = {
        "Host": "jingzhunapi.58.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Cookie": "xxzl_smartid=2ddb661398f076ef8db614da337f86d4; xxzl_deviceid=ooBYtJKAdzasgZl56eYV0VvqK%2F7zyHVdTlrph3t4UPPFgvjMXs%2FISGaWbi6eOYrR; id58=c5/nn1pv6TZlB5V7EPwSAg==; 58tj_uuid=f68dbc5f-5fd7-4929-b679-8d38f87d9e78; new_uv=8; als=0; commontopbar_myfeet_tooltip=end; gr_user_id=63d98d59-a7a1-41e4-9566-a5bffe4c1178; wmda_uuid=c17ae05ab58018530c5386f36224aeb0; wmda_new_uuid=1; wmda_visited_projects=%3B1731918550401; bj58_new_uv=2; bj58_id58s=\"RFpBLVBMSjRTTE9SMTgyNw==\"; 58home=bj; city=bj; ppStore_fingerprint=AA917BD17BA3D8C2544DC36E095FF2B337E8D2FD565220C6%EF%BC%BF1517543037529; PPU=\"UID=8990825076743&UN=jingzhun02&TT=d87326d3c8b6fc172798d8526f38ff0b&PBODY=YC9qy5ZDNowi2JCw5PEACk_s5DpSnmn_lGuMyHLRGAvTYt3Ct1Ekyq_7Pwhjt17gf6-1o5jo-Sgevc7x1D1jAX_FeC08F5XY7PQt7Wo03432gqquMD0ws3bcYChuqpc-1wSgfve7ML6Uy3nBlzXivlnr_p1V5u5AQmJdJFUrJyc&VER=1\"; 58cooper=\"userid=8990825076743&username=jingzhun02&cooperkey=38f642dd686d15e197dc4f7cf56e5335\"; www58com=\"AutoLogin=false&UserID=8990825076743&UserName=jingzhun02&CityID=0&Email=&AllMsgTotal=0&CommentReadTotal=0&CommentUnReadTotal=0&MsgReadTotal=0&MsgUnReadTotal=0&RequireFriendReadTotal=0&RequireFriendUnReadTotal=0&SystemReadTotal=0&SystemUnReadTotal=0&UserCredit=0&UserScore=0&PurviewID=&IsAgency=false&Agencys=null&SiteKey=1FC200CCC2CA2C7E95CA48D9A4651279CD7202596549E849D&Phone=&WltUrl=&UserLoginVer=4E2D7FDC8FC54575837CD36CC3F448598&LT=1517543037936\"; vip=masteruserid%3D8990825076743%26vipkey%3D82871afe94f6b3ab7c5226436c97c019%26vipusertype%3D0; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; commontopbar_ipcity=bj%7C%E5%8C%97%E4%BA%AC%7C0; new_session=0; utm_source=; spm=; init_refer=",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
    }
    robotTestCase = "sendPostRequest"
    robotTestSuite = r"E:/llf_58TestSuites/jz_webIntergration/robot_code/rfcode/send_Request.txt"
    testScene = "getSecondCatesByFirstCateId"
    testDataFile = "E:\\llf_58TestSuites\\jz_webIntergration\\robot_code\\testData\\testData.xlsx"
    # testCaseReportPath = "E:\\llf_58TestSuites\\jz_webIntergration\\robot_code\\report\\TestCaseReport"
    method, url, caseNo, testName, dict_params, expectCode, expectContent = getTestData(testDataFile, testScene, host, 1)
    code, content = send_HttpRequest(url, dict_params, headers, method=method)
    content = json.loads(content)
    print(content["code"])
    print(content["msg"])
    print(content["errorcode"])
    print(content["data"])


