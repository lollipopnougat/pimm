# lollipopnougat 2021.1.3
import sys
import os
import ping3
import threading
from pimm.pimm_const import *
from pimm.color_print import ColorPrint
import json
from concurrent.futures import ThreadPoolExecutor, wait
from multiprocessing import cpu_count


has_config_file = False
current_server = 'https://pypi.org/simple'
mirrors_file_path = os.path.join(os.path.dirname(__file__), 'mirrors.json')
mirrors_base_file_path = os.path.join(os.path.dirname(__file__), 'mirrors_base.json')
argn = 0
mirrors: dict = None
lines = None
res = {}
this_cpu_count = cpu_count()


def thread_job(name: str) -> (str, str):
    url = hostname.findall(mirrors[name])[0]
    tmp = ping3.ping(url)
    return (name, str(int(tmp * 1000)) if tmp else 'timeout')


def test_delay():
    pool = ThreadPoolExecutor(max_workers=this_cpu_count)
    all_jobs = [pool.submit(thread_job, name) for name in mirrors]
    wait(all_jobs)
    sorted_res = []
    for i in all_jobs:
        item = i.result()
        sorted_res.append(item)
    sorted_res.sort(key=lambda x: 4000 if x[1] == 'timeout' else int(x[1]))
    for item in sorted_res:
        name = item[0]
        time = item[1]
        url = mirrors[name]
        res = '{} {:<15}{}'.format(
            '*' if url == current_server else ' ', name, time)
        if item[1] == 'timeout':
            ColorPrint.warn(res)
        else:
            print(f'{res}ms')


def get_configuration_path():
    home = os.path.expanduser('~')
    config_path = '.pip/pip.conf'
    if sys.platform == 'win32':
        config_path = r'pip\pip.ini'
    return os.path.join(home, config_path)


def check_config_file():
    global current_server
    global lines

    config_path = get_configuration_path()

    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='UTF-8') as f:
            lines = f.read()
            current_server = pattern.findall(lines)[0]


def save_mirrors():
    with open(mirrors_file_path, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(mirrors))


def init_config():
    global mirrors
    config_path = get_configuration_path()
    config_folder = os.path.dirname(config_path)
    with open(mirrors_file_path, 'r', encoding='UTF-8') as f:
        mirrors = json.loads(f.read())
    if not os.path.exists(config_folder):
        os.mkdir(config_folder)
    if not os.path.exists(config_path):
        with open(config_path, 'w', encoding='UTF-8') as f:
            lines = f'{template_str1}{current_server}\n{template_str2}{hostname.findall(mirrors["default"])[0]}'
            f.write(lines)

def reset_config():
    global mirrors
    with open(mirrors_base_file_path, 'r', encoding='UTF-8') as f:
        mirrors = json.loads(f.read())
    save_mirrors()

def set_server(name: str):
    global current_server
    global lines
    current_server = mirrors[name]
    lines = f'{template_str1}{current_server}\n{template_str2}{hostname.findall(mirrors[name])[0]}'

    config_path = get_configuration_path()
    if os.path.exists(config_path):
        with open(config_path, 'w', encoding='UTF-8') as f:
            f.write(lines)


def add_server(name: str, url: str):
    if url_pattern.match(url):
        mirrors[name] = url
        save_mirrors()
        return True
    else:
        return False


def remove_server(name: str):
    global current_server
    if name in mirrors:
        if mirrors[name] == current_server:
            config_path = get_configuration_path()
            os.remove(config_path)
        mirrors.pop(name)
        save_mirrors()
        return True
    else:
        return False


def show_server():
    for i in mirrors:
        print('{} {:<15}{:<40}'.format('*' if mirrors[i] == current_server else ' ', i, mirrors[i]))


def show_help():
    print('Usage: pmm [options] [command]')
    print('Options:\n {:<20}{:<40}'.format(
        ' -V, --version', 'output the version number'))
    print(' {:<20}{:<40}'.format(' -h, --help, help', 'Show this help'))
    print('Commands:\n {:<20}{:<40}'.format(
        ' ls', 'List all the mirror server'))
    print(' {:<20}{:<40}'.format(' test', 'Show response time for all server'))
    print(' {:<20}{:<40}'.format(' use <name>', 'Change the mirror'))
    print(' {:<20}{:<40}'.format(' add <name> <url>', 'Add a mirror'))
    print(' {:<20}{:<40}'.format(' rm <name>', 'Remove the mirror'))
    print(' {:<20}{:<40}'.format(' reset', 'Reset to the initial state'))


def show_version():
    print(VERSION)


def main():
    argn = len(sys.argv)
    init_config()
    check_config_file()
    if argn == 1:
        ColorPrint.error('Not enough arguments')
        print('see pmm -h for more information')
    cmd = sys.argv[1]
    if cmd == '-h' or cmd == '--help':
        show_help()
    elif cmd == '-V' or cmd == '--version':
        show_version()
    elif cmd == 'ls':
        show_server()
    elif cmd == 'test':
        test_delay()
    elif cmd == 'use':
        if argn < 3:
            ColorPrint.error('Missing required argument')
            exit(-2)
        name = sys.argv[2]
        if name in mirrors:
            if current_server != mirrors[name]:
                set_server(name)
            ColorPrint.success(f'Server has been set to: {current_server}')
        else:
            ColorPrint.error(f'Server [{name}] not found')
            exit(-1)
    elif cmd == 'add':
        if argn < 4:
            ColorPrint.error('Missing required argument')
            exit(-2)
        name = sys.argv[2]
        url = sys.argv[3]
        res = add_server(name, url)
        if res:
            ColorPrint.success(f'Add Server [{name}] successfully')
        else:
            ColorPrint.error(f'The url {url} is invalid')
            exit(-3)
    elif cmd == 'rm':
        if argn < 3:
            ColorPrint.error('Missing required argument')
            exit(-2)
        name = sys.argv[2]
        res = remove_server(name)
        if res:
            ColorPrint.success(f'Remove Server [{name}] successfully')
        else:
            ColorPrint.error(f'Cannot found the item which name is {name}')
            exit(-2)
    elif cmd == 'reset':
        reset_config()
        ColorPrint.success(f'Reset the configuration successfully')
    elif cmd == 'help':
        show_help()
    else:
        ColorPrint.error(f'Unknown option: {cmd}')
        exit(-1)


if __name__ == "__main__":
    main()
