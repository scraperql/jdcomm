from playwright.sync_api import sync_playwright


def run(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state("load")
        print(page.title())
        input("Press Enter to continue...")
        browser.close()


if __name__ == '__main__':
    run("https://item.jd.com/100064843490.html")
