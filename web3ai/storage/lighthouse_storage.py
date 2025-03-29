from filecoin_storage import FilecoinStorage, ProviderType
from .base import StorageProvider

class LighthouseStorage(StorageProvider):
    def __init__(self, token: str = None):
        """Initialize Lighthouse storage with optional token"""
        self.client = FilecoinStorage(
            lighthouse_api_key=token,
            default_provider=ProviderType.LIGHTHOUSE
        )
    
    async def upload_file(self, file_path: str) -> dict:
        """Upload a single file to Lighthouse storage"""
        cid = await self.client.upload_file(file_path)
        return {"cid": cid}
    
    async def upload_directory(self, dir_path: str) -> dict:
        """Upload a directory to Lighthouse storage"""
        cid = await self.client.upload_directory(dir_path)
        return {"cid": cid}

    async def download_file(self, cid: str, output_path: str) -> None:
        """Download a file from Lighthouse storage"""
        await self.client.download_file(cid, output_path)

    async def download_directory(self, cid: str, output_path: str) -> None:
        """Download a directory from Lighthouse storage"""
        await self.client.download_directory(cid, output_path)

    async def get_file_info(self, cid: str) -> dict:
        """Get information about a stored file"""
        return await self.client.get_file_info(cid)

    async def delete_file(self, cid: str) -> bool:
        """Delete a file from Lighthouse storage"""
        return await self.client.delete_file(cid)

    def test(self):
        """Simple test function"""
        print("Hello from Storage Module") 