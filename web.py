import re
import os
from exp10it import update_config_file_key_value
from exp10it import CONFIG_INI_PATH

with open(CONFIG_INI_PATH, 'r+') as f:
    content = f.read()
#下面用于设置web后台口令及将web后台相关表[session机制,登录数据等属于django功能中要建立的表]存储到数据库
#os.chdir("pannel")
if re.search(r"finish_web_setting", content):
    pass
else:
    os.system("pip3 install Django==1.10.3")
    os.system("python3 pannel/manage.py migrate")
    os.system("python3 pannel/manage.py createsuperuser")
    update_config_file_key_value(CONFIG_INI_PATH, 'default', 'finish_web_setting', 1)

os.system("python3 pannel/manage.py runserver 0.0.0.0:8000")


