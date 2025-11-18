from googleapiclient.discovery import build

api_key = 'AIzaSyA-fDSFGhySHwNcQMixvge_BSuI8xC-gsY'

youtube = build('youtube', 'v3', developerKey=api_key)
channel_id = 'UC8Wx__5E_zUR8jQ4rkHMw-w'

response = youtube.channels().list(
    part='statistics',
    id=channel_id

).execute()

stats = response['items'][0]['statistics']

subscriber_count = stats.get('subscriberCount', 'Unknown')
video_count = stats.get('videoCount', 'Unknown')
view_count = stats.get('viewCount', 'Unknown')


print("Subscribers:",int(subscriber_count))
print("Videos on channel:",int(video_count))
print("Total Views:",int(view_count))

# from googleapiclient.discovery import build
#
# api_key = 'AIzaSyA-fDSFGhySHwNcQMixvge_BSuI8xC-gsY'
#
# youtube = build('youtube', 'v3', developerKey=api_key)
# channel_id = 'UC8Wx__5E_zUR8jQ4rkHMw-w'
#
# # Retrieve the user IDs of subscribers
# response = youtube.subscriptions().list(
#     part='subscriberSnippet',
#     mySubscribers=True,
#     maxResults=50  # Adjust as needed
# ).execute()
#
# # Extract the user IDs from the response
# subscriber_ids = [item['subscriberSnippet']['resourceId']['channelId'] for item in response.get('items', [])]
#
# # Print the subscriber IDs
# for idx, subscriber_id in enumerate(subscriber_ids, start=1):
#     print(f"Subscriber {idx}: {subscriber_id}")





