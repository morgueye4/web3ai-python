from web3ai.storage import LighthouseStorage
import os

def test_lighthouse_storage():
    # Replace with your Lighthouse API key
    API_KEY = "your_lighthouse_api_key"  # You should get this from environment variable in production
    
    # Initialize storage
    storage = LighthouseStorage(token=API_KEY)
    
    # Test 1: Simple print function
    print("\n=== Test 1: Print Function ===")
    storage.test()
    
    # Test 2: File Upload and Download
    print("\n=== Test 2: File Upload/Download ===")
    
    # Create test file
    test_file = "test_file.txt"
    test_content = "Hello, Web3AI Storage!"
    with open(test_file, 'w') as f:
        f.write(test_content)
    
    try:
        # Upload file
        print("Uploading file...")
        result = storage.upload_file(test_file)
        print(f"Upload result: {result}")
        
        if 'data' in result and 'Hash' in result['data']:
            cid = result['data']['Hash']
            print(f"File CID: {cid}")
            print(f"Access at: https://gateway.lighthouse.storage/ipfs/{cid}")
            
            # Download file
            print("\nDownloading file...")
            downloaded_file = "downloaded_test_file.txt"
            storage.download_file(cid, downloaded_file)
            
            # Verify content
            with open(downloaded_file, 'r') as f:
                downloaded_content = f.read()
            print(f"Original content: {test_content}")
            print(f"Downloaded content: {downloaded_content}")
            print(f"Content matches: {test_content == downloaded_content}")
            
    except Exception as e:
        print(f"Error during file operations: {str(e)}")
    
    # Test 3: Directory Upload
    print("\n=== Test 3: Directory Upload ===")
    
    # Create test directory with files
    test_dir = "test_dir"
    os.makedirs(test_dir, exist_ok=True)
    with open(f"{test_dir}/file1.txt", 'w') as f:
        f.write("Content of file 1")
    with open(f"{test_dir}/file2.txt", 'w') as f:
        f.write("Content of file 2")
    
    try:
        # Upload directory
        print("Uploading directory...")
        dir_result = storage.upload_directory(test_dir)
        print(f"Directory upload result: {dir_result}")
        
        if 'data' in dir_result and 'Hash' in dir_result['data']:
            dir_cid = dir_result['data']['Hash']
            print(f"Directory CID: {dir_cid}")
            print(f"Access at: https://gateway.lighthouse.storage/ipfs/{dir_cid}")
    
    except Exception as e:
        print(f"Error during directory operations: {str(e)}")
    
    # Cleanup
    print("\n=== Cleanup ===")
    try:
        os.remove(test_file)
        os.remove(downloaded_file)
        os.remove(f"{test_dir}/file1.txt")
        os.remove(f"{test_dir}/file2.txt")
        os.rmdir(test_dir)
        print("Cleanup completed successfully")
    except Exception as e:
        print(f"Error during cleanup: {str(e)}")

if __name__ == "__main__":
    test_lighthouse_storage() 