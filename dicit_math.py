import math
import sys
sys.set_int_max_str_digits(200000000)
Ascii = {
  ' ': 127,
  '!': 128,
  '"': 129,
  '#': 130,
  '$': 131,
  '%': 132,
  '&': 133,
  "'": 134,
  '(': 135,
  ')': 136,
  '*': 137,
  '+': 138,
  ',': 39,
  '-': 40,
  '.': 41,
  '/': 42,
  '0': 43,
  '1': 44,
  '2': 45,
  '3': 46,
  '4': 47,
  '5': 48,
  '6': 49,
  '7': 55,
  '8': 56,
  '9': 57,
  ':': 58,
  ';': 59,
  '<': 60,
  '=': 61,
  '>': 62,
  '?': 63,
  '@': 64,
  'A': 65,
  'B': 66,
  'C': 67,
  'D': 68,
  'E': 69,
  'F': 70,
  'G': 71,
  'H': 72,
  'I': 73,
  'J': 74,
  'K': 75,
  'L': 76,
  'M': 77,
  'N': 78,
  'O': 79,
  'P': 80,
  'Q': 81,
  'R': 82,
  'S': 83,
  'T': 84,
  'U': 85,
  'V': 86,
  'W': 87,
  'X': 88,
  'Y': 89,
  'Z': 90,
  '[': 91,
  '\\': 92,
  ']': 93,
  '^': 94,
  '_': 95,
  '`': 96,
  'a': 97,
  'b': 98,
  'c': 99,
  'd': 100,
  'e': 101,
  'f': 102,
  'g': 103,
  'h': 104,
  'i': 105,
  'j': 106,
  'k': 107,
  'l': 108,
  'm': 109,
  'n': 110,
  'o': 111,
  'p': 112,
  'q': 113,
  'r': 114,
  's': 115,
  't': 116,
  'u': 117,
  'v': 118,
  'w': 119,
  'x': 120,
  'y': 121,
  'z': 122,
  '{': 123,
  '|': 124,
  '}': 125,
  '~': 126 ,
  '\n' :50

}
Ascii2 = {
  ' ': 27,
  '!': 28,
  '"': 29,
  '#': 30,
  '$': 31,
  '%': 32,
  '&': 33,
  "'": 34,
  '(': 35,
  ')': 36,
  '*': 37,
  '+': 38,
  ',': 39,
  '-': 40,
  '.': 41,
  '/': 42,
  '0': 43,
  '1': 44,
  '2': 45,
  '3': 46,
  '4': 47,
  '5': 48,
  '6': 49,
  '7': 55,
  '8': 56,
  '9': 57,
  ':': 58,
  ';': 59,
  '<': 60,
  '=': 61,
  '>': 62,
  '?': 63,
  '@': 64,
  'A': 65,
  'B': 66,
  'C': 67,
  'D': 68,
  'E': 69,
  'F': 70,
  'G': 71,
  'H': 72,
  'I': 73,
  'J': 74,
  'K': 75,
  'L': 76,
  'M': 77,
  'N': 78,
  'O': 79,
  'P': 80,
  'Q': 81,
  'R': 82,
  'S': 83,
  'T': 84,
  'U': 85,
  'V': 86,
  'W': 87,
  'X': 88,
  'Y': 89,
  'Z': 90,
  '[': 91,
  '\\': 92,
  ']': 93,
  '^': 94,
  '_': 95,
  '`': 96,
  'a': 97,
  'b': 98,
  'c': 99,
  'd': 100,
  'e': 101,
  'f': 102,
  'g': 103,
  'h': 104,
  'i': 105,
  'j': 106,
  'k': 107,
  'l': 108,
  'm': 109,
  'n': 110,
  'o': 111,
  'p': 112,
  'q': 113,
  'r': 51,
  's': 52,
  't': 53,
  'u': 54,
  'v': 18,
  'w': 19,
  'x': 20,
  'y': 21,
  'z': 22,
  '{': 23,
  '|': 24,
  '}': 25,
  '~': 26 ,
  '\n' :50

}
def cal (num_of_key : int , message  , list_keys : list) :
  """
Function: cal
-------------
Performs the encryption process based on the number of keys and message type.

This function transforms the input message into a ciphered numeric form
depending on the number of keys (2 or 3) and the structure of the provided
keys. It uses bitwise operations, modular exponentiation, and ASCII mappings
to generate the encrypted output.

Parameters:
    num_of_key (int): Number of keys used for encryption (2 or 3).
    message    (str): The plaintext message to encrypt.
    list_keys  (list): A list containing the encryption keys.

Flow:
    1. Check if the keys are long (length around 308–309) to determine
       which ASCII mapping to use.
    2. Convert each character of the message into its ASCII value using
       either `Ascii` or `Ascii2`.
    3. If `num_of_key` is 2:
         - Extract numeric segments from the first and second keys.
         - Perform bitwise AND (&) between them.
         - Encrypt each ASCII value with a combination of pow(), addition,
           and concatenation.
    4. If `num_of_key` is 3:
         - Extract numeric parts from all three keys.
         - Compute a mix of AND (&) and XOR (^) to form an encryption mask.
         - Apply the encryption formula using pow() and the XORed mask.
    5. Concatenate all encrypted segments into one large integer.

Returns:
    int: A large integer representing the encrypted message.

Example:
    >>> cal(2, "HELLO", [key1, key2])
    534050231...
  """
  if len(str(list_keys[0])) == 308  or len(str(list_keys[0])) == 309 or len(str(list_keys[0])) == 307 :
    list_msg = list(message)
    for index , val in enumerate(list_msg) :
      for k , v in Ascii2.items() :
        if val == k :
          list_msg[index] = v
    if num_of_key == 2 and len(list_keys) == 2 :
      f_p = int(str(list_keys[0])[40:43] + str(list_keys[0])[90:93])    
      s_p = int(str(list_keys[1])[100 :102] + str(list_keys[1])[200 : 202] )
      an = s_p & f_p                 
      for index , val in enumerate(list_msg) :  
        cipher = pow(f_p,val) + s_p + an
        c = int(str(len(str(cipher))) + str(cipher))
        list_msg[index] = c            
      cipher = pow(f_p,val) + s_p + an
      c = int(str(len(str(cipher))) + str(cipher))
      list_msg[index] = c    
    if num_of_key == 3  and len(list_keys) == 3:
      f_p = int(str(list_keys[0])[40:45] + str(list_keys[0])[90:94])
      s_p = int(str(list_keys[1])[100 : 105] + str(list_keys[1])[210 : 212] +str(list_keys[1])[240 : 243])
      t_p = int(str(list_keys[2])[110 : 115] + str(list_keys[2])[220 : 223] +str(list_keys[2])[250 : 252])
      nu = int( str(list_keys[1])[640 : 645] +  str(list_keys[1])[120 : 123] + str(list_keys[2])[460 : 462] + str(list_keys[1])[300 : 305])   
      an = s_p & t_p           
      xo = an ^ nu       
      for index , val in enumerate(list_msg) :      
        cipher = pow(f_p,val) + xo
        c = int(str(len(str(cipher))) + str(cipher))
        list_msg[index] = c
  else :        
    list_msg = list(message)
    for index , val in enumerate(list_msg) :
      for k , v in Ascii.items() :
        if val == k :
          list_msg[index] = v
    if num_of_key == 2 and len(list_keys) == 2 :
      for index , val in enumerate(list_msg) :
        f_p = int(str(list_keys[0])[40:43] + str(list_keys[0])[90:93])
        s_p = int(str(list_keys[1])[100 :105] + str(list_keys[1])[500 : 505] )
        an = s_p & f_p       
        cipher = pow(f_p,val) + s_p + an
        c = int(str(len(str(cipher))) + str(cipher))
        list_msg[index] = c
    if num_of_key == 3  and len(list_keys) == 3:
      for index , val in enumerate(list_msg) :      
        f_p = int(str(list_keys[0])[40:45] + str(list_keys[0])[90:94])
        s_p = int(str(list_keys[1])[100 : 110] + str(list_keys[1])[510 : 515] +str(list_keys[1])[710 : 715])
        t_p = int(str(list_keys[2])[110 : 120] + str(list_keys[2])[520 : 525] +str(list_keys[2])[720 : 725])
        nu = int( str(list_keys[1])[640 : 650] +  str(list_keys[1])[120 : 130] + str(list_keys[2])[660 : 670] + str(list_keys[1])[900 : 930])           
        an = s_p & t_p           
        xo = an ^ nu 
        cipher = pow(f_p,val) + xo
        c = int(str(len(str(cipher))) + str(cipher))
        list_msg[index] = c

  big_number = int(''.join(str(n) for n in list_msg))           
  return big_number

def revrese_cal (num_of_key : int , message  , list_keys : list) :

  """
Function: revrese_cal
---------------------
Performs the decryption process to restore the original message
from the encrypted numeric form.

This function reverses the encryption logic implemented in `cal()`.
It splits the numeric ciphertext into chunks, applies logarithmic
and arithmetic operations to retrieve the original ASCII values,
and reconstructs the original string.

Parameters:
    num_of_key (int): Number of keys used for decryption (2 or 3).
    message    (int or str): The numeric ciphertext to decrypt.
    list_keys  (list): A list containing the same keys used during encryption.

Flow:
    1. Split the long numeric message into chunks based on stored length headers.
    2. Check key lengths to decide which ASCII mapping (`Ascii` or `Ascii2`) to use.
    3. If `num_of_key` is 2:
         - Extract numeric segments from both keys.
         - Reverse the encryption using subtraction and logarithmic operations.
         - Convert numeric ASCII values back to characters.
    4. If `num_of_key` is 3:
         - Extract numeric segments from all three keys.
         - Recalculate bitwise masks (AND and XOR).
         - Apply logarithmic reversal to retrieve ASCII codes.
         - Map them back to characters.
    5. Join all characters to form the final decrypted message.

Returns:
    str: The original plaintext message after decryption.

Example:
    >>> revrese_cal(2, 534050231..., [key1, key2])
    'HELLO'
  """

  message = str(message)
  list_msg = []
  while len(message) >= 3:
      collect = int(message[:3])
      chunk = message[3:collect]
      list_msg.append(chunk)
      h = collect+3
      message = message[h:]     

  if len(str(list_keys[0])) == 308  or len(str(list_keys[0])) == 309 or len(str(list_keys[0])) == 307 :
    if num_of_key == 2 and len(list_keys) == 2 :
      f_p = int(str(list_keys[0])[40:43] + str(list_keys[0])[90:93])    
      s_p = int(str(list_keys[1])[100 :102] + str(list_keys[1])[200 : 202] )
      an = s_p & f_p  
      for ind , val in enumerate(list_msg) :  
        f1 = int(val) - int(s_p)-int(an)
        f2  = math.log(f1 ,f_p)
        list_msg[ind] = math.ceil(f2)  
      for index , val in enumerate(list_msg) :
        for k , v in Ascii2.items() :
          if val == v :
            list_msg[index] = str(k)   

    if num_of_key == 3 and len(list_keys) == 3  :
      f_p = int(str(list_keys[0])[40:45] + str(list_keys[0])[90:94])
      s_p = int(str(list_keys[1])[100 : 105] + str(list_keys[1])[210 : 212] +str(list_keys[1])[240 : 243])
      t_p = int(str(list_keys[2])[110 : 115] + str(list_keys[2])[220 : 223] +str(list_keys[2])[250 : 252])
      nu = int( str(list_keys[1])[640 : 645] +  str(list_keys[1])[120 : 123] + str(list_keys[2])[460 : 462] + str(list_keys[1])[300 : 305])   
      an = s_p & t_p           
      xo = an ^ nu       
      for ind , val in enumerate(list_msg) : 
        f1 = int(val) - int(xo)
        f2  = math.log(f1 ,f_p)
        list_msg[ind] = round(f2)
      for index , val in enumerate(list_msg) :
        for k , v in Ascii2.items() :
          if val == v :
            list_msg[index] = str(k) 
      for index , val in enumerate(list_msg) :
        for k , v in Ascii2.items() :
          if val == v :
            list_msg[index] = str(k)             
            
  else :
    if num_of_key == 2 and len(list_keys) == 2 :
      f_p = int(str(list_keys[0])[40:43] + str(list_keys[0])[90:93])
      s_p = int(str(list_keys[1])[100 :105] + str(list_keys[1])[500 : 505] )
      an = s_p & f_p  
      for ind , val in enumerate(list_msg) :  
        f1 = int(val) - int(s_p)-int(an)
        f2  = math.log(f1 ,f_p)
        list_msg[ind] = round(f2)+1
        for index , val in enumerate(list_msg) :
          for k , v in Ascii.items() :
            if val == v :
              list_msg[index] = str(k)         
    if num_of_key == 3 and len(list_keys) == 3  :
      f_p = int(str(list_keys[0])[40:45] + str(list_keys[0])[90:94])
      s_p = int(str(list_keys[1])[100 : 110] + str(list_keys[1])[510 : 515] +str(list_keys[1])[710 : 715])
      t_p = int(str(list_keys[2])[110 : 120] + str(list_keys[2])[520 : 525] +str(list_keys[2])[720 : 725])
      nu = int( str(list_keys[1])[640 : 650] +  str(list_keys[1])[120 : 130] + str(list_keys[2])[660 : 670] + str(list_keys[1])[900 : 930])          
      an = s_p & t_p           
      xo = an ^ nu       
      for ind , val in enumerate(list_msg) : 
        f1 = int(val) - int(xo)
        f2  = math.log(f1 ,f_p)
        list_msg[ind] = round(f2)
        for index , val in enumerate(list_msg) :
          for k , v in Ascii.items() :
            if val == v :
              list_msg[index] = str(k) 
            
  word = ''.join(list_msg)     
  return word 
 
     
  

  