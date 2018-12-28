import pymysql as MySQLdb
import datetime
import rsa
import os
import hmac
import json
import hashlib

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5
import base64

def SignVerify(ds):
    data = json.loads(ds)
 #   print(data["ds_pi"])
    ds_pi = data["ds_pi"].split("===")
    pay_inf = ds_pi[0]  # 支付信息
    order_dig = ds_pi[1]  # 订单哈希
    sign_inf = ds_pi[2]  # 签名
    cli_cert = data["cli_cert"]  # 证书
    public_key = json.loads(cli_cert)["PublicKey"].replace(" ", "+")  # 用户公钥
    pay_dig = HashMd5(pay_inf)
    pubKey = RSA.importKey(base64.b64decode(public_key))
    h = MD5.new((order_dig + pay_dig).encode())  # Hash(订单hash||支付hash)
    verifier = PKCS1_v1_5.new(pubKey)

    return verifier.verify(h, base64.b64decode(sign_inf))

def sqlconnect():
    db = MySQLdb.connect('localhost', 'root', '123', 'bankdb', charset='utf8')
  #  cursor = db.cursor()
    return db

def DecodeDecrypt(ciphertext):
    file_path = os.path.abspath(__file__)
    file_path = "\\".join(file_path.split("\\")[:-1])

    private_path = open(file_path+"\\private_key.pem", 'r').read()
    private_key = RSA.importKey(private_path)

    text_decode = base64.b64decode(ciphertext)

    cipher_rsa_decrypt = PKCS1_OAEP.new(private_key)
    return cipher_rsa_decrypt.decrypt(text_decode)

def Digest(key, msg):
    h = hmac.new(str(key).encode(), str(msg).encode(), digestmod='MD5')
    return h.hexdigest()

def HashMd5(msg):
    hash = hashlib.md5()
    hash.update(msg.encode())
    return hash.hexdigest()
def SignVerify(ds):
    return True

def GetPayInf(ds):
    data = json.loads(ds)
  #  print(data["ds_pi"])
    ds_pi = data["ds_pi"].split("===")
    pay_inf = ds_pi[0]  # 支付信息
    return pay_inf

