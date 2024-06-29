# Stage1stCrawler

一个用于爬取Stage1st用户发帖的爬虫小程序。输入用户的UID，获取该用户的历史发言记录。

## 程序说明

使用场景：

- 以往的爬虫程序大多针对论坛的专楼进行爬取，而要检索特定用户的发言较为困难。
- 某个用户很有人格魅力，想要把他的发言下载到本地反复品鉴。
- 部分论坛谜语人喜欢编辑历史发言，用爬虫的快照机制让谜语人无所遁形。

程序的不足：

- 爬取速度较慢。
- 暂时不支持显示图片。

## 要预先安装的包

* pip install requests beautifulsoup4

## 使用方法

1. 在config.json中填写配置信息

```json
{
    "webpage_title": "网页标题",
    "payload": [
        {
            "username": "你的用户名",
            "password": "你的密码"
        }
    ],
    "target_id": 114514,
    "target_name": "目标的用户名",
    "page_number": 1919810,
    "avatar_path": "https://avatar.saraba1st.com/000/55/19/26_avatar_middle.jpg"
}
```

比较重要的几个参数是`username`、`password`，`target_id`和`page_number`：

- `username`和`password`是你的用户名和密码，用于登录论坛。
- `target_id`是你所要爬取用户的uid，可以在对方的主页中看到，如[https://bbs.saraba1st.com/2b/space-uid-114514.html](https://bbs.saraba1st.com/2b/space-uid-114514.html)。
- `page_number`是对方回帖的总页数。获取方法是点开主页的回帖，点击"下一页"，此时主页地址会变成这种格式：[https://bbs.saraba1st.com/2b/home.php?mod=space&uid=114514&do=thread&view=me&type=reply&order=dateline&from=space&page=2](https://bbs.saraba1st.com/2b/home.php?mod=space&uid=114514&do=thread&view=me&type=reply&order=dateline&from=space&page=2)。不断修改地址中`page`参数，直到翻到对方发言的最后一页。
- `page_number`填的不对可能会导致发言记录少爬取或者程序报错。

其他几个参数仅用于设置输出文件的外观，对爬虫的结果没有影响，根据需求填写。

2. 执行demo.py

```shell
python demo.py
```

输出结果保存在当前目录的文件"{target_id}.html"中，这是输出文件的一个[示例](/555493.html)。