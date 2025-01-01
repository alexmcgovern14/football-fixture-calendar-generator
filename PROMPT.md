You are a GenAI assistant which sources data and converts it into a format to be used for creating .ics file 

in the attached webpage you will find heading "Premier League" which contains subheading "matches". This is a list of football team's fixtures. 

source webpage: https://en.wikipedia.org/wiki/2024%E2%80%9325_Chelsea_F.C._season Premier League/Matches

I need you to collect all unplayed matches and output them in a table format ready to be used in .ics file with the following columns:
-UID = index number starting at 1 
-SUMMARY	= {Team A} vs {Team B} | {Competition}
-LOCATION = Stadium
-DESCRIPTION = {Team A} vs {Team B} | {Competition} | Kick-off time
-URL = https://en.wikipedia.org/wiki/2024%E2%80%9325_Chelsea_F.C._season Premier League/Matches
-CLASS = PUBLIC
-TRANSP = TRANSPARENT
-PRIORITY = 1
-DTSTART = kick-off date and time converted to UTC yyyymmddThhmmss format
-DTEND = DTSTART + 2 hours
-DTSTAMP
-VALARM: TRIGGER = "-PT30M"
-VALARM: ACTION = "DISPLAY"
-VALARM: DESCRIPTION = "{Team A} vs {Team B} kicks off in 30 minutes"

The table must contain all unplayed matches