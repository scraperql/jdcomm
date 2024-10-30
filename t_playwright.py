import json
import time

from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import agentql


QUERY_TABS = """
{
    tabs {
        product_introduction_element
        product_spec_element
        product_comment_element
        product_qa_element
    }
}
""".strip()


QUERY = """
{
    product {
        name
        price
        color[] {
            name
        }
        selected_color {
            name
        }
        version[] {
            name
        }
        selected_version {
            name
        }
    }
}
""".strip()


def query_product_info(page: Page):
    # extract the product info
    result = page.query_data(QUERY)
    print(json.dumps(result, indent=2))
    time.sleep(10)

    # extract the comments
    result = page.query_elements(QUERY_TABS)
    print(result.to_data())
    if result.product_comment_tab_btn:
        result.product_comment_tab_btn.click()
        time.sleep(10)


def run(url):
    with sync_playwright() as p:
        executable_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        browser = p.chromium.launch(executable_path=executable_path, headless=False)
        context = browser.new_context(storage_state="state.json")
        page = context.new_page()
        stealth_sync(page)
        page = agentql.wrap(page)
        page.goto(url, wait_until="load", timeout=1000 * 60 * 5)

        query_product_info(page)

        print(page.title())
        input("Press Enter to continue...")
        context.storage_state(path="state.json")
        context.close()
        browser.close()


if __name__ == '__main__':
    # run("https://bot.sannysoft.com/")
    run("https://item.jd.com/100064843490.html")
