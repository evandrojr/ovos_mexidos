#!/usr/bin/env python

#ovos_mexidos e|d|q [1-255] file_to_scramble

import sys
import hashlib
import os
import gc

operation = sys.argv[1].lower()
key =int(sys.argv[2])
file_name = sys.argv[3]
  
def xor_c(a):
  return bytearray([b^key for b in bytearray(a)])

def encrypt():    
  h1 = open(file_name,'r')
  h2 = open(file_name + ".crypt",'w')
  h3 = open(file_name + ".validate",'w')
  c1 = h1.read()
  md5_1 = hashlib.md5(c1).hexdigest()
  h1.close()
  h2.write(xor_c(c1))
  del c1
  gc.collect()
  h2.close()
  h2 = open(file_name + ".crypt",'r')
  c2 = h2.read()
  h2.close()
  h3.write(xor_c(c2))
  del c2
  gc.collect()
  h3.close()
  h3 = open(file_name + ".validate",'r')
  md5_3 = hashlib.md5(h3.read()).hexdigest()
  h3.close()
  if md5_1 != md5_3:
    print "Erro na criptografia"
  else:
    print "Aparentemente funcionou!"
    
    
def quick_encrypt():    
  h1 = open(file_name,'r')
  h2 = open(file_name + ".crypt",'w')
  c1 = h1.read()
  h1.close()
  h2.write(xor_c(c1))
  del c1
  gc.collect()
  h2.close()
  print "Terminada a compactacao nao tao lenta!"    
    
def decrypt():
  file_name_decrypt = file_name.replace(".crypt","")  
  h1 = open(file_name,'r')
  h2 = open(file_name_decrypt,'w')
  c1 = h1.read()
  h2.write(xor_c(c1))
  del c1
  h1.close()
  h2.close()
  print "Concluido"
  
if operation == 'e': 
  encrypt()
if operation == 'q': 
  quick_encrypt()  
if operation == 'd':
  decrypt()
  
    
 

  
