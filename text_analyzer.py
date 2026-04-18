def normalize(doc):
    return doc.strip().lower()

def is_valid(doc):
    if doc == "":
        return False
    if doc.isdigit():
        return False
    else:
        return True

def word_count(doc):
    list_words = doc.split()
    return len(list_words)

print(normalize("     Shashank is a Software Developer     "))
print(is_valid("12345"))
print(word_count("Shashak ajhdb edakhdb akhbe wefbahefb ehdwekuyg wkahckyegh awedgywe gd aywegyuweg"))
