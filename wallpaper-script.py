import shutil
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
page = requests.get("https://old.reddit.com/r/$__SUBREDDIT__/top/?sort=top&t=hour&limit=1", headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')
post_div = soup.find("div", class_ = "sitetable linklisting")
image_url = post_div.find("div").get("data-url")

del page

image_extensions = [".png", ".jpeg", ".jpg", ".bmp"]

if "imgur" in image_url:
    image_url += ".png"

elif any(image_extension in image_url for image_extension in image_extensions):
    pass

elif "redd.it" not in image_url:
    exit()

response = requests.get(image_url, stream=True)
with open("$__PATH__/wallpaper", "wb") as wallpaper:
    shutil.copyfileobj(response.raw, wallpaper)

del response
