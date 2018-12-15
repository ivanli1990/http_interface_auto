# coding: utf-8
import pymysql
import json

class ReadConfig(object):

    def __init__(self):
        '''
        ecomqadb信息
        '''
        self.host = '10.9.193.32'
        self.port = 3306
        self.user = 'work'
        self.passwd = '123456'
        self.db = 'ecomqa'

    def getConfig(self, test_service):
        '''
        读取db中的配置数据
        :param test_service: 测试服务在db中test_service字段中的值
        :return: dict形式的配置数据
        '''
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db, charset='utf8')
        cur = conn.cursor()
        sql = "select * from t_jingzhun_interfaces_testData t where t.test_method = 'get'"
        cur.execute(sql)
        raw = cur.fetchall()
        cur.close()
        conn.close()
        # print(raw[0])
        config_data = json.loads(raw[0][6])
        return config_data

if __name__ == "__main__":
    rc = ReadConfig()
    print(rc.getConfig("lego_scf_adplatform_config"))