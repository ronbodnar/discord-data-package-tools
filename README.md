# Discord Data Package Tools

A collection of Python scripts to interact with Discord data packages. These scripts help extract and organize information from Discord data for further analysis.

## Attachment Downloader

This script is used to download attachment files from Discord data packages.

### Usage

1. Place this script inside a directory containing the extracted "package" folder from Discord.
2. Run the script.

```bash
python attachment_downloader.py
```

### How it Works

The script scans CSV files in the Discord package data directory for attachment links. It then downloads the attachments and saves them to the "attachments" directory.

### Notes

- Multiple attachments in a message are split using delimiters such as '& ' or ','.
- The script generates an "attachment-links.csv" file containing all attachment links.

## Message Aggregator

This script aggregates messages from the Discord data package into a single CSV file.

### Usage

1. Place this script inside a directory containing the extracted "package" folder from Discord.
2. Run the script.

```bash
python message_aggregator.py
```

### How it Works

The script aggregates messages from multiple CSV files in the Discord package data directory into a single CSV file named "messages.csv." It also provides statistics on the total number of unique conversations, total messages found, and total messages containing attachments.

### Notes

- The script skips headers and extracts necessary information from each CSV file.
- The resulting "messages.csv" file contains columns for correspondent ID, message ID, timestamp, user ID, and message content.

## Prerequisites

- Python 3.x
- Dependencies: `os`, `csv`, `requests` (for Attachment Downloader)

## Author

- [Ron Bodnar](https://github.com/ronbodnar)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Important

Use these scripts responsibly and comply with Discord's terms of service.
