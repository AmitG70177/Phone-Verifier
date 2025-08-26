# phone_verifier.py

import requests
from setting import API_KEY, BASE_URL

def verify_phone_number(phone_number):
    params = {
        'access_key': API_KEY,
        'number': phone_number
    }

    print(f"📞 Verifying phone number: {phone_number} ...")

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("valid"):
            print("✅ Phone number is valid!")
            print(f"📍 Country: {data.get('country_name')}")
            print(f"🌍 Location: {data.get('location')}")
            print(f"📞 Line type: {data.get('line_type')}")
            print(f"📡 Carrier: {data.get('carrier')}")
        else:
            print("❌ Invalid phone number.")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error: {e}")


if __name__ == "__main__":
    phone = input("Enter phone number with country code (e.g. +14158586273): ")
    verify_phone_number(phone)
