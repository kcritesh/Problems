def crypted(sentence):
    translation =""
    for element in sentence:
        if element in "Aa":
            translation=translation+"1"
        elif element in "Bb":
            translation=translation+"9"
        elif element in "Cc":
            translation=translation+"2"
        elif element in "Dd":
            translation=translation+"s"
        elif element in "Ee":
            translation=translation+"d"
        elif element in "Ff":
            translation=translation+"/"
        elif element in "Gg":
            translation=translation+")"
        elif element in "Hh":
            translation=translation+"'"
        elif element in "Ii":
            translation=translation+"q"
        elif element in "Jj":
            translation=translation+"w"
        elif element in "Kk":
            translation=translation+"p"
        elif element in "Ll":
            translation=translation+"]"
        elif element in "Mm":
            translation=translation+"["
        elif element in "Nn":
            translation=translation+"o"
        elif element in "Oo":
            translation=translation+"i"
        elif element in "Pp":
            translation=translation+"e"
        elif element in "Qq":
            translation=translation+"r"
        elif element in "Rr":
            translation=translation+"t"
        elif element in "Ss":
            translation=translation+"y"
        elif element in "Tt":
            translation=translation+"u"
        elif element in "Uu":
            translation=translation+"i"
        elif element in "Vv":
            translation=translation+"b"
        elif element in "Ww":
            translation=translation+";"
        elif element in "Xx":
            translation=translation+":"
        elif element in "Yy":
            translation=translation+"T"
        elif element in "Zz":
            translation=translation+"+"
        else:
            translation = translation+element
    return translation 
print("Your Crypted Code: "+(crypted(input("Enter Your Key to Crypt: "))))

