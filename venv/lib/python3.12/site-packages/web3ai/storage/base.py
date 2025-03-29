from abc import ABC, abstractmethod

class StorageProvider(ABC):
    @abstractmethod
    async def upload_file(self, file_path: str) -> dict:
        """Upload a single file to storage"""
        pass

    @abstractmethod
    async def upload_directory(self, dir_path: str) -> dict:
        """Upload a directory to storage"""
        pass

    @abstractmethod
    async def download_file(self, cid: str, output_path: str) -> None:
        """Download a file from storage"""
        pass

    @abstractmethod
    async def download_directory(self, cid: str, output_path: str) -> None:
        """Download a directory from storage"""
        pass

    @abstractmethod
    async def get_file_info(self, cid: str) -> dict:
        """Get information about a stored file"""
        pass

    @abstractmethod
    async def delete_file(self, cid: str) -> bool:
        """Delete a file from storage"""
        pass 