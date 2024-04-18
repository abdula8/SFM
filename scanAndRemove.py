import os
import hashlib
import shutil

def get_file_hash(file_path):
    # Calculate the SHA-256 hash of the file
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        # Read the file in chunks to handle large files
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def find_similar_files(directory):
    # Create a dictionary to store file hashes and paths
    hash_table = {}

    # Traverse the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            # Calculate the hash value of the file
            file_hash = get_file_hash(file_path)
            # Check if the hash already exists in the hash table
            if file_hash in hash_table:
                # If the hash already exists, move the file to a backup directory
                backup_dir = os.path.join(directory, "similar_files_backup")
                if not os.path.exists(backup_dir):
                    os.mkdir(backup_dir)
                shutil.move(file_path, os.path.join(backup_dir, file_name))
            else:
                # If the hash doesn't exist, add it to the hash table
                hash_table[file_hash] = file_path

def main():
    directory = input("Enter the directory path to scan: ")
    find_similar_files(directory)
    print("Similar files have been processed. Duplicate files have been moved to a backup directory.")

if __name__ == "__main__":
    main()
