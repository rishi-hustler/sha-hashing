import hashlib
import os

def get_sha_object(algorithm):
    """
    Returns a hashlib SHA object based on user choice
    """
    if algorithm == "1":
        return hashlib.sha1()
    elif algorithm == "2":
        return hashlib.sha256()
    elif algorithm == "3":
        return hashlib.sha512()
    else:
        return None


def sha_hash_text(text, algorithm):
    """
    Generate SHA hash for a given text
    """
    sha = get_sha_object(algorithm)
    if sha is None:
        return None

    sha.update(text.encode("utf-8"))
    return sha.hexdigest()


def sha_hash_file(file_path, algorithm):
    """
    Generate SHA hash for a file
    """
    sha = get_sha_object(algorithm)
    if sha is None:
        return None

    try:
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha.update(chunk)
        return sha.hexdigest()

    except FileNotFoundError:
        return None


def verify_file_integrity(file_path, known_hash, algorithm):
    """
    Verify file integrity using SHA hash
    """
    current_hash = sha_hash_file(file_path, algorithm)
    if current_hash is None:
        return None

    return current_hash == known_hash


def display_algorithm_menu():
    print("\nSelect SHA Algorithm")
    print("1. SHA-1")
    print("2. SHA-256")
    print("3. SHA-512")


def display_main_menu():
    print("\n================ SHA HASH GENERATOR =================")
    print("1. Generate SHA hash for text")
    print("2. Generate SHA hash for a file")
    print("3. Verify file integrity")
    print("4. Compare two hashes")
    print("5. Exit")
    print("====================================================")


def main():
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-5): ")

        if choice in ["1", "2", "3"]:
            display_algorithm_menu()
            algorithm = input("Select algorithm (1-3): ")

            if algorithm not in ["1", "2", "3"]:
                print("Invalid algorithm selection.")
                continue

        if choice == "1":
            text = input("\nEnter text to hash: ")
            hash_result = sha_hash_text(text, algorithm)
            print("Generated Hash:", hash_result)

        elif choice == "2":
            file_path = input("\nEnter file path: ")

            if not os.path.exists(file_path):
                print("File does not exist.")
            else:
                hash_result = sha_hash_file(file_path, algorithm)
                print("Generated Hash:", hash_result)

        elif choice == "3":
            file_path = input("\nEnter file path: ")
            known_hash = input("Enter known hash: ")

            result = verify_file_integrity(file_path, known_hash, algorithm)

            if result is None:
                print("File not found.")
            elif result:
                print("File integrity verified. Hashes match.")
            else:
                print("File integrity compromised. Hashes do not match.")

        elif choice == "4":
            hash1 = input("\nEnter first hash: ")
            hash2 = input("Enter second hash: ")

            if hash1 == hash2:
                print("Hashes are identical.")
            else:
                print("Hashes are different.")

        elif choice == "5":
            print("\nExiting SHA Hash Generator.")
            break

        else:
            print("Invalid choice. Please select between 1-5.")


if __name__ == "__main__":
    main()
