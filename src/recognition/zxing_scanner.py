from zxing import BarCodeReader

def decode(frame):
    decoded_objects = []
    try:
        bar_code_reader = BarCodeReader()
        decoded_objects = bar_code_reader.decode(frame)
    except Exception as e:
        print(f"Error decoding using zxing: {e}")

    return decoded_objects
