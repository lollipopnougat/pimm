import re

VERSION = '0.0.6'
pattern = re.compile('(https?://.+?)/?\n')
url_pattern = re.compile('(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?')
hostname = re.compile('https?://(.+?)/')
template_str1 = '[global]\nindex-url = '
template_str2 = '[install]\ntrusted-host = '
command_str = 'pmm'

