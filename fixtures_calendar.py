import csv
from datetime import datetime

def convert_to_ics(csv_file, calendar_name="Chelsea fixtures", output_file="events.ics"):
    events = []
    
    try:
        # Open the CSV file
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Validate date formats
                    datetime.strptime(row['DTSTART'], '%Y%m%dT%H%M%SZ')
                    datetime.strptime(row['DTEND'], '%Y%m%dT%H%M%SZ')
                    datetime.strptime(row['DTSTAMP'], '%Y%m%dT%H%M%SZ')
                    
                    # Process event
                    summary = row['SUMMARY']
                    color = row.get('COLOR', '#FFFFFF')  # Default to white if no color is provided
                    
                    event = f"""BEGIN:VEVENT
SUMMARY:{summary}
LOCATION:{row['LOCATION']}
DESCRIPTION:{row['DESCRIPTION']}
URL:{row['URL']}
CLASS:{row['CLASS']}
TRANSP:{row['TRANSP']}
PRIORITY:{row['PRIORITY']}
DTSTART:{row['DTSTART']}
DTEND:{row['DTEND']}
DTSTAMP:{row['DTSTAMP']}
X-COLOR:{color}
BEGIN:VALARM
TRIGGER:{row['VALARM:TRIGGER']}
ACTION:{row['VALARM:ACTION']}
DESCRIPTION:{row['VALARM:DESCRIPTION']}
END:VALARM
END:VEVENT"""
                    events.append(event)
                    print(f"Processed event: {summary}")
                except ValueError as e:
                    print(f"Skipping invalid row due to error: {e}")
        
        # Create the ICS file
        with open(output_file, 'w') as ics_file:
            ics_file.write("BEGIN:VCALENDAR\n")
            ics_file.write("VERSION:2.0\n")
            ics_file.write(f"X-WR-CALNAME:{calendar_name}\n")
            ics_file.write("\n".join(events))
            ics_file.write("\nEND:VCALENDAR")
        
        print(f"{len(events)} events processed.")
        print(f"ICS file '{output_file}' created successfully.")
    
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except KeyError as e:
        print(f"Error: Missing column in CSV file: {e}")

# Example usage
convert_to_ics("fixtures_calendar.csv")