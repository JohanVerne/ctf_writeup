# usb_hid_decoder.py

HID_KEYCODES = {
    0x04: "a",
    0x05: "b",
    0x06: "c",
    0x07: "d",
    0x08: "e",
    0x09: "f",
    0x0A: "g",
    0x0B: "h",
    0x0C: "i",
    0x0D: "j",
    0x0E: "k",
    0x0F: "l",
    0x10: "m",
    0x11: "n",
    0x12: "o",
    0x13: "p",
    0x14: "q",
    0x15: "r",
    0x16: "s",
    0x17: "t",
    0x18: "u",
    0x19: "v",
    0x1A: "w",
    0x1B: "x",
    0x1C: "y",
    0x1D: "z",
    0x1E: "1",
    0x1F: "2",
    0x20: "3",
    0x21: "4",
    0x22: "5",
    0x23: "6",
    0x24: "7",
    0x25: "8",
    0x26: "9",
    0x27: "0",
    0x28: "\n",
    0x2C: " ",
    0x2D: "-",
    0x2E: "=",
    0x2F: "[",
    0x30: "]",
    0x31: "\\",
    0x33: ";",
    0x34: "'",
    0x35: "`",
    0x36: ",",
    0x37: ".",
    0x38: "/",
}

SHIFTED_CHARS = {
    "1": "!",
    "2": "@",
    "3": "#",
    "4": "$",
    "5": "%",
    "6": "^",
    "7": "&",
    "8": "*",
    "9": "(",
    "0": ")",
    "-": "_",
    "=": "+",
    "[": "{",
    "]": "}",
    "\\": "|",
    ";": ":",
    "'": '"',
    "`": "~",
    ",": "<",
    ".": ">",
    "/": "?",
}


def decode_hid_report(line):
    line = line.strip()
    if len(line) < 16:
        return ""
    bytes_list = [int(line[i : i + 2], 16) for i in range(0, 16, 2)]

    modifier = bytes_list[0]
    keycodes = bytes_list[2:]

    shift = modifier & 0x22  # Left or Right Shift

    keys = []
    for keycode in keycodes:
        if keycode == 0 or keycode == 1 or keycode == 255:
            continue
        char = HID_KEYCODES.get(keycode)
        if char:
            if shift and char in SHIFTED_CHARS:
                keys.append(SHIFTED_CHARS[char])
            elif shift:
                keys.append(char.upper())
            else:
                keys.append(char)
    return "".join(keys)


# ---- MAIN ----
decoded = []
previous_keys = set()

with open("usb_data.txt") as f:
    for line in f:
        line = line.strip()
        if len(line) < 16:
            continue

        result = decode_hid_report(line)
        if result:
            decoded.append(result)

# Print the decoded keystrokes
output = "".join(decoded)
print(output)
