import re

# mapping uppercase letters
LETTER_MAP = {
    "A":"V1","B":"H1","C":"H2","D":"H3","E":"H4","F":"X1","G":"X2","H":"B1",
    "I":"B2","J":"X3","K":"H5","L":"X4","M":"V2","N":"X5","O":"B3","P":"X6",
    "Q":"X7","R":"X8","S":"X9","T":"V3","U":"V4","V":"V5","W":"V6","X":"B4",
    "Y":"V7","Z":"X10"
}

# digits
DIGIT_MAP = {
    "0":"b5","1":"b6","2":"x11","3":"h6","4":"x12",
    "5":"x13","6":"x14","7":"x15","8":"b7","9":"x16"
}

def encode_text(text: str) -> str:
    result = []

    for ch in text:
        if ch.isalpha():
            code = LETTER_MAP[ch.upper()]
            if ch.islower():
                code = code.lower()
            result.append(code)

        elif ch.isdigit():
            result.append(DIGIT_MAP[ch])

        else:
            result.append(ch)

    return "".join(result)


if __name__ == "__main__":
    text = "placeholder"
    encoded = encode_text(text)

    print("Original:", text)
    print("Encoded :", encoded)
