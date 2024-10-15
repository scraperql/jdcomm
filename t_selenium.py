import asyncio
from selenium import webdriver


async def run(url):
    # options = webdriver.ChromeOptions()
    # options.add_argument("user-data-dir=./chrome-data")
    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    print(driver.title)
    input("Press Enter to continue...")
    driver.quit()


if __name__ == '__main__':
    asyncio.run(run("https://item.jd.com/100064843490.html"))
