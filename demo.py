import json
import re
import webCrawler
import htmlParser

config = json.load(open('./test.json', 'r', encoding='utf-8'))

webpage_title = config['webpage_title']
target_id = config['target_id']
target_name = config['target_name']
page_num = config['page_number']
avatar_path = config['avatar_path']

payload = {
    'username': config['payload']['username'],
    'password': config['payload']['password']
}

textList = []
urlList = []
pattern = r'forum\.php\?mod=redirect&goto=findpost&ptid=\d+&pid=\d+'

for i in range(1,page_num+1):
    login_url = 'https://bbs.saraba1st.com/2b/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
    protected_url = f'https://bbs.saraba1st.com/2b/home.php?mod=space&uid={target_id}&do=thread&view=me&type=reply&order=dateline&page={i}'
    soup = webCrawler.crawl_homepage(login_url, protected_url, payload)
    if soup:
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            text = link.text
            textList.append(text)
            if href is not None and href.find(pattern):
                urlList = urlList + list(re.findall(pattern, href))
print("Homepage retrieved.")
htmlList = webCrawler.crawl_posts(login_url, urlList, payload)
print("Posts retrieved.")
pidList = htmlParser.get_pid(urlList)
replyList = htmlParser.parse_html(pidList, htmlList, avatar_path, target_id, target_name)
print("Generating html file...")
# Output
htmlParser.save_output(replyList, webpage_title, target_id)