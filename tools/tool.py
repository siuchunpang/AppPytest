import logging
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.exceptions import PocoException

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

logging.basicConfig(filename=log_path + "\\%s.log" % time.strftime('%Y_%m_%d'),
                    filemode='a',
                    format='%(asctime)s-%(filename)s-%(levelname)s:%(message)s',
                    level=logging.INFO)

'''
def connect_camera():
    poco("com.fdage.eight:id/iv_scene_local").click()
    sleep(2)
    poco("com.fdage.eight:id/floatingBtn").click()
    sleep(2)
    # 判断是否有引导语，有就跳过
    if poco("com.fdage.eight:id/tv_title", text="拍摄场景（1/5）").exists():
        poco("com.fdage.eight:id/tv_cancel").click()
        sleep(2)
    # 判断
    if poco("com.fdage.eight:id/container").exists() and poco("com.fdage.eight:id/tv_content", text="拍摄项目会断开相机网络"):
        logging.info("app已连接相机，相机已联网")
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(2)
        logging.info("进入拍摄页面，相机已断网")
    elif poco("com.fdage.eight:id/disconnect_dialog_ok").exists():
        logging.info("app未连接相机")
        poco("com.fdage.eight:id/disconnect_dialog_ok", text="去连接相机").click()
        sleep(2)
        if poco("com.android.settings:id/switch_widget").attr('checked') == False:
            poco("com.android.settings:id/switch_widget").click()
            sleep(2)
        poco("android:id/title", text=camera_name).wait_for_appearance(10)
        poco("android:id/title", text=camera_name).click()
        sleep(2)
        poco("android:id/button1").click()
        sleep(2)
        logging.info("正在连接相机...")
        poco(name="向上导航").click()
        sleep(2)
        poco("com.fdage.eight:id/disconnect_dialog_ok").wait_for_disappearance(10)
        logging.info("app已连接相机" + camera_name)
    else:
        logging.info("app已连接相机，相机未联网")
        logging.info("进入拍摄页面")
'''

"""
参数设定：
hdr："auto"=自动，"on"=打开，"off"=关闭
左右拍摄开关rl：False/True
定时器timer：-0.3=关闭，-0.26=1s，0.3=15s
模式：0=自动,1=专业
色温wb：-0.3=自动，-0.26=3000k, 0.3=10000k
曝光补偿ev：-0.12=默认值，-0.3=-2值，0.3=2值
"""


def param(hdr="on", rl=False, timer=-0.3, type=0, wb=-0.3, ev=-0.3):
    poco("com.fdage.eight:id/iv_camset").click()
    sleep(2)
    # hdr开关
    poco("com.fdage.eight:id/iv_hdr").click()
    sleep(2)
    poco("com.fdage.eight:id/tv_" + hdr).click()
    sleep(2)
    logging.info("hdr模式为：%s" % hdr)

    # 左右拍摄开关
    if not rl:
        if poco(text="左右拍摄开").exists():
            poco(text="左右拍摄开").click()
            sleep(2)
        logging.info("参数设定：同步拍摄")
    elif rl:
        if poco(text="左右拍摄关").exists():
            poco(text="左右拍摄关").click()
            sleep(2)
        logging.info("参数设定：左右拍摄")
    # 定时器开关
    if timer == -0.3:
        if not poco(text="定时器").exists():
            poco("com.fdage.eight:id/set_timer").click()
            sleep(2)
            poco("com.fdage.eight:id/sb_timer").swipe([-0.3, 0])
            logging.info("参数设定：定时器关")
    else:
        poco("com.fdage.eight:id/set_timer").click()
        sleep(2)
        poco("com.fdage.eight:id/sb_timer").swipe([timer, 0])
        logging.info("参数设定：定时器开")
    # 自动模式/专业模式
    if type == 0:
        poco(text="自动模式").click()
        sleep(2)
        logging.info("参数设定：自动模式")
    else:
        poco(text="专业模式").click()
        sleep(2)
        # 专业模式色温
        if wb != -0.3:
            poco("com.fdage.eight:id/sb_colortemprature_manual").swipe([wb, 0])
            logging.info("参数设定：色温调节")
        # 专业模式曝光补偿
        if ev != -0.3:
            poco("com.fdage.eight:id/sb_exposure").swipe([ev, 0])
            logging.info("参数设定：曝光补偿调节")
    poco("com.fdage.eight:id/tv_right").click()
    sleep(2)


def shoot(rl=False):
    poco("com.fdage.eight:id/ic_shot").click()
    sleep(2)
    poco("com.fdage.eight:id/tv_title", text="正在拍照").wait_for_appearance(120)
    try:
        if rl:
            logging.info("左右拍摄开")
            logging.info("拍摄A面")
            poco("com.fdage.eight:id/tv_title", text="请站在相机右侧拍摄(1/2)").wait_for_appearance(120)
            sleep(2)
            poco("com.fdage.eight:id/ic_shot").click()
            sleep(2)
            poco("com.fdage.eight:id/tv_title", text="正在拍照").wait_for_appearance(120)
            logging.info("拍摄B面")
        else:
            logging.info("左右拍摄关")
        poco("com.fdage.eight:id/waveView").wait_for_appearance(120)
        logging.info("拍摄完成")
        sleep(2)
        if poco("com.fdage.eight:id/tv_title", text="拍摄空间视频").exists():
            poco("com.fdage.eight:id/tv_cancel").click()
            logging.info("拍摄空间视频提示")
            sleep(2)
        return True
    except PocoException as e:
        logging.error(e)
        if poco("com.fdage.eight:id/tv_content").exists():
            logging.info(poco("com.fdage.eight:id/tv_content").get_text())
            poco("com.fdage.eight:id/tv_ok").click()
            sleep(2)
        return False


def video(video_time):
    """录制视频"""
    poco(name="com.fdage.eight:id/btn_switch_video", text="录像").click()
    sleep(2)
    poco("com.fdage.eight:id/iv_cam_relocate").wait_for_appearance(60)
    logging.info("获取视频流画面")
    sleep(2)
    poco(name="com.fdage.eight:id/btn_record").click()
    sleep(video_time)
    poco(name="com.fdage.eight:id/btn_record").click()
    sleep(2)
    poco("com.fdage.eight:id/bg_btn_playback").wait_for_appearance(120)
    logging.info("录像mp4已保存")
    sleep(2)
    poco(name="com.fdage.eight:id/btn_switch_photo").click()
    sleep(2)
    poco("com.fdage.eight:id/tv_titlebar_title", text="拍摄").wait_for_appearance(30)
    logging.info("返回拍摄界面")
    sleep(2)


def save_scene(name, category=0):
    categories = ["industry_all", "culture_relics", "estate", "e_commercial", "food", "other"]
    poco(name="com.fdage.eight:id/tv_right", text="保存").click()
    sleep(2)
    poco(name="com.fdage.eight:id/et_title").set_text(name)
    poco("com.fdage.eight:id/btn_%s" % categories[category]).click()
    sleep(2)
    poco(name="com.fdage.eight:id/tv_right").click()
    logging.info("保存项目")
    sleep(2)


def upload(psw=None):
    """上传场景"""
    poco("com.fdage.eight:id/iv_upload").click()
    if poco("com.fdage.eight:id/tv_content", text="相机尚未连接Wi-Fi，点击跳转到连接界面").exists():
        logging.info("相机未连接wifi")
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(2)
        poco(text=wifi_name).wait_for_appearance(60)
        poco(text=wifi_name).click()
        poco("com.fdage.eight:id/iv_select").wait_for_appearance(60)
        sleep(2)
        poco("com.fdage.eight:id/tv_network_desc", text="已连接到%s" % wifi_name).wait_for_appearance(60)
        logging.info("已连接到%s" % wifi_name)
        poco("com.fdage.eight:id/iv_left").click()
        sleep(10)
        poco("com.fdage.eight:id/iv_upload").click()
    sleep(2)
    poco("com.fdage.eight:id/tv_ok", text="上传").click()
    sleep(2)
    poco(name="com.fdage.eight:id/tv_title").wait_for_appearance(timeout=600)
    logging.info("上传成功")
    poco("com.fdage.eight:id/tv_ok", text="确定").click()
    sleep(2)


def connect_wifi():
    """只连外网"""
    poco("com.fdage.eight:id/iv_my").click()
    sleep(2.0)
    poco("com.fdage.eight:id/tv_battery").click()
    sleep(2.0)
    while not poco(text=wifi_name).exists():
        poco("com.android.settings:id/list").swipe([-0.0152, -0.4633])
        sleep(2.0)
        if poco(text=wifi_name).exists():
            sleep(2.0)
            break
    poco(text=wifi_name).click()
    sleep(2.0)
    if poco("android:id/button1").exists():
        poco("android:id/button1").click()
        sleep(1.0)
    elif poco("com.android.settings:id/password", text="密码").exists():
        poco("com.android.settings:id/password").set_text("")
        poco("com.android.settings:id/password").set_text("4DAGE168")
        sleep(1.0)
        poco(text="连接").click()
        sleep(1.0)
    else:
        poco("android:id/button3").click()
        sleep(1.0)
    sleep(5.0)
    poco(text="已连接").wait_for_appearance(15)
    poco("向上导航").click()
    sleep(2.0)


def connect_camera():
    """连接相机"""
    poco("com.fdage.eight:id/iv_my").click()
    sleep(2.0)
    poco("com.fdage.eight:id/tv_battery").click()
    sleep(2.0)
    while not poco(text=camera_name).exists():
        poco("com.android.settings:id/list").swipe([-0.0152, -0.4633])
        sleep(2.0)
        if poco(text=camera_name).exists():
            sleep(2.0)
            break
    poco(text=camera_name).click()
    sleep(2.0)
    if poco("android:id/button1").exists():
        poco("android:id/button1").click()
        sleep(1.0)
    elif poco("com.android.settings:id/password", text="密码").exists():
        poco("com.android.settings:id/password").set_text("")
        poco("com.android.settings:id/password").set_text("12345678")
        sleep(1.0)
        poco(text="连接").click()
        sleep(1.0)
    else:
        poco("android:id/button3").click()
        sleep(1.0)
    sleep(5.0)
    poco(text="已连接 (不可上网)").wait_for_appearance(15)
    poco("向上导航").click()
    sleep(2.0)
    poco("com.fdage.eight:id/iv_scene_local").click()
    sleep(2)
    poco("com.fdage.eight:id/floatingBtn").click()
    sleep(2)

    # 判断是否有引导语，有就跳过
    if poco("com.fdage.eight:id/tv_title", text="拍摄场景（1/5）").exists():
        poco("com.fdage.eight:id/tv_cancel").click()
        sleep(2)
    # 判断
    if poco("com.fdage.eight:id/container").exists() and poco("com.fdage.eight:id/tv_content", text="拍摄项目会断开相机网络"):
        logging.info("app已连接相机，相机已联网")
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(2)
        logging.info("进入拍摄页面，相机已断网")
    elif poco("com.fdage.eight:id/disconnect_dialog_ok").exists():
        logging.info("app未连接相机")
        poco("com.fdage.eight:id/disconnect_dialog_ok", text="去连接相机").click()
        sleep(2)
        if poco("com.android.settings:id/switch_widget").attr('checked') == False:
            poco("com.android.settings:id/switch_widget").click()
            sleep(2)
        poco("android:id/title", text=camera_name).wait_for_appearance(10)
        poco("android:id/title", text=camera_name).click()
        sleep(2)
        poco("android:id/button1").click()
        sleep(2)
        logging.info("正在连接相机...")
        poco(name="向上导航").click()
        sleep(2)
        poco("com.fdage.eight:id/disconnect_dialog_ok").wait_for_disappearance(10)
        logging.info("app已连接相机" + camera_name)
    else:
        logging.info("app已连接相机，相机未联网")
        logging.info("进入拍摄页面")
