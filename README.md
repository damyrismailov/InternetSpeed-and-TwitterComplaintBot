# Internet Speed & Twitter Complaint Bot

Python automation script that measures current internet speed and, if it falls below a promised threshold, opens Twitter (X) and posts a complaint message. It combines web automation with Selenium, basic parsing of speed values, and conditional logic.

## Main features

- Opens an internet speed test site (e.g. Speedtest by Ookla) using Selenium.
- Starts the test, waits for the download and upload results to appear, and reads the numbers from the page.
- Converts the scraped text (e.g. `"85.23"`) into floats for comparison.
- Compares current speeds against configured minimum download and upload values (your “promised” speeds).
- If the speed is too low:
  - opens Twitter/X in the same browser session
  - logs in using stored credentials/profile (or a scripted login if configured)
  - composes a complaint tweet mentioning the provider and including the measured speeds.
- If the speed is acceptable, prints a message and does not post anything.
- Uses Selenium waits (`WebDriverWait`, `expected_conditions`) for:
  - Speed test “Go” button
  - Result elements (download / upload)
  - Tweet text area and “Post” button.
- Handles common Selenium exceptions to avoid random crashes while pages load or elements move.

## What I learned

- How to automate browser interactions across multiple websites within one Selenium session.
- How to read dynamic values from a web UI (speed test results) and convert them into usable data types.
- How to design a simple decision rule (if speed < threshold → take action, else skip).
- How to work with login flows and text inputs on modern web apps like Twitter/X.
- How fragile selectors and timing issues show up in real-world automation, and how `WebDriverWait` and proper exception handling make scripts more reliable.

## How to run

1. Clone the repo:

   git clone https://github.com/<your-username>/internet-speed-twitter-complaint.git  
   cd internet-speed-twitter-complaint  

2. (Optional) Create and activate a virtual environment:

   python -m venv venv  
   source venv/bin/activate   (Windows: venv\Scripts\activate)  

3. Install dependencies:

   pip install -r requirements.txt  

4. Configure settings in `main.py` (or in a config/env file, depending on how the script is written):

   - `PROMISED_DOWN` – minimum acceptable download speed (e.g. `150` for 150 Mbps).  
   - `PROMISED_UP` – minimum acceptable upload speed.  
   - Speed test URL (if you want to change from the default).  
   - Twitter/X login method:
     - either reuse a persistent Chrome profile (recommended)  
     - or set username/password and selectors for the login form.
   - Complaint message template (e.g. including provider handle and placeholders for measured speeds).

5. Run the script:

   python main.py  

   - Selenium will open the browser, run the speed test, and read the results.  
   - If speeds are below the promised thresholds, it will open Twitter/X and post the complaint message.  
   - If speeds meet or exceed the thresholds, it prints a summary and exits without posting.
