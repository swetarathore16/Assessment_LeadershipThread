from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://automationintesting.online/")

    # Booking dates
    page.get_by_role("heading", name="Check Availability & Book").click()
    page.get_by_role("textbox").first.click()
    page.get_by_role("gridcell", name="Choose Thursday, 5 March").click()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("gridcell", name="Choose Tuesday, 10 March").click()
    page.get_by_role("button", name="Check Availability").click()

    # Select room
    expect(page.get_by_role("heading", name="Single")).to_be_visible()
    page.wait_for_timeout(2000)
    page.get_by_role("link", name="Book now").nth(1).click()

    # Fill reservation form
    expect(page.get_by_role("heading", name="Book This Room")).to_be_visible()
    page.get_by_role("button", name="Reserve Now").click()
    page.wait_for_timeout(2000)
    page.get_by_role("textbox", name="Firstname").fill("TestQA2")
    page.get_by_role("textbox", name="Lastname").fill("Singh1")
    page.get_by_role("textbox", name="Email").fill("test2@mailinator.com")
    page.get_by_role("textbox", name="Phone").fill("89999999989")
    page.wait_for_timeout(3000)
    
    # Reserve
    page.get_by_role("button", name="Reserve Now").click()
    expect(page.get_by_role("link", name="Return home")).to_be_visible()
    
    print("UserFlow -Test Passed ")

    #context.close()
    #browser.close()
with sync_playwright() as playwright:
    run(playwright)
