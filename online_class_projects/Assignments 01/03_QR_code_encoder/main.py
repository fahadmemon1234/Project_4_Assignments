import streamlit as st
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


st.set_page_config(page_title="QR Code Generator & Scanner", layout="centered")

st.title("🔲 QR Code Generator & Scanner")


tab1, tab2 = st.tabs(["Generate QR Code", "Scan QR Code"])

# ---------------- QR Code Generation ----------------
with tab1:
    st.subheader("📌 Enter Text to Generate QR Code")
    qr_text = st.text_input("Enter text or URL:",
                            placeholder="Type something here...")

    width = st.number_input("Enter QR Code Width:",
                            min_value=100, max_value=1000, value=300, step=50)
    height = st.number_input("Enter QR Code Height:",
                             min_value=100, max_value=1000, value=300, step=50)

    if st.button("Generate QR Code"):
        if qr_text:

            qr = qrcode.QRCode(
                version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(qr_text)
            qr.make(fit=True)

            qr_image = qr.make_image(fill="black", back_color="white")

            qr_image = qr_image.resize(
                (width, height), Image.Resampling.LANCZOS)

            qr_path = "QRCode.png"
            qr_image.save(qr_path)

            st.image(qr_path, caption="Your QR Code", use_container_width=True)

            with open(qr_path, "rb") as qr_file:
                qr_bytes = qr_file.read()
                st.download_button(
                    label="📥 Download QR Code", data=qr_bytes, file_name="QRCode.png", mime="image/png")
        else:
            st.warning("⚠️ Please enter text to generate a QR Code.")

# ---------------- QR Code Scanning ----------------
with tab2:
    st.subheader("📤 Upload an Image to Decode QR Code")
    uploaded_file = st.file_uploader(
        "Upload a QR Code image", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        try:

            img = Image.open(uploaded_file)
            st.image(img, caption="Uploaded Image",
                     use_container_width=True)

            decoded_info = decode(img)

            if decoded_info:
                for obj in decoded_info:
                    st.success(f"✅ Decoded Text: {obj.data.decode('utf-8')}")
            else:
                st.error("❌ No QR Code found in the image.")
        except Exception as e:
            st.error(f"⚠️ Error decoding QR Code: {e}")

st.markdown("---")
st.markdown("🔗 Built with ❤️ using Streamlit | © 2025 QR Code Generator")
