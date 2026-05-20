import qrcode 

data = input("Enter Text or URL for QR Code: ")
filename = input("Please Enter the Name of your File: ")

qr = qrcode.make(data)

qr.save(filename + ".png")

print("QR Code generated successfully!")
print("Thank You for using My_QR Code.apk")

