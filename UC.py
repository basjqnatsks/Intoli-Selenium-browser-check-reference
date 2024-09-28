import undetected_chromedriver as uc
from time import sleep
driver = uc.Chrome()

sleep(1)
driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")

