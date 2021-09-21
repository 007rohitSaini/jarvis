from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

"""Shows basic usage of the Google Calendar API.
Prints the start and name of the next 10 events on the user's calendar.
"""
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('calendar', 'v3', credentials=creds)

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time


def get_event_data():
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    res = []
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start = start.replace('+05:30', '')
        dt = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S')
        time = dt.strftime("%r")
        date = dt.strftime("%Y-%m-%d")
        ans = {"date": date, "time": time, "event": event['summary']}
        res.append(ans)
    return res


def insert(task):
    event = task
    event = service.events().insert(calendarId='primary', body=event).execute()
    return event.get('htmlLink')


if __name__ == '__main__':
    data = {
        'summary': 'Test',
        'location': 'Nalagarh',
        'description': 'Test to add data to calender',
        'start': {
            'dateTime': '2021-08-15T09:00:00',
            'timeZone': 'Asia/Kolkata',
        }, 'end': {
            'dateTime': '2021-08-15T09:30:00',
            'timeZone': 'Asia/Kolkata'
        }
    }
    #summary = insert(data)
    #print(summary)
    answer = get_event_data()
    print(answer)
