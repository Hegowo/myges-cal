from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz
import re

def parse_input(input_str):
    input_str = re.sub(r'\s{2,}', '   ', input_str.strip())
    
    parts = input_str.split('   ')
    
    if len(parts) != 5:
        raise ValueError("Erreur : L'entrée doit contenir 5 parties séparées par '   ' (trois espaces).")
    
    day = parts[0]
    schedule = parts[1]
    rooms = parts[2]
    name = parts[3]
    teacher = parts[4]
    
    return day, schedule, rooms, name, teacher

def format_date(date_str):
    return datetime.strptime(date_str, '%a, %B %d, %Y')

def format_time_range(time_range):
    start_time_str, end_time_str = time_range.split(' -> ')
    start_time = datetime.strptime(start_time_str, '%I:%M %p')
    end_time = datetime.strptime(end_time_str, '%I:%M %p')
    return start_time.time(), end_time.time()

def create_calendar_event(day, schedule, rooms, name, teacher):
    event_date = format_date(day)
    start_time, end_time = format_time_range(schedule)
    
    start_datetime = datetime.combine(event_date, start_time).replace(tzinfo=pytz.UTC)
    end_datetime = datetime.combine(event_date, end_time).replace(tzinfo=pytz.UTC)
    
    event = Event()
    event.add('summary', name)
    event.add('dtstart', start_datetime)
    event.add('dtend', end_datetime)
    event.add('location', rooms)
    event.add('description', f'Professeur : {teacher}')
    
    return event

def get_first_day_of_week(date):
    start_of_week = date - timedelta(days=date.weekday())
    return start_of_week

cal = Calendar()

dates = []

while True:
    input_str = input("Entrez les détails de l'événement (format brut de myges agenda ) ou tapez 'STOP' pour finir : ")
    
    if input_str.strip().upper() == 'STOP':
        break
    
    try:
        day, schedule, rooms, name, teacher = parse_input(input_str)
        
        dates.append(format_date(day))
        
        event = create_calendar_event(day, schedule, rooms, name, teacher)
        cal.add_component(event)
    
    except ValueError as e:
        print(e)

if dates:
    latest_date = max(dates)
    first_day_of_week = get_first_day_of_week(latest_date)
    file_name = f"Semaine du {first_day_of_week.strftime('%d %B %Y')}.ics"
else:
    file_name = 'my_event.ics'

with open(file_name, 'wb') as f:
    f.write(cal.to_ical())

print(f"Fichier {file_name} créé avec succès!")
