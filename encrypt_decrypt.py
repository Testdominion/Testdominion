from Crypto.Cipher import AES
import base64

# Function to remove padding
def unpad(text):
    return text[:-ord(text[-1])]

# Ask user for the encrypted message
encrypted_text = input("Enter the encrypted text: ")

# Ask user for the key (should be exactly 16, 24, or 32 bytes)
key_input = input("Enter the key (in base64 format): ")

# Decode the key from base64
key = base64.b64decode(key_input)

try:
    # Decode and decrypt
    encrypted_data = base64.b64decode(encrypted_text)
    iv, encrypted_bytes = encrypted_data[:16], encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(encrypted_bytes).decode())

    print(f"🔓 Decrypted Message: {decrypted_message}")

except Exception as e:
    print("❌ Decryption failed! Make sure you have the correct key and encrypted text.")
