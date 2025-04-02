import qrcode
from PIL import Image
import cv2
import numpy as np
from pyzbar.pyzbar import decode


def generate_qr():

    data = input("Enter data for QR Code: ")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save("qr_code.png")
    img.show()

    print(f"QR Code generated and saved as qr_code.png")


def decode_qr():

    file_path = input(
        "Enter the path of the QR code image to decode (e.g., qr_code.png): ")

    img = cv2.imread(file_path)

    decoded_objects = decode(img)

    if not decoded_objects:
        print("No QR code found in the image.")
        return

    for obj in decoded_objects:
        qr_data = obj.data.decode('utf-8')
        print(f"Decoded Data: {qr_data}")

        points = obj.polygon
        if len(points) == 4:
            pts = np.array(points, dtype=np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], isClosed=True,
                          color=(0, 255, 0), thickness=2)

        cv2.imshow("QR Code", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


print("Choose an option: ")
print("1. Generate QR Code")
print("2. Decode QR Code")

choice = input("Enter choice (1/2): ")

if choice == "1":
    generate_qr()
elif choice == "2":
    decode_qr()
else:
    print("❌ Invalid Choice! Run again.")
