#THIS IS AN ENCRYPTION DECRYPTION PROGRAM
#ONLY USE LETTERS, NUMBERS AND THE ALLOWED CHARACTERS
# ALLOWED CHARACTERS [!,@, #, $, %, ^, &, *, -, _, +, =, [, ], {, ], ;, :, <, >, /, ?]
# THIS PROGRAM DO NOT SUPPORT ANY OF THESE CHARACTERS [ ' , " , \, |, (, ) ] 
# TRY TO AVOID THIS CHARACTERS AND OTHER SPECIAL CHARACTERS  
 

                                   #ENCRYPTION
 
# replace(n) replaces a character with a encrypted character
def replace(n): 
 basic_message =   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', '(',
                    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ')',
                    'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 
                    'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', 
                    '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^',
                    '&', '*', '-', '_', '+', '=', '[', ']', '{', '}',
                    ';', ':', '"', ',', '<', '.', '>', '/', '?', '`', '~']  
 
 if n in basic_message: 
   encrypt_message = ['&', '*', 'T', 'U', 'V', 'W', 'I', 'J', 'K', 'L', '(', ')',
                      'x', 'y', 'z', 'A', 'm', 'n', '2', '3', '4', 'o', 'p', 'a', 
                      'b', 'c', 'd', '5', '6', '7', '8', 'B', 'C', 'D', 'E', 'e', 
                      'f', 'g', 'h', 'q', 'r', 's', 't', 'N', 'M', 'O', 'P', 'X', 
                      'Y', 'Z', '1', '9', '!', '@', '#', '-', '_', '+', '=', 'i', 
                      'j', 'k', 'l', 'u', 'v', 'w', 'Q', 'R', 'S', 'F', 'G', 'H', 
                      '$', '%', '^', ';', ':', '"', ',', '/', '?', '`', '~', '<',
                      '.', '>', ']', '{', '}', '[', '0'] 
   position_n = basic_message.index(n)  
  
   return encrypt_message[position_n]

 else: return ' '
                        
                        
# encrypt(str1) consumes a string/sentence and encrypts it   
 
def encrypt(str1):
 
 return ''.join(encryption(list(str1))) 


#encryption(lst) consumes a list of characters and produces a list of encrypted
# characters

def encryption(lst):
 
 if lst ==[]: return []   

 else:
  first = lst[0]
  rest = lst[1:]

  return [replace(first)] + encryption(rest)  
 
 
                        
                          #DECRYPTION

#decrypt(str1) decrypts the consumed encrypted string

def decrypt(str1):
 return ''.join(decryption(list(str1)))


#decryption(lst) produces a list of decrypted characters

def decryption(lst):
 
 if lst==[]: return []
 
 else:
  first = lst[0]
  rest = lst[1:]

  return [decrypted(first)] + decryption(rest)
 
 
#decrypted(e) decrypts a consumed encrypted character

def decrypted(e):
 
 encrypted_message = ['&', '*', 'T', 'U', 'V', 'W', 'I', 'J', 'K', 'L', '(', ')',
                      'x', 'y', 'z', 'A', 'm', 'n', '2', '3', '4', 'o', 'p', 'a', 
                      'b', 'c', 'd', '5', '6', '7', '8', 'B', 'C', 'D', 'E', 'e', 
                      'f', 'g', 'h', 'q', 'r', 's', 't', 'N', 'M', 'O', 'P', 'X', 
                      'Y', 'Z', '1', '9', '!', '@', '#', '-', '_', '+', '=', 'i', 
                      'j', 'k', 'l', 'u', 'v', 'w', 'Q', 'R', 'S', 'F', 'G', 'H', 
                      '$', '%', '^', ';', ':', '"', ',', '/', '?', '`', '~', '<',
                      '.', '>', ']', '{', '}', '[', '0']  
 
 if e in encrypted_message:                     
   decrypt_message=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', '(',
                    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ')',
                    'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 
                    'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', 
                    '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^',
                    '&', '*', '-', '_', '+', '=', '[', ']', '{', '}',
                    ';', ':', '"', ',', '<', '.', '>', '/', '?', '`', '~']  
   position_e = encrypted_message.index(e) 
   
   return decrypt_message[position_e]
 
 else: return ' '
 
print encrypt("my password is = rutpatel")
print decrypt("xc A&22pznU K2 ; n43A&3V)") 

print encrypt(" my name is rutpatel rd4patel")
print decrypt(" xc y&xV K2 n43A&3V) nU=A&3V)")