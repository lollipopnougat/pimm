# lollipopnougat 2021.1.3
import sys
import os
import ping3
import threading
from pimm.pimm_const import *
import json


has_config_file = False
current_server = 'https://pypi.org/simple'
argn = 0
mirrors = None
lines = None
res = {}


def test_delay():
    thread_list = []
    def job(name):
        url = hostname.findall(mirrors[name])[0]
        tmp = ping3.ping(url)
        if tmp:
            res[name] = int(tmp * 1000)
        else:
            res[name] = 'timeout!'
    for i in mirrors:
        t = threading.Thread(target=job, args=(i,))
        thread_list.append(t)
        t.start()
    for t in thread_list:
        t.join()
    for i in res:
        if mirrors[i] == current_server:
            if res[i] == 'timeout!':
                print('* {:<10}{:<40}\t{}'.format(i, mirrors[i], res[i]))
            else:
                print('* {:<10}{:<40}\t{}ms'.format(i, mirrors[i], res[i]))
        else:
            if res[i] == 'timeout!':
                print('  {:<10}{:<40}\t{}'.format(i, mirrors[i], res[i]))
            else:
                print('  {:<10}{:<40}\t{}ms'.format(i, mirrors[i], res[i]))
    


def check_config_file():
    global current_server
    global lines
    global mirrors
    mirror_config_path = os.path.dirname(__file__) + '/mirrors.json'
    home = os.path.expanduser('~')
    config_path = '/.pip/pip.conf'
    if sys.platform == 'win32':
        config_path = r'\pip\pip.ini'
        mirror_config_path.replace('/', '\\')
    if os.path.exists(home + config_path):
        has_config_file = True
        with open(home + config_path, 'r', encoding='UTF-8') as f:
            lines = f.read()
            current_server = pattern.findall(lines)[0]
    with open(mirror_config_path, 'r', encoding='UTF-8') as f:
        mirrors = json.loads(f.read())


def save_mirrors(mymirrors):
    mirror_config_path = os.path.dirname(__file__) + '/mirrors.json'
    if sys.platform == 'win32':
        mirror_config_path.replace('/', '\\')
    with open(mirror_config_path, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(mirrors))


def init_config():
    home = os.path.expanduser('~')
    config_path = '/.pip/pip.conf'
    config_folder = '/.pip'
    if sys.platform == 'win32':
        config_path = r'\pip\pip.ini'
        config_folder =r'\pip'

    if not os.path.exists(home + config_folder):
        os.mkdir(home + config_folder)
    if not os.path.exists(home + config_path):
        with open(home + config_path, 'w', encoding='UTF-8') as f:
            lines = template_str1 + current_server + '\n' + template_str2 + 'https://' + hostname.findall(mirrors['default'])[0]
            f.write(lines)
        
    
def set_server(name):
    global current_server
    global lines
    current_server = mirrors[name]
    lines = template_str1 + current_server + '\n' + template_str2 + 'https://' + hostname.findall(mirrors[name])[0]
    home = os.path.expanduser('~')
    config_path = '/.pip/pip.conf'
    if sys.platform == 'win32':
        config_path = r'\pip\pip.ini'
    if os.path.exists(home + config_path):
        has_config_file = True
        with open(home + config_path, 'w', encoding='UTF-8') as f:
            f.write(lines)


def show_server():
    for i in mirrors:
        if mirrors[i] == current_server:
            print('* {:<10}{:<40}'.format(i, mirrors[i]))
        else:
            print('  {:<10}{:<40}'.format(i, mirrors[i]))


def show_help():
    print('Usage: pmm [options] [command]')
    print('Options:\n {:<25}{:<40}'.format(' -V, --version','output the version number'))
    print(' {:<25}{:<40}'.format(' -h, --help','output usage information'))
    print('Commands:\n {:<25}{:<40}'.format(' ls','List all the mirror server'))
    print(' {:<25}{:<40}'.format(' test','Show response time for all server'))
    print(' {:<25}{:<40}'.format(' use <server name>','Change the mirror'))
    print(' {:<25}{:<40}'.format(' help','Show this help'))




def show_version():
    print(VERSION)


def main():
    argn = len(sys.argv)
    init_config()
    check_config_file()
    if argn == 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        show_help()
    elif sys.argv[1] == '-V' or sys.argv[1] == '--version':
        show_version()
    elif sys.argv[1] == 'ls':
        show_server()
    elif sys.argv[1] == 'test':
        test_delay()
    elif sys.argv[1] == 'use':
        if argn < 3:
            print('error: missing required argument server_name')
        elif sys.argv[2] in mirrors:
            if current_server != mirrors[sys.argv[2]]:
                set_server(sys.argv[2])
            print(f'Server has been set to: {current_server}')
        else:
            print(f'Server {sys.argv[2]} not find')
    elif sys.argv[1] == 'help':
        show_help()
    else:
        print(f'error: unknown option {sys.argv[1]}')


if __name__ == "__main__":
    main()
