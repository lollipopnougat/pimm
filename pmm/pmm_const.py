import re

VERSION = '0.0.3'
pattern = re.compile('(https?://.+?)/?\n')
hostname = re.compile('https?://(.+?)/')
template_str1 = '[global]\nindex-url = '
template_str2 = '[install]\ntrusted-host = '
# mirrors = {
#     "aliyun": "https://mirrors.aliyun.com/pypi/simple",
#     "thu": "https://pypi.tuna.tsinghua.edu.cn/simple",
#     "opentuna": "https://opentuna.cn/pypi/web/simple",
#     "ustc": "https://pypi.mirrors.ustc.edu.cn/simple",
#     "douban": "https://pypi.doubanio.com/simple",
#     "default": "https://pypi.org/simple"
# }
