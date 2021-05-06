[框架描述]
1.启动main.py
2.Pytest会先找pytest.ini，确定启动参数
3.根据pytest.ini，找到测试用例集文件夹
4.按照文件名a-z的顺序执行测试用例
5.每个测试用例先执行auto_setup方法，然后在testCase文件夹的airLog创建airtest报告所需要的图片和log文件
6.每个测试用例执行途中，会把步骤生成并记录在log文件夹的log文件内，若执行出错，会保留截图在snapShot文件夹
7.每个用例执行完毕，会执行pytest配置文件conftest.py的simple_report方法，根据airLog文件在airReport生成airtest报告
8.待所有用例执行完毕后，在testReport生成pytest报告


[用例排序]
1XX：已连相机时执行的用例
1XXX：未连相机时执行的用例


