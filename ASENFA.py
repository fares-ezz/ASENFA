import secrets
import random
from hlp import shfit , unshfit 
from animation import draw
import socket
import time
import dicit_math
s = {0: "~", 1: "?", 2: ")", 3: ".", 4: "|", 5: "&", 6: "!", 7: "#", 8: "^", 9: "@"}
s1 = {0: "?", 1: ")", 2: ".", 3: "|", 4: "&", 5: "!", 6: "#", 7: "^", 8: "@", 9: "~"}
s2 = {0: ")", 1: ".", 2: "|", 3: "&", 4: "!", 5: "#", 6: "^", 7: "@", 8: "~", 9: "?"}
s3 = {0: ".", 1: "|", 2: "&", 3: "!", 4: "#", 5: "^", 6: "@", 7: "~", 8: "?", 9: ")"}
s4 = {0: "|", 1: "&", 2: "!", 3: "#", 4: "^", 5: "@", 6: "~", 7: "?", 8: ")", 9: "."}
s5 = {0: "&", 1: "!", 2: "#", 3: "^", 4: "@", 5: "~", 6: "?", 7: ")", 8: ".", 9: "|"}
s6 = {0: "!", 1: "#", 2: "^", 3: "@", 4: "~", 5: "?", 6: ")", 7: ".", 8: "|", 9: "&"}
s7 = {0: "#", 1: "^", 2: "@", 3: "~", 4: "?", 5: ")", 6: ".", 7: "|", 8: "&", 9: "!"}
s8 = {0: "^", 1: "@", 2: "~", 3: "?", 4: ")", 5: ".", 6: "|", 7: "&", 8: "!", 9: "#"}
s9 = {0: "@", 1: "~", 2: "?", 3: ")", 4: ".", 5: "|", 6: "&", 7: "!", 8: "#", 9: "^"}

option = {1: s1, 2: s2, 3: s3, 4: s4, 5: s5, 6: s6, 7: s7, 8: s8, 9: s9, 10: s}

def fakesize() :
    key = secrets.randbits(1024)
    return key
def generate_key(length : int):
    """
    Function: generate_key
    ----------------------
    Generates a cryptographic random key of a specific bit length
    based on the user's selected option.

    Parameters:
        length (int): Determines the bit-length of the key to generate.
                      Acceptable values:
                        1 → 2048-bit key
                        2 → 3072-bit key
                        3 → Randomly chooses between 2048 or 3072 bits

    Returns:
        int: A randomly generated integer representing the cryptographic key.

    Behavior:
        • Uses Python's 'secrets' module for secure random number generation.
        • Prints an error message if 'length' is outside the range (1–3).
        • Ensures unpredictable, cryptographically secure key material.

    Example:
        >>> key1 = generate_key(1)
        >>> key2 = generate_key(2)
        >>> key3 = generate_key(3)
        >>> print(key1.bit_length())  # 2048
        >>> print(key2.bit_length())  # 3072 or 2048
    """

    length = length 
    if length == 1 :  
        key = secrets.randbits(2048) 
        return key
    elif length == 2 :     
        key = secrets.randbits(1024)
        return key
    elif length == 3 :     
        allowed_sizes = [2048, 1024]
        key_size = secrets.choice(allowed_sizes)  
        key = secrets.randbits(key_size) 
        return key
    else :
        print(f"Erorr occurred Because the length parameter must between 1 to 3 numbers")

def encriptkey_main(len_key:int):
 
    """
    Function: encriptkey_main
    -------------------------
    Generates and encodes an encryption key using a combination of:
        - Fake random data (to obscure true key size)
        - Transformation and substitution operations
        - Random key-generation rules

    Parameters:
        len_key (int): Indicates the desired key size mode.
                       Usually 1 = 2048-bit, 2 = 3072-bit.

    Returns:
        tuple:
            (
                enc_key (str): Final encoded encryption key (string format),
                key (int): Original numeric cryptographic key,
                num_of_gen (int): Number of total keys to generate (3 or 4),
                drop_key (int): Index of key to drop from the key exchange
            )

    Process Description:
        1. Generate a large random "fake" number (via fakesize()) to act as noise.
        2. Adjust its length to be within expected bounds (≈308 digits).
        3. Extract pattern-based control values (num, op, num_of_gen, drop_key)
           by scanning the digits of the fake number.
        4. Generate a real cryptographic key using `generate_key(len_key)`.
        5. Shift and map digits of the key using substitution dictionaries (`option`, `s`).
        6. Combine the transformed real key and fake list to produce the final encoded key.
        7. Return the encoded key and parameters used for synchronization with the receiver.

    Example:
        >>> enc_key, key, num_of_gen, drop_key = encriptkey_main(1)
        >>> print(len(enc_key))
        >>> print(num_of_gen, drop_key)
    """    
    
    # --- STEP 1: Generate fake number sequence to obscure the key structure ---
    fake_len = fakesize() # external function expected to return a large integer

    # --- STEP 2: Normalize fake list length around 308 digits ---
    list_fake_list = list(str(fake_len))
    if len(list_fake_list) == 309 :
        list_fake_list.pop()
    elif len(list_fake_list) == 307 :
        fake_num = random.randint(0,9) # to handle number of fake list by adding him
        list_fake_list.append(fake_num) 


    sh_f = list_fake_list # alias for clarity
    
    # --- STEP 3: Extract pattern-based control numbers from fake data ---
    for ind , val in enumerate(sh_f):
        if val == "0" :
            num = int(list_fake_list[ind+1])
            break
    if num == 0 : 
        num = 2 
    for ind , val in enumerate(sh_f):
        if val == "1" :
            op=int(sh_f[ind+1])
            break
    if op == 0 : 
        op = 3  
    for ind , val in enumerate(reversed(sh_f)):
        if val == "7" :
            num_of_gen=int(sh_f[ind+1])
            break
    if  5 <= num_of_gen <= 7  or num_of_gen == 0 or num_of_gen == 1 or num_of_gen == 2  :
        num_of_gen = 3
    elif num_of_gen > 7  or num_of_gen == 4:
        num_of_gen = 4    
    for ind , val in enumerate(reversed(sh_f)):
        if val == "8" :
            drop_key=int(sh_f[ind+1])
            break
    if drop_key == 0 :
        drop_key = 1
    elif 2 <= drop_key <=6 :
            drop_key = 2 
    elif drop_key > 6 :
        if num_of_gen == 4  :
            drop_key = 3
        else :
            drop_key = 1  

    # --- STEP 4: Generate the actual encryption key ---                   
    key = generate_key(len_key)
    list_key = list(str(key))

    # --- STEP 5: Shift key digits using calculated offset ---
    l_k = shfit(list_key,num)
    # --- STEP 6: Apply digit substitution based on operation mapping ---
    list_map =  option[op]   
    for index , value in enumerate(l_k) :
        for k , v in list_map.items():
            if int(value) == k :
                l_k[index] = v           
    # --- STEP 7: Apply substitution mapping to fake number as well ---               
    for index , value in enumerate(sh_f) :
        for k , v in s.items():
            if int(value) == k :
                sh_f[index] = v      
    #STEP 8: Combine both lists and finalize encoded key ---                  
    final_list = l_k+sh_f
    enc_key = "".join(final_list)
    
    return enc_key , key , num_of_gen , drop_key   


def decript_key(key : str) :
    """
    Function: decript_key
    ---------------------
    Decrypts an encrypted key produced by the `encriptkey_main()` function
    by reversing the fake padding, mapping, and shifting transformations.

    Parameters:
        key (str): The full encrypted key string generated by `encriptkey_main()`.
                   This string contains both:
                        - The real encrypted key (main section)
                        - The fake data (last 308 characters) used to obfuscate it.

    Returns:
        tuple:
            (
                result (int): The original decrypted key (integer form).
                number_of_keys (int): Indicates the number of key blocks used in generation.
                number_drop_key (int): Indicates the key-drop method applied.
            )

    Core Logic:
        1. Splits the input key into:
             • The fake portion (last 308 chars)
             • The real encrypted key portion (the rest)
        2. Reverses the mapping applied during encryption using dictionary `s`
        3. Extracts control parameters embedded in the fake data:
             • `sh_num` → shift value
             • `map_num` → mapping table number
             • `number_of_keys` → number of key blocks generated
             • `number_drop_key` → defines post-generation drop behavior
        4. Restores all values to valid ranges (corrects 0s and limits)
        5. Reconstructs the original key by:
             • Reversing symbol-to-number mapping (`option`)
             • Undoing the shift using `unshfit()`
        6. Converts the recovered digit list back into an integer key.

    Dependencies:
        - `option` : A dictionary of encryption mapping tables
        - `s`      : A dictionary used for symbol encoding in fake data
        - `unshfit(list, shift)` : Function that undoes the shifting operation
                                   applied in `encriptkey_main()`

    Example:
        >>> enc_key, original_key, num_gen, drop_key = encriptkey_main(1)
        >>> dec_key, num_of_keys, number_drop_key = decript_key(enc_key)
        >>> print(dec_key == original_key)
        True

    Notes:
        • The function is tightly coupled with `encriptkey_main()`.
        • The fake padding section is always expected to be 308 characters long.
        • The structure of dictionaries `s` and `option` must be consistent with encryption.
    """
    # Initialize all control variables
    sh_num , map_num ,number_of_keys ,number_drop_key =  0 , 0 , 0 , 0 
    # Split real key and fake padding (last 308 chars are fake)
    list_key = list(key)
    fakekey_list = list_key[-308 : ]
    real_key = list(list_key[:-308])
    # Reverse the fake symbol encoding (using dictionary `s`)
    for index , value in enumerate(fakekey_list) :
        for k , v in s.items():
            if value == v :
                fakekey_list[index] = k 
    # Extract embedded control parameters from fake section            
    for ind , val in enumerate(fakekey_list):
        if val == 0:
            sh_num = fakekey_list[ind+1]
            break
    for ind , val in enumerate(fakekey_list):
        if val == 1 :
            map_num = fakekey_list[ind+1]
            break
    for ind , val in enumerate(reversed(fakekey_list)):
        if val == 7 :
            number_of_keys = fakekey_list[ind+1]
            break
    for ind , val in enumerate(reversed(fakekey_list)):
        if val == 8 :
            number_drop_key = fakekey_list[ind+1]
            break
    # Extract embedded control parameters from fake section    
    if sh_num == 0 : 
        sh_num = 2
    if map_num == 0 : 
        map_num = 3
    if  5 <= number_of_keys  <= 7  or number_of_keys  == 0 or number_of_keys  == 1 or number_of_keys  == 2  :
        number_of_keys  = 3
    elif number_of_keys  > 7  or number_of_keys  == 4:
        number_of_keys  = 4 
    if number_drop_key == 0 :
        number_drop_key = 1
    elif 2 <= number_drop_key <=6 :
            number_drop_key = 2 
    elif number_drop_key > 6 :
        if number_of_keys == 4  :
            number_drop_key = 3
        else :
            number_drop_key = 1 
    # Reverse mapping using selected map table        
    ma_p = option[map_num]        
    for index , value in enumerate(real_key) :
        for k , v in ma_p.items():
            if value == v :
                real_key[index] = k
    list_key = unshfit(real_key , sh_num)            
    result = int(''.join(map(str, list_key)))            
    return result , number_of_keys , number_drop_key                   
    


import socket
import time

# ---------------- SENDER ---------------- #
def sender(ip="127.0.0.1", port=5000):


    """
    Function: sender
    ----------------
    Establishes a connection to the receiver, performs a key exchange,
    and sends an encrypted message.

    Parameters:
        ip   (str): IP address of the receiver (default: "127.0.0.1")
        port (int): Port number of the receiver (default: 5000)

    Flow:
        1. Connects to receiver.
        2. Prompts user to select key length (1=2048, 2=3072).
        3. Sends chosen length to receiver.
        4. Exchange keys with the Reciver To Encript The Message.
        5. If valid, proceeds with key exchange and encrypted message sending.
        6. Closes socket after transmission.

    Returns:
        None
    """
        
    time.sleep(1)  # give receiver time to start
    draw()
    print("Hello To My Small Script ASENFA ...\n")

    print("Hello To My Small Script ASENFA I Create To This will reinforce important concepts \n such as encryption and decryption and how it all works.\n I hope you have a pleasant experience\n")
    len_key = input(
        "Choose Length Of Key That Used To Encript 2048 Press 1 or if you Want The That Used To Encript 3072 Press 2 :  \n"
    ).strip()
    time.sleep(1)
    # Connect first, then send the choice immediately
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        print(f"Sender connected to {ip}:{port}")
    except Exception as e:
        print("Could not connect to receiver:", e)
        return

    # Send length-of-key choice first
    client.sendall(len_key.encode())
    print("Sender sent length of keys:", repr(len_key))

    # Wait for receiver acknowledgement or rejection
    try:
        ack = client.recv(1024).decode().strip()
    except Exception as e:
        print("Error waiting for receiver response:", e)
        client.close()
        return

    if ack == "INVALID":
        print("Receiver rejected length of key. Closing connection.")
        client.close()
        return
    elif ack == "OK":
        print("Receiver accepted length of key. Continuing key exchange...")
    else:
        # unexpected response — be defensive and close
        print("Unexpected response from receiver:", repr(ack))
        client.close()
        return

    # ----- proceed with existing key-exchange logic -----
    exchanged = []
    enc_key, main_key, number_of_keys, number_drop_key = encriptkey_main(int(len_key))

    time.sleep(1)
    client.sendall(enc_key.encode())  # send 1st
    exchanged.append(main_key)
    print("Sender sent key #1")

    time.sleep(1)
    data = client.recv(3072)
    key1, _, _ = decript_key(data.decode())
    exchanged.append(key1)
    print("Sender got key #2:", key1)

    time.sleep(1)
    enc_key2, main_key2, _, _ = encriptkey_main(int(len_key))
    client.sendall(enc_key2.encode())  # send 3rd
    exchanged.append(main_key2)
    time.sleep(1)
    print("Sender sent key #3")

    if number_of_keys == 4:
        data = client.recv(3072)
        key2, _, _ = decript_key(data.decode())
        exchanged.append(key2)
        time.sleep(1)
        print("Sender got key #4:", key2)

    # ---- Cleanup keys ----
    print("\nSender exchanged keys:", exchanged)
    print(f"drop Key {number_drop_key}")
    exchanged[number_drop_key] = 0
    exchanged.remove(0)
    time.sleep(1)
    print("Final keys:", exchanged)

    # ---- Send encrypted message (same socket) ----
    plain_text = input("Enter message to send: ")
    encrypted_text = dicit_math.cal(len(exchanged), plain_text, exchanged)
    client.sendall(str(encrypted_text).encode())
    time.sleep(1)
    print("Sender sent encrypted message:", encrypted_text)
    time.sleep(1)
    print("\nThis Frist Version Or The Demo Verison of it May be in future I will Make Him More Bigger and More Useful \n And You can Do That . \n That Code For You , Also You can Modify in it As You Like And Create Your version \n And in End Goodbye") 
    print("\nYou have now been successfully hacked 😊")
    client.close()


# ---------------- RECEIVER ---------------- #
def receiver(ip="127.0.0.1", port=5000):

    """
    Function: receiver
    ------------------
    Waits for a connection, validates the key length choice,
    performs key exchange, and decrypts the received message.

    Parameters:
        ip   (str): IP address to listen on (default: "127.0.0.1")
        port (int): Port to listen on (default: 5000)

    Flow:
        1. Creates a socket and listens for connections.
        2. Receives key length choice and validates it.
        3. Exchange keys with the Reciver To decript The Message.
        4. If valid, performs key exchange and decrypts message.
        5. Closes connection and stops listening.

    Returns:
        None
    """

    draw()
    print("Hello To My Small Script ASENFA ...\n")
    print("Hello To My Small Script ASENFA I Create To This will reinforce important concepts \n such as encryption and decryption and how it all works.\n I hope you have a pleasant experience\n")
    time.sleep(1)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # allow quick restart during development
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip, port))
    server.listen(1)
    print(f"Receiver listening on {ip}:{port}")

    try:
        conn, addr = server.accept()
    except Exception as e:
        print("Accept failed:", e)
        server.close()
        return

    print(f"Connected by {addr}")
    exchanged = []

    # Receive length-of-key choice first
    try:
        data = conn.recv(3072)
    except Exception as e:
        print("Receive failed:", e)
        conn.close()
        server.close()
        return

    if not data:
        print("No data received. Closing.")
        conn.close()
        server.close()
        return

    len_keys = data.decode().strip()
    if len_keys in ("1", "2"):
        print("Received valid length of keys:", len_keys)
        # Acknowledge to sender that it's OK to continue
        conn.sendall("OK".encode())
    else:
        print("Unsucessful Process For Length Of Key:", repr(len_keys))
        # Inform sender and close connection & stop listening
        try:
            conn.sendall("INVALID".encode())
        except Exception:
            pass
        conn.close()
        server.close()
        print("Receiver closed connection and stopped listening due to invalid length.")
        return

    # ---- Key Exchange ----
    try:
        data = conn.recv(3072)
        result, number_of_keys, number_drop_key = decript_key(data.decode())
    except Exception as e:
        print("Error during key exchange:", e)
        conn.close()
        server.close()
        return

    exchanged.append(result)
    time.sleep(1)
    print("Receiver got key #1:", result)

    key_one, key1, _, _ = encriptkey_main(int(len_keys))
    conn.sendall(key_one.encode())  # send 2nd
    exchanged.append(key1)
    time.sleep(1)
    print("Receiver sent key #2")

    data = conn.recv(3072)
    result2, _, _ = decript_key(data.decode())
    exchanged.append(result2)
    time.sleep(1)
    print("Receiver got key #3:", result2)

    if number_of_keys == 4:
        key_two, key2, _, _ = encriptkey_main(int(len_keys))
        conn.sendall(key_two.encode())  # send 4th
        exchanged.append(key2)
        time.sleep(1)
        print("Receiver sent key #4")

    # ---- Cleanup keys ----
    time.sleep(1)
    print("\nReceiver exchanged keys:", exchanged)
    print(f"drop Key {number_drop_key}")
    exchanged[number_drop_key] = 0
    exchanged.remove(0)
    print("Final keys:", exchanged)

    # ---- Receive encrypted message ----
    data = conn.recv(1000000).decode()
    encrypted_int = data
    decrypted_text = dicit_math.revrese_cal(len(exchanged), encrypted_int, exchanged)
    time.sleep(1)
    print("Receiver decrypted message:", decrypted_text)
    time.sleep(1) 
    print("\nThis Frist Version Or The Demo Verison of it May be in future I will Make Him More Bigger and More Useful \n And You can Do That . \n That Code For You , Also You can Modify in it As You Like And Create Your version \n And in End Goodbye") 
    print("\nYou have now been successfully hacked 😊")
    conn.close()
    server.close()

