"""

======================

@author:niuqun

@time:2019/9/4:9:55 AM

@email:17689551930@163.com

======================
杜丫丫ios 页面元素
变量名 = 元素
"""
import sys,os
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
# 手机号码登陆按钮
phone_login = (By.ID,"ai.zile.app:id/btn_phone_login")
# 微信登陆入口
wx_login=(By.ID,"ai.zile.app:id/btn_wechat_login")
# 杜丫丫隐私统一按钮
privacy_yes=(By.ID,"ai.zile.app:id/checkboxContract")
# 杜丫丫隐私不同意按钮
# privacy_no=(By.NAME,"select no")
# ios权限允许
system_ios=(By.NAME,"打开")
# 如何上课
who_word=(By.XPATH,'//*[@resource-id="app"]/android.view.View[7]/android.view.View[1]/android.view.View[1]')
# 课堂type
classroom=(By.ID,"ai.zile.app:id/nav_course")
# 下载课程
download = (By.XPATH,'//*[@text="下载课程"]')
# 关卡列表I'm hungry
hungry = (By.XPATH,'//*[@resource-id="app"]/android.view.View[6]/android.view.View[1]/android.view.View[1]')
# 课程picnic
pinnic = (By.XPATH,'//*[@resource-id="app"]/android.view.View[5]/android.view.View[1]/android.view.View[1]')
# 课程What's this?
What_this=(By.XPATH,'//*[@resource-id="app"]/android.view.View[4]/android.view.View[1]/android.view.View[1]')
# 课程onthefram
on_the_farm=(By.XPATH,'//*[@resource-id="app"]/android.view.View[3]/android.view.View[1]/android.view.View[1]')
# 课程reviwe
review=(By.XPATH,'//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[1]')
# 点击reciew课程关卡
reviews=(By.XPATH,'//*[@text="Review"]')
# 发现按钮
discover=(By.NAME,"发现")
# 杜丫丫按钮
duyaya=(By.NAME,"杜丫丫")
my=(By.NAME,"我的")
# 发现如何上课
how_clss=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView')
# 练习客服
relation=(By.XPATH,'//XCUIElementTypeApplication[@name="杜丫丫爱英语"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeButton[2]')
# 购买课程
buy_cou=(By.ID,'ai.zile.app:id/card_view')
# 添加地址页面
Add_the_address=(By.XPATH,'//XCUIElementTypeOther[@name="付款"])[2]/XCUIElementTypeOther[5]')
# 取消按钮
call=(By.XPATH,'//XCUIElementTypeSheet[@name="400-061-0365"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther')
# 发现——如何上课返回
return_duyaya=(By.ID,"ai.zile.app:id/iv_back_pressed")
# 购买课程返回
add_return=(By.ID,"ai.zile.app:id/relativeBack")
# 课程内部返回按钮
return_lict=(By.XPATH,'//*[@resource-id="ai.zile.app:id/relativeBack"]/android.widget.ImageView[1]')