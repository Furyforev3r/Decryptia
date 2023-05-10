import src.decryptia as decryptia


def App():
    while True:
        print("Welcome do Decryptia!")

        encryption = input("""
- Choose the encryption:
    1. Base64
    2. Morse Code
    3. Binary Code
    4. Vinegere Cipher
- """)

        match int(encryption):
            case 1:
                decode_or_encode = input("Decode or Encode? ")

                match decode_or_encode.lower():
                    case "decode":
                        base_input = input("String to decode...\n- ")
                        base_result = decryptia.Base64().Decode(base_input)
                        print(f"Decoded string: {base_result}")
                    case "encode":
                        base_input = input("String to encode...\n- ")
                        base_result = decryptia.Base64().Encode(base_input)
                        print(f"Encoded string: {base_result}")
            case 2:
                decode_or_encode = input("Decode or Encode? ")

                match decode_or_encode.lower():
                    case "decode":
                        morse_input = input("String to decode...\n- ")
                        morse_result = decryptia.MorseCode().Decode(morse_input)
                        print(f"Decoded string: {morse_result}")
                    case "encode":
                        morse_input = input("String to encode...\n- ")
                        morse_result = decryptia.MorseCode().Encode(morse_input)
                        print(f"Encoded string: {morse_result}")
            case 3:
                decode_or_encode = input("Decode or Encode? ")

                match decode_or_encode.lower():
                    case "decode":
                        binary_input = input("String to decode...\n- ")
                        binary_result = decryptia.BinaryCode().Decode(binary_input)
                        print(f"Decoded string: {binary_result}")
                    case "encode":
                        binary_input = input("String to encode...\n- ")
                        binary_result = decryptia.BinaryCode().Encode(binary_input)
                        print(f"Encoded string: {binary_result}")
            case 4:
                decode_or_encode = input("Decode or Encode? ")
                key = input("Key...\n- ")

                match decode_or_encode.lower():
                    case "decode":
                        vigenete_input = input("String to decode...\n- ")
                        vigenete_result = decryptia.VinegereCipher().Decrypt(vigenete_input, key)
                        print(f"Decoded string: {vigenete_result}")
                    case "encode":
                        vigenete_input = input("String to encode...\n- ")
                        vigenete_result = decryptia.VinegereCipher().Encrypt(vigenete_input, key)
                        print(f"Encoded string: {vigenete_result}")

        close_input = input("Close program? (Y/N)\n- ")

        if close_input.lower() == "y":
            quit()
        else:
            pass


if __name__ == '__main__':
    App()
