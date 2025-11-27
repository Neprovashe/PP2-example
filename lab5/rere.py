import re
import string
a = "sdlsadsn"
def is_a(text):
    return bool(re.search("a", text))


def is_ab(text):
    return (bool(re.search("abb", text)) or bool(re.search("abbb", text))) and not bool(re.search("abbbb", text))

#print(is_ab("abbbb"))

def lower_dash(text):
    return bool(re.search("[a-z]_[a-z]", text))


#print(lower_dash("hi_a"))


def upper_low(text):
    return bool(re.search("[A-Z][a-z]", text))


#print(upper_low("dA"))

def a_b(text):
    return bool(re.search(r"a.*b$", text))

#print(a_b("jdshaldksba"))

def replace(text):
    return re.sub(r"[ ,.]", ":", text)

#   print(replace("Hello, I am,."))


def snake_camel(text):
    for i in range(len(text)):
        if i<len(text):
            if  text[i]=="_":
                text = text[:i] + text[i+1:].capitalize()
            #text[i] = text[i].upper()
    return text

#print(snake_camel("Hello_friends_hi"))



def split_at_upper(text):
    return re.split(r"([A-Z])", text)



def insert_space(text):
    return re.sub(r"([a-z])([A-Z])", r"\1 \2", text)

def camel_snake(text):
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", text)


print(camel_snake("CamelSnakeCat"))


def phone(text):
    return bool(re.findall(r"^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$", text))

print(phone("12345678911"))