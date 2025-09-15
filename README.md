# Ubuntu Image Fetcher

## Overview
This Python script, `image_fetcher.py`, is a command-line tool for mindfully and safely downloading images from the web. It's designed to handle multiple URLs at once, prevent duplicate downloads, and implement crucial security checks to ensure a respectful and secure fetching process.

## Features
- **Batch Downloading**: Fetches images from multiple URLs provided by the user in a single command.
- **Duplicate Prevention**: Uses SHA256 hashing to identify and skip images that have already been downloaded, saving time and disk space.
- **Safety Precautions**: 
    - **URL Scheme Validation**: Ensures only `http` or `https` URLs are processed.
    - **Content-Type Check**: Verifies that the fetched file is an image (`image/`).
    - **Size Limit**: Skips files that exceed a predefined size limit (20MB) to prevent large or malicious downloads.
- **Robust Error Handling**: Provides clear and specific error messages for network issues, invalid URLs, or other problems, allowing for easy troubleshooting.
- **Respectful File Naming**: Infers the correct file extension from the HTTP headers if the URL doesn't provide one.
- **Organized Storage**: Automatically saves all fetched images into a dedicated `Fetched_Images` directory.

## Getting Started

### Prerequisites
- Python 3.6 or higher
- `requests` library

### Installation
You can install the required Python library using pip:
```bash
pip install requests
Usage
Run the script from your terminal:

Bash

python image_fetcher.py
When prompted, enter one or more image URLs, separated by a comma.

Bash

Please enter the image URLs, separated by a comma: [https://example.com/image1.jpg](https://example.com/image1.jpg), [https://example.com/image2.png](https://example.com/image2.png)
The script will display the status of each download and save the images to the Fetched_Images directory.

Code Structure
main() function: The core of the program, which handles user input, iterates through URLs, and calls the necessary functions for fetching and saving.

requests library: Used for all HTTP communication, including requests.head() for pre-download checks and requests.get() for fetching the full content.

os and urllib.parse: Used for file and directory management, and for parsing URLs to extract filenames.

hashlib: Employed to generate SHA256 hashes for duplicate image detection.

Contributing
We welcome contributions that align with the Ubuntu principles of community, respect, and mindfulness. If you have an idea for an improvement or a bug fix, please open an issue or submit a pull request.

License
This project is open-source. See the LICENSE file for more details.







