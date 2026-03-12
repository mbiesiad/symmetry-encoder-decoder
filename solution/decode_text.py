import re

LETTER_MAP = {
    "A":"V1","B":"H1","C":"H2","D":"H3","E":"H4","F":"X1","G":"X2","H":"B1",
    "I":"B2","J":"X3","K":"H5","L":"X4","M":"V2","N":"X5","O":"B3","P":"X6",
    "Q":"X7","R":"X8","S":"X9","T":"V3","U":"V4","V":"V5","W":"V6","X":"B4",
    "Y":"V7","Z":"X10"
}

DIGIT_MAP = {
    "0":"b5","1":"b6","2":"x11","3":"h6","4":"x12",
    "5":"x13","6":"x14","7":"x15","8":"b7","9":"x16"
}

# reverse maps
REV_LETTER = {v.lower():k for k,v in LETTER_MAP.items()}
REV_DIGIT = {v.lower():k for k,v in DIGIT_MAP.items()}

TOKEN_REGEX = re.compile(r'[vhbxVHXB]\d+')

def decode_text(text: str) -> str:

    result = []
    i = 0

    while i < len(text):

        match = TOKEN_REGEX.match(text, i)

        if match:
            token = match.group()
            lower = token.lower()

            if lower in REV_LETTER:
                letter = REV_LETTER[lower]
                if token[0].islower():
                    letter = letter.lower()
                result.append(letter)

            elif lower in REV_DIGIT:
                result.append(REV_DIGIT[lower])

            else:
                result.append("?")

            i += len(token)

        else:
            result.append(text[i])
            i += 1

    return "".join(result)


if __name__ == "__main__":
    encoded = "x6x4v1h2h4b1b3x4h3h4x8"
    decoded = decode_text(encoded)

    print("Encoded :", encoded)
    print("Decoded :", decoded)
