from icalendar import Calendar, Event
import os

# Ensure the file path is correct
file_path = 'calendar.ics'
if not os.path.exists(file_path):
    print(f"The file {file_path} does not exist. Please check the file path.")
else:
    # Load your ICS file
    with open(file_path, 'rb') as file:
        cal = Calendar.from_ical(file.read())

    # Define keywords or phrases to search for in the summary
    keywords = [
        'comp60023', 'comp60033', 'comp60032', 'comp70015', 'comp60001', 'comp60023',
        'comp60029',
        'co horizons courses', 'co horizons year-in-europe language classes - for info',
        'comp60006', 'comp70089', 'computer vision',
        'comp60017', 'comp70075', 'system performance engineering',
        'comp60008', 'comp70070', 'custom computing',
        'comp60003', 'communicating computer science in schools',
        'comp60005', 'comp70090', 'graphics'
    ]

    events_to_keep = []
    count_removed = 0

    for component in cal.walk():
        if component.name == "VEVENT":
            # Normalize the summary for case-insensitive comparison
            summary = component.get('summary').strip().lower() if component.get('summary') else ''
            # Check if any keyword is in the summary
            if any(keyword in summary for keyword in keywords):
                count_removed += 1
            else:
                events_to_keep.append(component)

    print(f"Number of events removed: {count_removed}")

    # Create a new calendar
    new_cal = Calendar()
    for component in events_to_keep:
        new_cal.add_component(component)

    # Save the modified calendar
    new_filename = 'modified_calendar.ics'
    with open(new_filename, 'wb') as file:
        file.write(new_cal.to_ical())
    
    print(f"Modified calendar saved as {new_filename}.")