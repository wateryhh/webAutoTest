import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
CONFIG_DIR = os.path.join(BASE_DIR,"config","config.ini")
# 测试用例目录
TEST_DIR = os.path.join(BASE_DIR,"testCase")
# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR,"testReport")
# 日志目录
LOG_DIR = os.path.join(BASE_DIR,"logs")
# 测试数据文件
TEST_DATA_YAML = os.path.join(BASE_DIR,"testData")
# 元素控件
TEST_Element_YAML = os.path.join(BASE_DIR,"testYaml")
