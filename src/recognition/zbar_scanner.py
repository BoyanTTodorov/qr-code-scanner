import pyzbar.pyzbar as pyzbar

def decode(frame):
    try:
        decoded_objects = pyzbar.decode(frame)
    except pyzbar.pyzbar.ZBarSymbolTypePDF417 as e:
        print(f"Warning: PDF417 decoding issue: {e}")
        decoded_objects = []

    return decoded_objects
