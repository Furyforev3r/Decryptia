import src.decryptia as decryptia


def App():
    while True:
        print("Welcome do Decryptia!")

        encryption = input("""
- Choose the encryption:
    1. Base64

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

        close_input = input("Close program? (Y/N)\n- ")

        if close_input.lower() == "y":
            quit()
        else:
            pass


if __name__ == '__main__':
    App()
