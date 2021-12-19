
def remove_punc(text):
    punc = ['!', '(', ')', '-', '[', ']', '{', '}', ';', ':', "'", '"', '\\', ',', '<', '>', '.', '/', '?', '@', '#', '$', '%', '^', '&', '*', '_', '~', '\xa0']

    for p in punc:
        text = text.replace(p, " ")
    return text


def tokenize(text):
    text = remove_punc(text)
    text = text.split()
    return text

def get_max_key_dict(input_dict):
    return max(input_dict, key=input_dict.get)