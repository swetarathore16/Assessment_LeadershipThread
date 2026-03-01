from playwright.sync_api import Playwright, sync_playwright, expect


def run_negative(playwright: Playwright) -> p:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        # Step 1: Navigate to the site
        page.goto("https://automationintesting.online/", wait_until="domcontentloaded", timeout=30000)

        # Step 2: Scroll to booking section and select dates
        # Wait for the heading to be visible before interacting
        page.get_by_role("heading", name="Check Availability & Book").scroll_into_view_if_needed()

        # Fill check-in date (first textbox)
        checkin_box = page.get_by_role("textbox").first
        checkin_box.wait_for(state="visible", timeout=10000)
        checkin_box.click()
        page.get_by_role("gridcell", name="Choose Thursday, 5 March").click()

        # Fill check-out date (second textbox)
        checkout_box = page.get_by_role("textbox").nth(1)
        checkout_box.wait_for(state="visible", timeout=10000)
        checkout_box.click()
        page.get_by_role("gridcell", name="Choose Tuesday, 10 March").click()

        # Click Check Availability
        check_btn = page.get_by_role("button", name="Check Availability")
        check_btn.wait_for(state="visible", timeout=10000)
        check_btn.click()

        # Step 3: Select room — wait for results to load
        single_heading = page.get_by_role("heading", name="Single")
        single_heading.wait_for(state="visible", timeout=15000)
        expect(single_heading).to_be_visible()

        # Click "Book now" on the second result (index 1)
        book_link = page.get_by_role("link", name="Book now").nth(1)
        book_link.wait_for(state="visible", timeout=10000)
        book_link.click()

        # Step 4: Wait for reservation form
        book_heading = page.get_by_role("heading", name="Book This Room")
        book_heading.wait_for(state="visible", timeout=10000)
        expect(book_heading).to_be_visible()

        # Step 5: Submit form WITHOUT filling any fields
       
        page.get_by_role("button", name="Reserve Now").click(timeout=5000)
        


        # Step 6: Assert validation error messages are displayed
        # De-duplicated list — "must not be empty" appeared twice originally
        error_messages = [
            "Lastname should not be blank",
            "size must be between 3 and 18",
            "Firstname should not be blank",
            "must not be empty",
            "size must be between 11 and 21",
            "size must be between 3 and 30",
        ]

        for msg in error_messages:
            locator = page.get_by_text(msg, exact=False).first
            expect(locator).to_be_visible(timeout=8000)
            print(f"  Validation error found: '{msg}'")

        print(" Negative Scenario Passed: All Validation Errors Displayed Successfully")

    except Exception as e:
        print(f" Test Failed: {e}")
        # Take a screenshot on failure for debugging
        page.screenshot(path="failure_screenshot.png")
        raise

    finally:
        context.close()
        browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run_negative(playwright)