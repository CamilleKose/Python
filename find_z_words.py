def find_z_words(words):
    liste = []
    for word in words:
        if word[0] == "z" or word[0] == "Z":
            liste.append(word)
    return liste


print(find_z_words(["zoulou", "coucou", "ouhh", "zizou", "miaou"]))