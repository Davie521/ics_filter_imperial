# iCalendar Event Filter

This Python script filters events from an iCalendar (.ics) file based on a list of keywords found in the event summaries. It creates a new .ics file containing only the events that *do not* match the specified keywords. This is useful for cleaning up calendars by removing unwanted or irrelevant entries.

## How it Works

The script reads an input .ics file, iterates through each event, and checks if its summary contains any of the predefined keywords (case-insensitively). If a keyword is found, the event is marked for removal. Finally, a new .ics file is created containing only the events that were not marked for removal.

## Requirements

*   Python 3.x
*   `icalendar` library: Install using pip: `pip install icalendar`

## Usage

1.  **Save the script:** Save the Python code as a `.py` file (e.g., `filter_calendar.py`).
2.  **Prepare your calendar:** You need an .ics file to filter. See the section below on how to export a calendar from Microsoft Outlook. Place the .ics file (e.g., `calendar.ics`) in the same directory as the script.
3.  **Define keywords:** In the script, modify the `keywords` list to include the strings you want to filter out. Make sure the keywords are in lowercase for case-insensitive filtering.
4.  **Run the script:** Open a terminal or command prompt, navigate to the directory containing the script and your .ics file, and run the script using: `python filter_calendar.py`
5.  **Output:** The script will create a new .ics file named `modified_calendar.ics` in the same directory, containing the filtered events.

## Getting an .ics Link from Microsoft Outlook (Outlook on the Web)

This is the correct method to obtain an .ics link for your Outlook calendar:

1.  Log in to Outlook on the web (outlook.office.com).
2.  Click on the **Settings** gear icon (usually in the top right corner).
3.  At the bottom of the settings pane, click **View all Outlook settings**.
4.  In the Settings window, navigate to **Calendar** -> **Shared calendars**.
5.  Under the "Publish a calendar" section, select the calendar you want to export from the dropdown menu.
6.  Choose the permissions you want to grant (e.g., "Can view all details").
7.  Click **Publish**.
8.  You will now see two links: an HTML link and an **ICS link**. Copy the **ICS link**. This is the URL you can use to subscribe to or download the calendar data. You can paste this link into a browser to download the .ics file.

## Example

Let's say your `calendar.ics` contains events with the following summaries:

*   "Project Meeting"
*   "COMP60023 Lecture"
*   "Team Lunch"
*   "comp60033 Tutorial"

And your `keywords` list is:

```python
keywords = ['comp60023', 'comp60033']