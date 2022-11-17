# Python program to demonstrate
# Substitution Cipher


import string

def encryptFunction():
 all_letters= string.ascii_letters
 dict1 = {}
 plain_txt= input('Write A Message To Encrypt: ')
 key = input('Enter A Key in Decimal Value For Substitution Cipher To Encrypt Message: ')
 key = int(key)
 for i in range(len(all_letters)):
	 dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]
 cipher_txt=[]
 for char in plain_txt:
	 if char in all_letters:
		 temp = dict1[char]
		 cipher_txt.append(temp)
	 else:
		 temp =char
		 cipher_txt.append(temp)
 cipher_txt= "".join(cipher_txt)
 print("Cipher Text is: ",cipher_txt)	
 dict2 = {}	
 for i in range(len(all_letters)):
	 dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]

#  encryptFunction.bye = cipher_txt
#  return  key
 return cipher_txt



def decryptFunction(cipher_txt_sc):
 decrypt_txt = []
 key = input('Enter Key For Substitution Cipher in Decimal Value To Decrypt Message: ')
 key = int(key)
 all_letters = []
 all_letters=  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
 dict2 = {}	
 for i in range(len(all_letters)):
	 dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
 for char in cipher_txt_sc:
    if char in all_letters:
        temp = dict2[char]
        decrypt_txt.append(temp)
    else:
        temp = char
        decrypt_txt.append(temp)
 decrypt_txt = "".join(decrypt_txt)
 print("Recovered plain text :", decrypt_txt)
 
#  Main -->

# key = 0
# key = int(key)
# key= encryptFunction()
# print(key)
# print(encryptFunction.bye)
# cipher_txt=encryptFunction.bye
# print("key is ")
# print(key)
# print("cipher_txt is ") 
# print(cipher_txt)
# decryptFunction(cipher_txt , key)

cipher_txt_sc = []
cipher_txt_sc = encryptFunction()
print(cipher_txt_sc)
decryptFunction(cipher_txt_sc)