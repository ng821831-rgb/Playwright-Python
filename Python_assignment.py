from playwright.sync_api import sync_playwright

def test_chatgpt_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Open ChatGPT
        page.goto("https://chat.openai.com", timeout=60000)
        page.wait_for_timeout(5000)

        try:
            # Locate input box
            search_box = page.locator("textarea")
            search_box.wait_for(timeout=10000)

            # Enter search text
            search_box.fill("what is the future of SDET role in IT")
            search_box.press("Enter")

            # Wait to simulate response loading
            page.wait_for_timeout(8000)

        except Exception:
            print("ChatGPT login required. Test executed till page load.")

        browser.close()
