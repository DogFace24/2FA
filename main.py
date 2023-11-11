#install totp module and qrcode module
import pyotp
import qrcode


#you have to set a long secret key:
secretKey = "AadityaSahooIsTheSmartestManInTheWorldButHisAccountWouldStillBeHackedIfHeUsesThisAsHisSecretKey"
'''
uri = pyotp.totp.TOTP(secretKey).provisioning_uri(name = "Secret key for authentication",
                                                  issuer_name = "Aaditya Sahoo's Authentication Key")
#uri means universal resource identifier
#it is used to distinguish one logical aspect from another

print(uri)

qrcode.make(uri).save("AuthenticationCode.png")
#now you can scan this on your google authenticator... make sure that you dont use illegal characters in the secretKey - like , and - and other things

#now that i have generated this qrcode i dont need the entire code. i just need a checker if the value from google is true or false.
'''

totp = pyotp.TOTP(secretKey)

print(totp.verify(input("Enter Authentication Key: ")))


