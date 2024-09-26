#!/usr/bin/env python3

from mastodon import Mastodon

MASTODON_URL = ''
ACCESS_TOKEN = ''

mastodon = Mastodon(
    access_token=ACCESS_TOKEN,
    api_base_url=MASTODON_URL
)

def get_latest_post():
    statuses = mastodon.account_statuses(mastodon.me()['id'], limit=1)
    return statuses[0] if statuses else None

def unpin_all():
    statuses = mastodon.account_statuses(mastodon.me()['id'], pinned=True)
    for status in statuses:
        mastodon.status_unpin(status['id'])

def pin_post_by_id(post_id):
    try:
        mastodon.status_pin(post_id)
        print(f"Successfully pinned post ID: {post_id}")
    except Exception as e:
        print(f"Error pinning post ID {post_id}: {e}")

def pin_latest_post():
    latest_post = get_latest_post()
    if latest_post:
        print(f"Pinning latest post: {latest_post['content']}")
        mastodon.status_pin(latest_post['id'])

def pin_latest_and_specific_post(specific_post_id):
    unpin_all()
    pin_latest_post()
    pin_post_by_id(specific_post_id)

if __name__ == "__main__":
    SPECIFIC_POST_ID = POST ID HERE
    pin_latest_and_specific_post(SPECIFIC_POST_ID)