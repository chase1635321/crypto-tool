import os

class RSA:
    def __init__(self):
        pass
    def public_info(self):
        print("Printing RSA public key info")
        os.system("openssl rsa -noout -text -inform PEM -in temp.txt -pubin")

    def uncipher(self):
        print("Unciphering using RsaCtfTool...")
        if len(self.command) < 3:
            print("Usage: ru <public key> <encrypted>")
        else:
            os.system("./RsaCtfTool/RsaCtfTool.py --publickey " + self.command[1] + " --uncipherfile " + self.command[2] + " --verbose")
