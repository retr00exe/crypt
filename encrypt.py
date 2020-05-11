class encrypt:
    def setValue(self,inputComboBox,textboxValue):
        self.inputComboBox = inputComboBox
        self.textboxValue = textboxValue

    def getValue(self):
        import base64, hashlib, codecs

        if(self.inputComboBox=="Base64"):
            textUTF8 = self.textboxValue.encode("utf-8")
            base64_bytes = base64.b64encode(textUTF8)
            base64 = base64_bytes.decode("utf-8")
            return base64

        if(self.inputComboBox=="Base32"):
            textUTF8 = self.textboxValue.encode("utf-8")
            base32_bytes = base64.b32encode(textUTF8)
            base32 = base32_bytes.decode("utf-8")
            return base32

        if(self.inputComboBox=="Base16"):
            textUTF8 = self.textboxValue.encode("utf-8")
            base16_bytes = base64.b16encode(textUTF8)
            base16 = base16_bytes.decode("utf-8")
            return base16

        if(self.inputComboBox=="Ascii85"):
            textUTF8 = self.textboxValue.encode("utf-8")
            Ascii85_bytes = base64.b85encode(textUTF8)
            Ascii85 = Ascii85_bytes.decode("utf-8")
            return Ascii85

        if(self.inputComboBox=="ASCII"):
            asciiText = ' '.join(str(ord(c))for c in self.textboxValue)
            return asciiText

        if(self.inputComboBox=="Reverse"):
            reverse = self.textboxValue[::-1]
            return reverse

        if(self.inputComboBox=="ROT13"):
            rot13 = codecs.encode(self.textboxValue, 'rot_13')
            return rot13

        if(self.inputComboBox=="MD5"):
            textUTF8 = self.textboxValue.encode("utf-8")
            hash = hashlib.md5(textUTF8)
            md5 = hash.hexdigest()
            return md5

        if(self.inputComboBox=="SHA-1"):
            textUTF8 = self.textboxValue.encode("utf-8")
            hash = hashlib.sha1(textUTF8)
            sha1 = hash.hexdigest()
            return sha1

        if(self.inputComboBox=="SHA-224"):
            textUTF8 = self.textboxValue.encode("utf-8")
            hash = hashlib.sha224(textUTF8)
            sha224 = hash.hexdigest()
            return sha224

        if(self.inputComboBox=="SHA-256"):
            textUTF8 = self.textboxValue.encode("utf-8")
            hash = hashlib.sha256(textUTF8)
            sha256 = hash.hexdigest()
            return sha256

        if(self.inputComboBox=="SHA-384"):
            textUTF8 = self.textboxValue.encode("utf-8")
            hash = hashlib.sha384(textUTF8)
            sha384 = hash.hexdigest()
            return sha384

        if(self.inputComboBox=="SHA-512"):
            textUTF8 = self.textboxValue.encode("utf-8")
            hash = hashlib.sha512(textUTF8)
            sha512 = hash.hexdigest()
            return sha512