def lenghtOfLastWord(x):
    kelime = ""
    sonKelime = ""
    for i in x:
        if i != " ":
            kelime += i
            sonKelime = kelime 
        else:
            kelime = ""
            
    if kelime == "":
        return len(sonKelime)
    return len(kelime)

lenghtOfLastWord("luffy is still joyboy ")