import re

from playwright.async_api import async_playwright
from playwright_stealth import Stealth
import asyncio, csv
from pathlib import Path
async def main():
    async with Stealth().use_async(async_playwright()) as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,svg,gif}", lambda route: route.abort())
        await page.goto("https://www.carousell.com.my/")
        
        search_content = input("Enter the product you want to search: ")
        search_box = page.get_by_placeholder("Search for an item")
        await search_box.wait_for()
        await search_box.fill(search_content)
        await search_box.press("Enter")
        
        close_button = page.get_by_role("button", name="Close")
        try:
            await close_button.wait_for(state="visible", timeout=5000)
            if await close_button.is_visible():
                await close_button.click()
                await page.locator("div").filter(has_text=re.compile(r"^All$")).first.click()
        except Exception:
            pass
        
        #press_see_more_button
        Next_button = page.get_by_role("button", name="Next")
        Continue_browsing = page.get_by_role("button", name="Continue browsing")
        await Next_button.wait_for(state="visible", timeout=5000)
        await Next_button.click()
        await page.wait_for_timeout(1000)
        await Next_button.click()
        await page.wait_for_timeout(1000)
        await Continue_browsing.click()
        
        while True:
            see_more_button = page.get_by_role("button", name="Show more results")
            try:
                await see_more_button.wait_for(state="visible", timeout=3000)
                await see_more_button.click()
                await page.wait_for_timeout(1000)
            except:
                break
        #get_results
        data = []
        await page.wait_for_selector("div[data-testid]")
        product = await page.locator("div[data-testid^='listing-card']").all()
        for item in product:
            res={
                "product_name": await item.locator("p[style*='--max-line']").first.inner_text(),
                "price": await item.locator("p[title^='RM'], p[title*='free' i]").first.inner_text(),
                "link": f"https://www.carousell.com.my{await item.locator("a[href^='/p/']").first.get_attribute("href")}"
            }
            data.append(res)

        await browser.close()        

        #export to csv
        script_dir = Path(__file__).parent
        file_name = f"carousell_data_{search_content.replace(' ', '_')}.csv"
        file_path = script_dir / file_name
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["product_name", "price", "link"])
            writer.writeheader()
            writer.writerows(data)
        await browser.close()
        print("Total products found: ", len(data))
        print(f"Data has been exported to {file_path}")


if __name__ == "__main__":
    asyncio.run(main())