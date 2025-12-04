from __future__ import annotations

import os
import json

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# This scope lets you read YouTube data (including subscribers)
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]


def get_credentials() -> Credentials:
    creds = None

    # 1. Try to load existing user credentials from token.json
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # 2. If no creds, or they are invalid, refresh or run full OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh existing token
            creds.refresh(Request())
        else:
            # Run the OAuth flow using client secrets in credentials.json
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # 3. Save the authorized user credentials for next time
        with open("token.json", "w") as token_file:
            token_file.write(creds.to_json())

    return creds


def main():
    creds = get_credentials()

    youtube = build("youtube", "v3", credentials=creds)

    response = youtube.subscriptions().list(
        part="subscriberSnippet",
        mySubscribers=True,
        maxResults=250,
    ).execute()

    if "items" in response:
        for item in response["items"]:
            snippet = item["subscriberSnippet"]
            subscriber_title = snippet["title"]
            subscriber_id = snippet["channelId"]
            print(f"Subscriber Title: {subscriber_title}, Subscriber ID: {subscriber_id}")
    else:
        print("No subscribers found.")


if __name__ == "__main__":
    main()



