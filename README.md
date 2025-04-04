# Web3 AI Python Library

A modular Python library for Web3 AI applications.

## Installation

Install directly from GitHub:
```bash
pip install git+https://github.com/gdaust/web3ai-python.git
```

## Usage

```python
import asyncio
from web3ai.storage import LighthouseStorage

async def main():
    # Initialize storage with your Lighthouse token
    storage = LighthouseStorage(token="your_lighthouse_token")

    # Upload a file
    result = await storage.upload_file("path/to/file")
    print(f"File uploaded with CID: {result['cid']}")

    # Upload a directory
    result = await storage.upload_directory("path/to/directory")
    print(f"Directory uploaded with CID: {result['cid']}")

    # Download a file
    await storage.download_file(result['cid'], "downloaded_file.txt")

    # Download a directory
    await storage.download_directory(result['cid'], "downloaded_directory")

    # Get file information
    info = await storage.get_file_info(result['cid'])
    print(f"File info: {info}")

    # Delete a file
    success = await storage.delete_file(result['cid'])
    print(f"File deleted: {success}")

    # Run test
    storage.test()

# Run the async main function
asyncio.run(main())
```

## Features

- File upload and download
- Directory upload and download
- File information retrieval
- File deletion
- Progress tracking (coming soon)
- Multiple storage provider support (coming soon)

## Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `python -m unittest discover`
