# Stage1stCrawler

一个用于爬取Stage1st用户发帖的爬虫小程序。输入用户的UID，获取该用户的历史发言记录。

## 程序说明

使用场景：

- 以往的爬虫程序大多针对论坛的专楼进行爬取，而要检索特定用户的发言较为困难。
- 某个用户很有人格魅力，想要把他的发言下载到本地反复品鉴。
- 部分论坛谜语人喜欢编辑发言，用爬虫的快照机制让谜语人无所遁形。

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

几个比较重要的参数是`username`、`password`，`target_id`和`page_number`：

- `username`和`password`是你的用户名和密码，用于登录论坛。
- `target_id`是你所要爬取用户的UID，可以在用户主页中看到，如[https://bbs.saraba1st.com/2b/space-uid-114514.html](https://bbs.saraba1st.com/2b/space-uid-114514.html)，`114514`便是该用户的UID。
- `page_number`是用户回帖的总页数。获取方法是访问目标用户的主页，进入"回帖数"页面，自行统计回帖的页数。
- `page_number`填的不对可能会导致发言记录少爬取或者程序报错。

其他参数仅用于调整输出文件的外观，对爬虫的结果没有影响，根据需求填写：

- `webpage_title`是输出文件的HTML head title。
- `target_name`是你所要爬取用户的昵称。
- `avatar_path`是用户头像的图床链接。

2. 执行demo.py

```shell
python demo.py
```

输出结果保存在项目根目录下的f"{target_id}.html"中，这是输出文件的一个[示例](/555493.html)。
