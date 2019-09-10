allure generate report/ -o report/html(将xml文件转化为html)
pytest==4.0.1
获取app启动名/包名adb shell dumpsys window windows | grep mFocusedApp
ai.zile.app/.ui.main.MainActivity
获取启动日志：第一启动包名
adb logcat ActivityManager:I *:s

