import re

def get_pid(urlList):
    pidList = []
    pattern = r'pid=(\d+)'

    for url in urlList:
        match = re.search(pattern, url)
        if match:
            pidList.append(match.group(1))
            
    return pidList


def parse_html(pidList, htmlList, avatar, tid, tname):
    avatar = f'<p><img src="{avatar}"/></a></p>'
    author = f'<a class="xw1" href="https://bbs.saraba1st.com/2b/space-uid-{tid}.html" target="_blank">{tname}</a>'
    replyList = [avatar]
    
    # Parse the HTML content and get the comments
    for i in range(len(pidList)):
        pid = pidList[i]
        html = str(htmlList[i])
        time_match = fr'(<em id="authorposton{pid}">.*?</em>)'
        content_match = fr'(<td class="t_f" id="postmessage_{pid}">.*?<div class="cm" id="comment_{pid}">)'
        time = re.findall(time_match, html, re.DOTALL)
        content = re.findall(content_match, html, re.DOTALL)
        if time: 
            reply = author + '<p>' + time[0] + '</p>'
        if content:
            reply = reply + '<p>' + content[0] + '</p>'
        replyList.append(reply)
        
    return replyList

def save_output(replyList, title, tid):
    beginner = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
    """

    ender = """
    </body>
    </html>
    """

    output = beginner
    for reply in replyList:
        output = output + reply + "<hr/>"
    output = output + ender

    # Replace relative_path with full_path
    pattern = r"forum.php\?mod=attachment"
    replace = "https://bbs.saraba1st.com/2b/forum.php?mod=attachment"
    output = re.sub(pattern, replace, output)

    # Write the HTML content to a file
    with open(f'{tid}.html', 'w', encoding='utf-8') as file:
        file.write(output)