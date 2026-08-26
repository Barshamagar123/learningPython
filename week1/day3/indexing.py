name="python programming"
print(f"first: {name[0]}")
print(f"last:{name[-1]}")

def get_first_char(text):
    if text:
        return text[0]
    return ""
def get_last_char(text):
    if text:
        return text[-1]
    return ""
def get_char_at(text,position):
    if 0<=position < len(text):
        return text[position]
    return "invalid"
text="hello world"
print(f"the first char is {get_first_char(text)}")
print(f"the last char is {get_last_char(text)}")
print(f"the char at any position {get_char_at(text,4)}")