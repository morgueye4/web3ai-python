import unittest
import asyncio
from web3ai.storage import LighthouseStorage

class TestLighthouseStorage(unittest.TestCase):
    def setUp(self):
        self.storage = LighthouseStorage()
        self.loop = asyncio.get_event_loop()

    def test_module_print(self):
        """Test the simple print function"""
        self.storage.test()

    async def async_test_upload(self):
        """Test file upload"""
        result = await self.storage.upload_file("test.txt")
        self.assertIn("cid", result)

    def test_upload(self):
        """Run async upload test"""
        self.loop.run_until_complete(self.async_test_upload())

if __name__ == '__main__':
    unittest.main() 