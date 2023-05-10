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


class MorseCode(object):

    @staticmethod
    def Encode(morse_input: str) -> str:
        morse_code = {
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '0': '-----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '.': '.-.-.-',
            ',': '--..--',
            '?': '..--..',
            "'": '.----.',
            '!': '-.-.--',
            '/': '-..-.',
            '(': '-.--.',
            ')': '-.--.-',
            '&': '.-...',
            ':': '---...',
            ';': '-.-.-.',
            '=': '-...-',
            '+': '.-.-.',
            '-': '-....-',
            '_': '..--.-',
            '"': '.-..-.',
            '$': '...-..-',
            '@': '.--.-.',
            ' ': '/'
        }

        encoded_string = []
        for char in morse_input:
            if char.upper() in morse_code:
                encoded_string.append(morse_code[char.upper()])
        encoded_morse = ' '.join(encoded_string)

        return encoded_morse

    @staticmethod
    def Decode(morse_input: str) -> str:
        morse_code = {
            '.-': 'A',
            '-...': 'B',
            '-.-.': 'C',
            '-..': 'D',
            '.': 'E',
            '..-.': 'F',
            '--.': 'G',
            '....': 'H',
            '..': 'I',
            '.---': 'J',
            '-.-': 'K',
            '.-..': 'L',
            '--': 'M',
            '-.': 'N',
            '---': 'O',
            '.--.': 'P',
            '--.-': 'Q',
            '.-.': 'R',
            '...': 'S',
            '-': 'T',
            '..-': 'U',
            '...-': 'V',
            '.--': 'W',
            '-..-': 'X',
            '-.--': 'Y',
            '--..': 'Z',
            '-----': '0',
            '.----': '1',
            '..---': '2',
            '...--': '3',
            '....-': '4',
            '.....': '5',
            '-....': '6',
            '--...': '7',
            '---..': '8',
            '----.': '9',
            '.-.-.-': '.',
            '--..--': ',',
            '..--..': '?',
            '.----.': "'",
            '-.-.--': '!',
            '-..-.': '/',
            '-.--.': '(',
            '-.--.-': ')',
            '.-...': '&',
            '---...': ':',
            '-.-.-.': ';',
            '-...-': '=',
            '.-.-.': '+',
            '-....-': '-',
            '..--.-': '_',
            '.-..-.': '"'
        }

        decoded_string = []
        morse_words = morse_input.split('/')
        for word in morse_words:
            morse_chars = word.split()
            decoded_word = ''
            for char in morse_chars:
                if char in morse_code:
                    decoded_word += morse_code[char]
            decoded_string.append(decoded_word)

        decoded_text = ' '.join(decoded_string)

        return decoded_text
