from lighthouseweb3 import Lighthouse
from .base import StorageProvider

class LighthouseStorage(StorageProvider):
    def __init__(self, token: str = None):
        """Initialize Lighthouse storage with optional token"""
        self.client = Lighthouse(token=token)
    
    def upload_file(self, file_path: str) -> dict:
        """Upload a single file to Lighthouse storage
        Returns:
            dict: Contains upload result with CID in data.Hash
        """
        result = self.client.upload(source=file_path)
        return result
    
    def upload_directory(self, dir_path: str) -> dict:
        """Upload a directory to Lighthouse storage
        Returns:
            dict: Contains upload result with CID in data.Hash
        """
        result = self.client.upload(source=dir_path)
        return result

    def download_file(self, cid: str, output_path: str) -> None:
        """Download a file from Lighthouse storage"""
        gateway_url = f"https://gateway.lighthouse.storage/ipfs/{cid}"
        import requests
        response = requests.get(gateway_url)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
        else:
            raise Exception(f"Download failed with status code: {response.status_code}")

    def download_directory(self, cid: str, output_path: str) -> None:
        """Download a directory from Lighthouse storage"""
        # Same as file download for now
        self.download_file(cid, output_path)

    def get_file_info(self, cid: str) -> dict:
        """Get information about a stored file"""
        # This would need to be implemented based on Lighthouse API capabilities
        gateway_url = f"https://gateway.lighthouse.storage/ipfs/{cid}"
        return {"cid": cid, "gateway_url": gateway_url}

    def delete_file(self, cid: str) -> bool:
        """Delete a file from Lighthouse storage"""
        # Note: Actual deletion might not be possible with basic Lighthouse SDK
        # This is a placeholder implementation
        return True

    def test(self):
        """Simple test function"""
        print("Hello from Storage Module") 