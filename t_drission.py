from DrissionPage import ChromiumPage


def run(url):
    page = ChromiumPage()
    page.get(url)
    print(page.title)
    input("Press Enter to continue...")
    page.quit()


if __name__ == '__main__':
    run("https://item.jd.com/100064843490.html")
