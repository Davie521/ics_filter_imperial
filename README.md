# iCalendar Event Filter

This Python script filters events from an iCalendar (.ics) file based on a list of keywords found in the event summaries. It creates a new .ics file containing only the events that *do not* match the specified keywords. This is useful for cleaning up calendars by removing unwanted or irrelevant entries.

## How it Works

The script reads an input .ics file, iterates through each event, and checks if its summary contains any of the predefined keywords (case-insensitively). If a keyword is found, the event is marked for removal. Finally, a new .ics file is created containing only the events that were not marked for removal.

## Requirements

*   Python 3.x
*   `icalendar` library: Install using pip: `pip install icalendar`

## Usage

1.  **Save the script:** Save the Python code as a `.py` file (e.g., `filter_calendar.py`).
2.  **Prepare your calendar:** Place the .ics file you want to filter (e.g., `calendar.ics`) in the same directory as the script.
3.  **Define keywords:** In the script, modify the `keywords` list to include the strings you want to filter out. Make sure the keywords are in lowercase for case-insensitive filtering.
4.  **Run the script:** Open a terminal or command prompt, navigate to the directory containing the script and your .ics file, and run the script using: `python filter_calendar.py`
5.  **Output:** The script will create a new .ics file named `modified_calendar.ics` in the same directory, containing the filtered events.

## Example

Let's say your `calendar.ics` contains events with the following summaries:

*   "Project Meeting"
*   "COMP60023 Lecture"
*   "Team Lunch"
*   "comp60033 Tutorial"

And your `keywords` list is:

```python
keywords = ['comp60023', 'comp60033']# ics_filter_imperial
