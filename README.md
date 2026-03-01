# Assessment_LeadershipThread
Qa Automation Assessment

# Playwright Python – Room Booking Automation

This project contains an end-to-end UI automation script written in **Python** using the **Playwright Sync API**.  
It validates the complete **room booking journey** on:

 https://automationintesting.online/

---

##  Objective
To automate and validate the critical booking flow:
- Date selection
- Room availability check
- Room booking
- Reservation form submission
- Booking confirmation

---

##  Test Scenario – Step by Step

1. Launch Chromium browser (headed mode)
2. Navigate to the application URL
3. Open **Check Availability & Book** section
4. Select **Check-in date**
5. Select **Check-out date**
6. Click **Check Availability**
7. Verify room availability
8. Select a room and click **Book now**
9. Verify **Book This Room** page
10. Submit reservation form
11. Validate successful booking

---

##  Automation Flow Covered

- Accessibility-first locators (`get_by_role`)
- Positive end-to-end booking scenario
- Negtive Scenario- validation on error message

---

## Execute the automation script:
python booking_test.py

What This One Command Does
- Creates a virtual environment
- Activates it
- Installs Playwright
- Installs browsers
- Executes the test