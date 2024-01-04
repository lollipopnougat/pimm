# pimm

## pip mirrors manager

This is a pip mirrors manager, just like [nrm](https://github.com/Pana/nrm) for npm.

### support command

```bash
pmm ls # list all server
pmm help # show help
pmm test # show response time of all servers 
pmm use <name> # use <server_name> server 
pmm -V # show current version
pmm add <name> <url> # Add a mirror
pmm rm <name> #Remove the mirror
pmm reset #Reset to the initial state
```

### mirrors includes

```json
{
    "aliyun": "https://mirrors.aliyun.com/pypi/simple",
    "douban": "https://pypi.doubanio.com/simple",
    "hit": "https://mirrors.hit.edu.cn/pypi/web/simple",
    "huawei": "https://repo.huaweicloud.com/repository/pypi/simple",
    "jlu": "https://mirrors.jlu.edu.cn/pypi/simple",
    "pku": "https://mirrors.pku.edu.cn/pypi/web/simple",
    "tencent": "https://mirrors.cloud.tencent.com/pypi/simple",
    "thu": "https://pypi.tuna.tsinghua.edu.cn/simple",
    "ustc": "https://pypi.mirrors.ustc.edu.cn/simple",
    "default": "https://pypi.org/simple"
}
```

### LICENSE

MIT
