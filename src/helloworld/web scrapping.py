# import requests
from bs4 import BeautifulSoup
from pageContent import page, homepage
import pandas as pd

site = page

soup = BeautifulSoup(site, "html.parser")
body = soup.find(class_="mvp-main-blog-body left relative")

story = body.find_all(class_="mvp-blog-story-wrap left relative infinite-post")
# story_link = story[0].find("a").get("href")
# story_head = story[0].find("a").find(class_="mvp-blog-story-text left relative").find("h2").text
story_heads = [item.find("a").find(
    class_="mvp-blog-story-text left relative").find("h2").text for item in story]
story_links = [item.find("a").get("href") for item in story]

if site != homepage:
    recent_story = body.find(id="mvp-cat-feat-wrap").find_all("a")
    # recent_story_link = recent_story[0].get("href")
    # recent_story_head = recent_story[0].find("h2").text
    recent_story_heads = [item.find("h2").text for item in recent_story]
    recent_story_links = [item.get("href") for item in recent_story]
else:
    recent_story_heads = []
    recent_story_links = []

headings = recent_story_heads + story_heads
links = recent_story_links + story_links

blog_page = pd.DataFrame({
    "headings": headings,
    "links": links
})
#blog_page.to_csv("home post.csv")


# get max Page number
def get_url(select, page_number=1):
    if select == "Home":
        url = "https://delaniblog.com.ng/"
    elif select == "Music":
        url = "https://delaniblog.com.ng/category/download-mp3/"
    elif select == "Entertainment":
        url = "https://delaniblog.com.ng/category/entertainment/"
    elif select == "Videos":
        url = "https://delaniblog.com.ng/category/world/videos/"
    elif select == "Album & EP":
        url = "https://delaniblog.com.ng/category/album-download/"
    elif select == "Lyrics":
        url = "https://delaniblog.com.ng/category/download-mp3/lyrics/"
    elif select == "Mixtape":
        url = "https://delaniblog.com.ng/category/mixtape/"
    elif select == "Trending":
        url = "https://delaniblog.com.ng/category/download-mp3/trending/"
    if page_number != 1:
        url = url + "page/" + str(page_number)
        return url
    else:
        return url


url1 = get_url("Entertainment")
url2 = get_url("Mixtape", 10)
print(url1)
print(url2)

website = BeautifulSoup(site, "html.parser")
last_page = website.find(class_="pagination").find_all("span")[
    0].text.split(" ")[-1]
print(last_page)
