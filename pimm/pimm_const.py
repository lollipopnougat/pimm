import re

VERSION = '0.0.2'
pattern = re.compile('(https?://.+?)/?\n')
hostname = re.compile('https?://(.+?)/')
template_str1 = '[global]\nindex-url = '
template_str2 = '[install]\ntrusted-host = '
