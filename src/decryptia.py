import base64


class Base64(object):
    @staticmethod
    def Encode(base_input: str) -> str:
        base_encode = base_input.encode("ascii")

        base64_bytes = base64.b64encode(base_encode)
        base64_string = base64_bytes.decode("ascii")

        return base64_string

    @staticmethod
    def Decode(base_input: str) -> str:
        base64_bytes = base_input.encode("ascii")
        decoded_string_bytes = base64.b64decode(base64_bytes)
        decoded_string = decoded_string_bytes.decode("ascii")

        return decoded_string
