import hashlib
import base58
import base64
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
        16: "md2",
        32: "md5",
        40: "sha1",
        64: "sha256",
        56: "sha224",
        96: "sha384",
        128: "sha512"
    }
    
    hash_length = len(hash_value)
    return hash_lengths.get(hash_length, "unknown")

def decode_hash(hash_type, hash_value, wordlist_path):
    plaintext = find_hash_match(hash_type, hash_value, wordlist_path)
    return plaintext

def decode_base32(encoded_value):
    return base64.b32decode(encoded_value).decode()

def decode_base45(encoded_value):
    return base64.b45decode(encoded_value).decode()

def decode_base58(encoded_value):
    return base58.b58decode(encoded_value).decode()

def decode_base64(encoded_value):
    return base64.b64decode(encoded_value).decode()

def clear_terminal():
    os.system('clear')  # For Linux/macOS
    # Alternatively, you can use os.system('cls') for Windows

def print_figlet_banner(text):
    os.system(f'figlet -c {text}')

if __name__ == "__main__":
    clear_terminal()
    print_figlet_banner("Hash Decoder")
    print("                      +------------------------------------+")
    print("                      |     Hash crack using python        |")
    print("                      |     Created By Rezwan              |")
    print("                      +------------------------------------+\n") 
    print("-----------------------------------------------------------------\n")
    
    hash_value = input("Enter the hash or encoded value: ")
    
    decoded_value = None
    hash_type = detect_hash_type(hash_value)
    
    if hash_type != "unknown":
        print(f"Detected hash type: {hash_type}")
        wordlist_path = "/usr/share/wordlists/rockyou.txt"
        decoded_value = decode_hash(hash_type, hash_value, wordlist_path)
    else:
        try:
            decoded_value = decode_base32(hash_value)
            print("Decoded using Base32:")
        except:
            pass
        
        try:
            decoded_value = decode_base45(hash_value)
            print("Decoded using Base45:")
        except:
            pass
        
        try:
            decoded_value = decode_base58(hash_value)
            print("Decoded using Base58:")
        except:
            pass
        
        try:
            decoded_value = decode_base62(hash_value)
            print("Decoded using Base62:")
        except:
            pass
        
        try:
            decoded_value = decode_base64(hash_value)
            print("Decoded using Base64:")
        except:
            pass
        
        
    if decoded_value is not None:
        print(decoded_value)
    else:
        print("No match or decoding available.")
