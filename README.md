# jdcomm
Scrape comments of given product 

# 自动化批量抓取京东商品评论

问题及解决方案

登录状态


Playwright
遇到的第一个问题：自动化工具检测

```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://item.jd.com/100011633978.html')
        await page.screenshot(path='example.png')
        await browser.close()

asyncio.run(main())
```

解决方案：使用 Playwright 的 Stealth 模式，可以绕过反爬检测。
> https://github.com/tinyfish-io/tf-playwright-stealth

## What is Playwright Stealth?  
Playwright Stealth is a library that helps you bypass bot detection and make your web scraping undetectable. It is built on top of Playwright, a powerful automation library that enables you to control web browsers programmatically.

## How does Playwright Stealth work?
Playwright Stealth uses a combination of techniques to make your web scraping undetectable. It uses a real browser to scrape the web, which makes it harder for websites to detect that you are using a bot. It also uses a rotating user agent and IP address to make your scraping more anonymous.

## What does Playwright Stealth do?
### User Agent
Playwright Stealth uses a rotating user agent to make your web scraping more anonymous. It changes the user agent of the browser every time it makes a request, which makes it harder for websites to detect that you are using a bot.


## Anti-bot 常见检测手段
- User Agent 检测
- IP 检测
- Cookie 检测
- 验证码检测
- 行为检测
- 浏览器指纹检测
- 网络检测
- 机器学习检测
- 人工检测
- 其他检测


CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart)
完全自动化的公共图灵测试，用于区分计算机和人类
常用户防止恶意机器人访问网站
批量抓取数据时，可能会遇到 CAPTCHA 验证



JavaScript 检测



对策：
人工识别验证码
使用机器学习模型识别验证码
使用第三方验证码识别服务







```python
import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
        page = await context.new_page()
        await page.goto('https://item.jd.com/100011633978.html')
        await page.screenshot(path='example.png')
        await browser.close()


asyncio.run(main())
```


保持登录状态


自动化操作过程中检测是否需要人工验证和重新登录


检测
