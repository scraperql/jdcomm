import asyncio

from dotenv import load_dotenv
from playwright.async_api import async_playwright
import agentql
from playwright_stealth import stealth_async

price_login_query = """
{
    login_check {
        is_login
        username
    }
    
    product {
        name
        price(number only, without the currency)
        currency
        colors[] {
            color
            selected
        }
        versions[] {
            version
            selected
        }
    }
}
""".strip()


comments_query = """
    product {
        price(number only, without the currency)
        currency
        colors[] {
            color
            selected
        }
        versions[] {
            version
            selected
        }
    }
    distributor {
        name
        absolute_url
    }
    
    product_reviews[] {
        author
        stars
        content
        attachments[] {
            absolute_url
        }
        color
        version
        date
        location
        upvote_number
    }
    """.strip()


def configPlaywright():
    pass


class JdComments:
    def __init__(self, url):
        self.url = url

    async def get_price(self):
        async def on_request(request):
            url = request.url
            if url != "https://item.jd.com/100064843490.html":
                return
            print(">>", request.method, request.url)
            headers = await request.all_headers()
            for header in headers:
                print(f"{header}: {headers[header]}")

        async with async_playwright() as p, await p.chromium.launch(headless=False) as browser:
            context = await browser.new_context(storage_state='./cookies/jd_session.json')
            page = await agentql.wrap_async(context.new_page())
            # await page.enable_stealth_mode()
            await page.set_viewport_size({"width": 1920, "height": 1080})
            await page.set_extra_http_headers({'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6'})
            await page.set_extra_http_headers({'Dnt': '1'})
            page.on("request", on_request)
            await stealth_async(page)
            await self._get_price_worker(page)
            await page.wait_for_timeout(3000)
            # save state to file
            await context.storage_state(path='./cookies/jd_session.json')
            input("Press enter to close browser")
            await page.close()

    async def _get_price_worker(self, page):
        await page.goto(self.url)
        await page.wait_for_page_ready_state()
        await page.wait_for_timeout(3000)

        # Check if the page need to log-in
        while True:
            response = await page.query_data(price_login_query)
            print(response)

            if not response['login_check']['is_login']:
                await self._login(page)
            else:
                name = response['product']['name']
                price = response['product']['price']
                print(f"{name} Price: {price}")
                input("Press enter to exit")
                break

    async def _login(self, page):
        # wait for human to login, prompt user to login then press enter to continue
        input("Please login then press enter to continue")


async def drissionTest(url):
    from DrissionPage import ChromiumPage
    page = ChromiumPage()
    page.listen.start('comment')
    page.get(url)
    response = page.listen.wait()
    print(response)


async def main():
    url = 'https://item.jd.com/100064843490.html'
    # url = 'https://detail.tmall.com/item.htm?id=738427143584'
    # jd = JdComments(url)
    # await jd.get_price()
    await drissionTest(url)


if __name__ == "__main__":
    # load env
    load_dotenv()
    asyncio.run(main())
