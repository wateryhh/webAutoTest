import configparser
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
import yaml,json

class ReadFile:
    def readConfig(self,key,param):
        configfile = setting.CONFIG_DIR
        config = configparser.ConfigParser()
        config.read(configfile, encoding="utf8")
        return config.get(key,param)

    def readYaml(self,yamlfile_path):
        try:
            f = open(yamlfile_path,encoding='utf-8')
            data =yaml.load(f, Loader=yaml.FullLoader)
            f.close()
            return data
        except Exception as msg:
            print("异常消息-> {0}".format(msg))

if __name__ == '__main__':
    test = ReadFile()
    element = test.readYaml(setting.TEST_DATA_YAML + '/' + 'login_data.yaml')
    print(element[1]['data'])
