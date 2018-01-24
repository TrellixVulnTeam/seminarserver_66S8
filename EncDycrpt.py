from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class EncDec(object):

    def __init__(self):
        self.key = RSA.generate(2048)
        self.priv_pub_keys_dict = {}

    def create_private_public_key(self):
        bin_priv_key = self.key.exportKey('PEM')
        file_name = "p_key.pem"
        file_to_write = open(file_name, 'w')
        file_to_write.write(bin_priv_key)
        file_to_write.close()
        bin_pub_key = self.key.publickey().exportKey('PEM')
        self.priv_pub_keys_dict.update({"bin_priv_key": bin_priv_key})
        self.priv_pub_keys_dict.update({"bin_pub_key": bin_pub_key})

    def encrypt_data(self, data_to_encrypt):
        public_key = RSA.importKey(self.priv_pub_keys_dict["bin_pub_key"])
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_msg = cipher.encrypt(data_to_encrypt)
        return encrypted_msg

    def decrypt_data(self, data_to_decrypt):
        private_key = RSA.importKey(self.priv_pub_keys_dict["bin_priv_key"])
        cipher = PKCS1_OAEP.new(private_key)
        decrypted_msg = cipher.decrypt(data_to_decrypt)
        return decrypted_msg
