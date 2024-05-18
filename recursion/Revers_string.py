def reverse(text):
    if len(text)==0:
        return text
    else:
        return text[len(text)-1] + reverse(text[0:len(text)-1])