# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


@pytest.mark.run(order=1003)
def test_share(ini):
    try:
        connect_wifi()
        """登录账号"""
        poco(name="com.fdage.eight:id/iv_my").click()
        sleep(2.0)
        poco(name="com.fdage.eight:id/tv_user_name").click()
        sleep(1.5)
        poco(name="com.fdage.eight:id/et_phone").set_text("")
        sleep(1.5)
        poco(name="com.fdage.eight:id/et_phone").set_text("13138102395")
        sleep(2.0)
        poco(name="com.fdage.eight:id/et_password").set_text("")
        sleep(1.5)
        poco(name="com.fdage.eight:id/et_password").set_text("Mo970325")
        sleep(2.0)
        poco(name="com.fdage.eight:id/btn_login").click()
        sleep(3.0)
        account = poco("com.fdage.eight:id/tv_user_accout").attr("text")
        try:
            assert_equal(account, "账号:13138102395", "登录账号13138102395")
            logging.info("登录成功")
        except AssertionError:
            logging.info("登录失败")
        sleep(3.0)

        """分享场景-微信"""
        poco("com.fdage.eight:id/iv_scene_cloud").click()
        sleep(5.0)
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.fdage.eight:id/frag_container").offspring("com.fdage.eight:id/rcv_scene").child(
            "com.fdage.eight:id/root_item")[0].child("com.fdage.eight:id/iv_menu").click()
        sleep(1.5)
        poco("com.fdage.eight:id/tv_option", text="分享").click()
        sleep(1.5)
        poco("com.fdage.eight:id/iv_wx")[0].click()
        sleep(5.0)
        poco("com.tencent.mm:id/gbv").click()
        sleep(2.0)
        poco("com.tencent.mm:id/doz", text="分享").click()
        sleep(1.0)
        poco("com.tencent.mm:id/ayl", text="已发送").wait_for_appearance(10)
        sleep(1.0)
        poco("com.tencent.mm:id/dom", text="返回四维看看Pro").click()

        """分享场景-朋友圈"""
        poco("com.fdage.eight:id/iv_scene_cloud").click()
        sleep(5.0)
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.fdage.eight:id/frag_container").offspring("com.fdage.eight:id/rcv_scene").child(
            "com.fdage.eight:id/root_item")[0].child("com.fdage.eight:id/iv_menu").click()
        sleep(1.5)
        poco("com.fdage.eight:id/tv_option", text="分享").click()
        sleep(1.5)
        poco("com.fdage.eight:id/iv_wx_timeline")[0].click()
        sleep(5.0)
        poco("com.tencent.mm:id/ch", text="发表").click()
        sleep(5.0)

        """分享场景-QQ"""
        poco("com.fdage.eight:id/iv_scene_cloud").click()
        sleep(5.0)
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.fdage.eight:id/frag_container").offspring("com.fdage.eight:id/rcv_scene").child(
            "com.fdage.eight:id/root_item")[0].child("com.fdage.eight:id/iv_menu").click()
        sleep(1.5)
        poco("com.fdage.eight:id/tv_option", text="分享").click()
        sleep(1.5)
        poco("com.fdage.eight:id/iv_qq")[0].click()
        sleep(5.0)
        poco("com.tencent.mobileqq:id/text1")[0].click()
        sleep(1.5)
        poco("com.tencent.mobileqq:id/dialogRightBtn", text="发送").click()
        sleep(1.5)
        poco("com.tencent.mobileqq:id/dialogLeftBtn", text="返回四维看看Pro").click()
        sleep(5.0)

        """分享-复制链接"""
        poco("com.fdage.eight:id/iv_scene_cloud").click()
        sleep(5.0)
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.fdage.eight:id/frag_container").offspring("com.fdage.eight:id/rcv_scene").child(
            "com.fdage.eight:id/root_item")[0].child("com.fdage.eight:id/iv_menu").click()
        sleep(1.5)
        poco("com.fdage.eight:id/tv_option", text="分享").click()
        sleep(1.5)
        poco("com.fdage.eight:id/iv_link")[0].click()

        """退出登录"""
        poco(name="com.fdage.eight:id/iv_my").click()
        sleep(2.0)
        poco(name="com.fdage.eight:id/tv_user_name").click()
        sleep(2.0)
        poco(name="com.fdage.eight:id/btn_logout").click()
        sleep(2.0)
        poco(name="com.fdage.eight:id/tv_ok").click()
        sleep(5.0)
        value = poco("com.fdage.eight:id/tv_user_accout").attr("text")
        try:
            assert_equal(value, "登录账号管理您的场景", "登出账号")
            logging.info("登出成功")
        except AssertionError:
            logging.info("登出失败")
        sleep(3.0)
    except Exception as e:
        logging.error("test_login error：" + str(e))
        now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        snapshot(filename=snapShot_path + "\\snapshot_%s.png" % now)


if __name__ == '__main__':
    pytest.main()
