import base64, hashlib, codecs

class solver:
    def __init__(self,inputComboBox,textboxValue):
        self.inputComboBox = inputComboBox
        self.textboxValue = textboxValue

    def encrypt(self,inputComboBox,textboxValue):
        import base64, hashlib, codecs
        if(inputComboBox=="Base64"):
            textUTF8 = textboxValue.encode("utf-8")
            base64_bytes = base64.b64encode(textUTF8)
            base64 = base64_bytes.decode("utf-8")
            return base64