# SHA Hash Generator – Python

## Overview

This project is a **menu-driven SHA Hash Generator** implemented in Python.
It supports multiple Secure Hash Algorithm (SHA) variants and allows users to generate hashes for text and files, verify file integrity, and compare hash values.

The project demonstrates **modern cryptographic hashing techniques** used in cybersecurity for data integrity and verification.

---

## Objectives

* Understand Secure Hash Algorithms (SHA)
* Learn differences between SHA-1, SHA-256, and SHA-512
* Perform file and text hashing
* Verify file integrity using cryptographic hashes
* Practice modular and menu-driven Python programming

---

## Features

* Generate SHA hash for text
* Generate SHA hash for files
* Verify file integrity using SHA
* Compare two hash values
* Choose hashing algorithm dynamically
* Menu-driven command-line interface
* Proper error handling

---

## Supported Algorithms

| Algorithm | Hash Length | Status        |
| --------- | ----------- | ------------- |
| SHA-1     | 160-bit     | Deprecated    |
| SHA-256   | 256-bit     | Secure        |
| SHA-512   | 512-bit     | Highly Secure |

---

## Technologies Used

* Programming Language: Python 3
* Standard Libraries:

  * `hashlib`
  * `os`

No third-party libraries are required.

---

## Project Structure

```
SHA-Hash-Generator/
│
├── sha_hash_generator.py
├── README.md
└── sample.txt (optional)
```

---

## How SHA Works

* SHA is a family of cryptographic hash algorithms
* It generates a fixed-length hash regardless of input size
* A small change in input produces a completely different hash
* SHA hashes are one-way and irreversible
* SHA-256 and SHA-512 are widely used in modern security systems

---

## How to Run the Program

### Step 1: Verify Python Installation

```
python --version
```

### Step 2: Run the Program

```
python sha_hash_generator.py
```

---

## Menu Options Explained

1. **Generate SHA hash for text**
   Generates a SHA hash for user-provided text using the selected algorithm.

2. **Generate SHA hash for a file**
   Computes the SHA hash of a file by reading it in binary mode.

3. **Verify file integrity**
   Compares the current file hash with a known hash to detect tampering.

4. **Compare two hashes**
   Checks whether two hash values are identical.

5. **Exit**
   Safely terminates the program.

---

## Sample Use Case

* Generate a SHA-256 hash of an important file
* Store the hash securely
* Recalculate the hash later
* If hashes differ, the file has been modified

---

## Security Notes

* SHA-1 is no longer recommended for secure systems
* SHA-256 and SHA-512 are safe for integrity verification
* Hashing should not be confused with encryption
* Passwords should always be hashed with salt

---

## Limitations

* No salting mechanism included
* No real-time monitoring
* Command-line based interface only

---

## Future Enhancements

* Add salted password hashing
* Implement HMAC-SHA hashing
* Combine MD5 and SHA into one tool
* Add file integrity monitoring
* Add logging and reporting features

