import requests
import os
from urllib.parse import urlparse
import hashlib

def main():
    """
    A tool for mindfully collecting images from the web, enhanced to handle
    multiple URLs, prevent duplicates, and implement safety checks.
    """
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get multiple URLs from the user
    urls_input = input("Please enter the image URLs, separated by a comma: ")
    urls = [url.strip() for url in urls_input.split(',')]
    
    # Create and maintain a set of hashes for downloaded images to prevent duplicates
    downloaded_hashes = set()
    
    for url in urls:
        if not url:
            continue
            
        print(f"\nAttempting to fetch: {url}")
        
        try:
            # Implement precautions for unknown sources
            # 1. Check for valid URL scheme (http/https) to avoid local file access or other schemes
            parsed_url = urlparse(url)
            if parsed_url.scheme not in ['http', 'https']:
                print(f"✗ Skipping {url}. Only HTTP/HTTPS URLs are supported for safety.")
                continue

            # 2. Check headers before downloading the full content
            with requests.head(url, timeout=10) as head_response:
                head_response.raise_for_status()
                content_type = head_response.headers.get('Content-Type', '')
                content_length = int(head_response.headers.get('Content-Length', 0))

                # Ensure it's an image and not too large
                if not content_type.startswith('image/'):
                    print(f"✗ Skipping {url}. Content-Type is not an image: {content_type}")
                    continue
                
                # Precaution: Set a reasonable size limit (e.g., 20 MB)
                if content_length > 20 * 1024 * 1024:
                    print(f"✗ Skipping {url}. File is too large ({content_length} bytes).")
                    continue
            
            # Fetch the image content
            response = requests.get(url, timeout=20)
            response.raise_for_status()
            
            # Generate a hash of the image content to check for duplicates
            image_hash = hashlib.sha256(response.content).hexdigest()
            
            if image_hash in downloaded_hashes:
                print(f"✓ Skipping {url}. This is a duplicate of a previously downloaded image.")
                continue
            
            # Create directory if it doesn't exist
            os.makedirs("Fetched_Images", exist_ok=True)
            
            # Extract filename from URL or generate one
            filename = os.path.basename(parsed_url.path)
            
            if not filename or '.' not in filename:
                # Add a default extension if none is present
                extension = content_type.split('/')[-1]
                filename = f"downloaded_image.{extension}"
            
            # Save the image
            filepath = os.path.join("Fetched_Images", filename)
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            # Add the hash to the set of downloaded images
            downloaded_hashes.add(image_hash)
            
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
            print("\nConnection strengthened. Community enriched.")
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")

if __name__ == "__main__":
    main()