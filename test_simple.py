import requests
import base64

def test_api():
    """
    Fungsi sederhana untuk testing API
    Melakukan:
    1. Test endpoint root
    2. Test encode dengan gambar upi.jpg
    3. Test decode dari hasil encode
    """
    # URL API
    base_url = "http://localhost:5000"
    
    # 1. Test endpoint root
    response = requests.get(base_url)
    print("Root endpoint:", response.json())
    
    # 2. Test encode
    # Baca gambar
    with open("original.png", "rb") as img:
        b64_image = base64.b64encode(img.read()).decode("utf-8")

    response = requests.post("http://localhost:5000/encode", json={
        "image": b64_image,
        "message": "Secret message",
        "key": "encryptionkey" 
    })

    encoded_image = response.json()["encoded_image"]
    
    # Kirim request encode
    print("\nMencoba encode...")
    response = requests.post(f"{base_url}/encode", json=encode_data)
    
    if response.status_code == 200:
        result = response.json()
        print("Encode berhasil!")
        
        # Simpan gambar hasil
        img_data = base64.b64decode(result['encoded_image'])
        with open("hasil_encode.png", "wb") as f:
            f.write(img_data)
        print("Gambar tersimpan sebagai hasil_encode.png")
        
        # 3. Test decode
        response = requests.post("http://localhost:5000/decode", json={
            "image": encoded_image,
            "key": "encryptionkey"
        })

        message = response.json()["message"]
        print(message)
        print("\nMencoba decode...")
        response = requests.post(f"{base_url}/decode", json=decode_data)
        
        if response.status_code == 200:
            result = response.json()
            print("Decode berhasil!")
            print("Pesan:", result['message'])
        else:
            print("Error decode:", response.json().get('error'))
    else:
        print("Error encode:", response.json().get('error'))

if __name__ == "__main__":
    test_api() 