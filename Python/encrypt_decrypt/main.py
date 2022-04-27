from Crypto.Cipher import AES
from PIL import Image
import pwinput
import io

while(True):
  print('1.Encrypt\t2.Decrypt\T3.Exit')
  ch = int(input())

  if ch == 1:
    # for encryption
    print("Enter the filename")
    fname = input()
    file = open(fname,'rb');
    data = file.read()
    print("Enter the key")
    keystring = pwinput.pwinput()

    # to convert string into bytes
    key = keystring.encode('utf-8')    
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    # to save encrypted text in a file
    file_out = open("encrypted.txt", "wb")
    file_out.truncate(0)
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    file_out.close()
    file.close()

  elif ch==2:
    # for decryption
    print("Enter the filename")
    fname = input()
    file = open(fname, "rb")
    nonce, tag, ciphertext = [ file.read(x) for x in (16, 16, -1) ]
    file.close()  
    print("Enter the key")
    keystr = pwinput.pwinput()

    # to convert string into bytes
    key=keystr.encode('utf-8')
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
  
    try:      
      # to obtain decoded text data
      decodedata=data.decode('utf-8')
      file_out=open("decrypted.txt",'w');
      file_out.truncate(0)
      file_out.write(decodedata)
      file_out.close()
      
    except:      
      # to obtain decoded image
      img = Image.open(io.BytesIO(data))
      img.save('img.jpg')
  else:
    break
