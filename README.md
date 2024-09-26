# Mastodon Pinning Bot

This is a Python script that interacts with the Mastodon API to manage pinned posts on a user account. The script can pin the latest post and a specific post, unpinning any currently pinned posts in the process.

## Features

- **Get the Latest Post:** Fetches the most recent post from the user's timeline.
- **Unpin All Posts:** Unpins all currently pinned posts.
- **Pin a Post by ID:** Pins a specific post given its ID.
- **Pin the Latest Post:** Pins the latest post automatically.
- **Pin Latest and Specific Post:** Unpins all posts, pins the latest post, and pins a specified post by ID.

## Requirements

- Python 3.x
- `mastodon.py` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Elytra15/mastodon-autopin.git
   cd mastodon-pinning-bot
   ```

2. Install the required Python package:

   ```bash
   pip install mastodon.py
   ```

3. Update the script with your Mastodon credentials:
   - Edit the script and fill in `MASTODON_URL` with your Mastodon instance URL.
   - Fill in `ACCESS_TOKEN` with your access token.
   - Replace `SPECIFIC_POST_ID` with the ID of the post you want to pin.

## Usage

To run the script, execute the following command:

```bash
python3 pin.py
```

### Example

Assuming your script is named `pin.py`, you would run:

```bash
python3 pin.py
```

## Setting Up with Cron

To automate the pinning process using `cron`, follow these steps:

1. Open the crontab editor:

   ```bash
   crontab -e
   ```

2. Add a new cron job. For example, to run the script every hour, add the following line:

   ```bash
   0 * * * * /usr/bin/python3 /path/to/your/script/pin.py
   ```

   Make sure to replace `/path/to/your/script/` with the actual path to your script.

3. Save and exit the editor.

## Notes

- Ensure your script has execute permissions:

  ```bash
  chmod +x pin.py
  ```

- Check your Mastodon API documentation for details on obtaining an access token and the limitations of the API.
  
## License

Free to use
