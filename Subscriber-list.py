from googleapiclient.discovery import build
import json
from google.oauth2.credentials import Credentials


with open('credentials.json') as f:
    credentials_data = json.load(f)
    a = credentials_data['installed']

credentials = Credentials.from_authorized_user_info(info=a)

youtube = build('youtube', 'v3', credentials=credentials)

channel = 'UC8Wx__5E_zUR8jQ4rkHMw-w'

response = youtube.subscriptions().list(
    part='subscriberSnippet',
    mySubscribers=True,
    maxResults=250,
).execute()

# subscriber_ids = [item['subscriberSnippet']['channelId'] for item in response.get('items', [])]
# # # subscriber_ids = [item['subscriberSnippet'] for item in response.get('items', [])]
# print(subscriber_ids)

# print(response)
# new_dumps = (json.dumps((response), sort_keys=True, indent=4, separators=(",", ": ")))
# print(new_dumps)

if 'items' in response:
    for item in response['items']:
        snippet = item['subscriberSnippet']
        subscriber_title = snippet['title']
        subscriber_id = snippet['channelId']
        print(f"Subscriber Title: {subscriber_title}, Subscriber ID: {subscriber_id}")
else:
    print("No subscribers found.")


