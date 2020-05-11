class decrypt:
    def setValue(self,inputComboBox,textboxValue):
        self.inputComboBox = inputComboBox
        self.textboxValue = textboxValue

    def getValue(self):
        import base64, hashlib, codecs

        if(self.inputComboBox=="Base64"):
            textUTF8 = self.textboxValue.encode("utf-8")
            base64_bytes = base64.b64decode(textUTF8)
            base64 = base64_bytes.decode("utf-8")
            return base64

        if(self.inputComboBox=="Base32"):
            textUTF8 = self.textboxValue.encode("utf-8")
            base32_bytes = base64.b32decode(textUTF8)
            base32 = base32_bytes.decode("utf-8")
            return base32

        if(self.inputComboBox=="Base16"):
            textUTF8 = self.textboxValue.encode("utf-8")
            base16_bytes = base64.b16decode(textUTF8)
            base16 = base16_bytes.decode("utf-8")
            return base16

        if(self.inputComboBox=="ASCII"):
            asciiText = ''.join(chr(i) for i in [int(i) for i in self.textboxValue.split()])
            return asciiText

        if(self.inputComboBox=="Ascii85"):
            textUTF8 = self.textboxValue.encode("utf-8")
            Ascii85_bytes = base64.b85decode(textUTF8)
            Ascii85 = Ascii85_bytes.decode("utf-8")
            return Ascii85

        if(self.inputComboBox=="Reverse"):
            reverse = self.textboxValue[::-1]
            return reverse

        if(self.inputComboBox=="ROT13"):
            rot13 = codecs.decode(self.textboxValue, 'rot_13')
            return rot13