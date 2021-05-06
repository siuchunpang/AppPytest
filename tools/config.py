import os

# devices = ["Android://127.0.0.1:5037/192.168.10.151:5555"]  # 连接安卓设备127.0.0.1:5037固定写法192.168.10.151安卓真机的Ip
devices = ["Android://"]
# devices = "Android://127.0.0.1:5037/192.168.10.130:5555"
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # pytest项目目录

snapShot_path = os.path.join(root_path, 'snapShot')  # 截图目录
test_path = os.path.join(root_path, 'testCase')  # 测试用例目录
air_log_path = os.path.join(test_path, 'airLog')  # airtest日志目录
air_report_path = os.path.join(test_path, 'airReport')  # airtest报告目录
log_path = os.path.join(root_path, 'log')  # 打印日志目录
report_path = os.path.join(root_path, 'testReport')  # 报告目录

camera_name = "4DKKPRO_0239E5CD0"
wifi_name = "test-5G"


