import hashlib
import os

def find_hash_match(hash_type, hash_value, wordlist_path):
    with open(wordlist_path, 'r', errors='ignore') as wordlist:
        for line in wordlist:
            word = line.strip()
            hashed_word = hashlib.new(hash_type, word.encode()).hexdigest()
            if hashed_word == hash_value:
                return word
    return None

def detect_hash_type(hash_value):
    hash_lengths = {
        32: "md5",
        40: "sha1",
        64: "sha256",
        56: "sha224",
        96: "sha384"
    }
    
    hash_length = len(hash_value)
    return hash_lengths.get(hash_length, "unknown")

def decode_hash(hash_type, hash_value, wordlist_path):
    plaintext = find_hash_match(hash_type, hash_value, wordlist_path)
    return plaintext

def clear_terminal():
    os.system('clear')  # For Linux/macOS
    # Alternatively, you can use os.system('cls') for Windows

if __name__ == "__main__":
    clear_terminal()
    print("                            Hash Decoder and Matcher")
    print("                      +------------------------------------+")
    print("                      |     Hash crack using python        |")
    print("                      |     Created By Rezwan              |")
    print("                      +------------------------------------+")
 
    hash_value = input("Enter the hash value: ")
    detected_hash_type = detect_hash_type(hash_value)
    
    if detected_hash_type == "unknown":
        print("Unknown hash type based on hash length.")
    else:
        print(f"Detected hash type: {detected_hash_type}")
        
        wordlist_path = "/usr/share/wordlists/rockyou.txt"
        plaintext = decode_hash(detected_hash_type, hash_value, wordlist_path)
        
        if plaintext:
            print(f"\nDecoded plaintext: {plaintext}")
        else:
            print("\nNo match found using the provided hash type and wordlist.")
