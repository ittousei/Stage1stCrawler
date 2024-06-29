import requests
from bs4 import BeautifulSoup

# Function to log in and retrieve the target's homepage
def crawl_homepage(login_url, protected_url, payload):
    # Start session
    session = requests.Session()
    # Login
    response = session.post(login_url, data=payload)
    
    # Check if login was successful
    if response.status_code == 200:
        # Now request the protected page
        response = session.get(protected_url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        else:
            print(f"Failed to retrieve the protected page. Status code: {response.status_code}")
            return None
    else:
        print(f"Failed to log in. Status code: {response.status_code}")
        return None
    

# Function to retrieve the target's all posts
def crawl_posts(login_url, urlList, payload):
    htmlList = []
    # Start session
    session = requests.Session()
    # Login
    response = session.post(login_url, data=payload)
    
    # Request all post pages in target's homepage
    for i in range(len(urlList)):
        protected_url = "https://bbs.saraba1st.com/2b/" + urlList[i]
        # Check if login was successful
        if response.status_code == 200:
            # Now request the protected page
            response = session.get(protected_url)
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the HTML content
                soup = BeautifulSoup(response.text, 'html.parser')
                if soup:
                    htmlList.append(soup)
                else:
                    print(f"Failed to retrieve the protected page. Status code: {response.status_code}")
        else:
            print(f"Failed to log in. Status code: {response.status_code}")
    return htmlList