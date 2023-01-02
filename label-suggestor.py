# ok so basically theres a few things i need to do manually (like a big sad loser ong) and those are:
#   - make a dictionary of every sexuality this thing is gonna have
#   - create the key for each sexuality
# and then the program will
#   - ask whether the user wants to find an ace/aro spec orientation, a sexual/sexual orientation, or a gender identity
#   - ask the user questions where each answer has a value
#   - use the value that the user inputs to find the associated orientation/identity names
#   - show them to the user in order of most similar -> least similar to the user input
# how the values work
#   - each question corresponds to an index
#   - each question can be answered by one of four options
#   - i answer each question from the perspective of each sexuality and that string becomes the value
#   - the string made from the answers of the user are compared to the rest of the values, each correct letter being a point, and then the labels are displayed in order of largest amount of points to smallest amount of points

# ACE SPEC QUIZ
def ace_spec_quiz():
    aceflux = "yyssssnssssyssss"
    acespike = "synssnnssnsysyss"
    asexual = "nsnsynnnnnnnnnnn"
    demisexual = "synssnnsynnynsny"
    fictosexual = "nsssyynnnynssnnn"
    fraysexual = "synssnnsnnyyysnn"
    greysexual = "synsssnssssyssss"
    lithosexual = "synsssnsnssyysnn"
    reciprosexual = "synsssnssnnynsny"
    aegosexual = "nsynyynnnssnsnnn"
    apothisexual = "nnsyynnnnnsnynnn"
    bellussexual = "nnsnyynnsssnsnns"
    caedsexual = "nnnyynynssnnsnnn"
    cupiosexual = "nnnnsnnysnsnnnns"
    myrsexual = "yyssssnssssysyss"
    quoisexual = "rrsrrrnrrrrrryyr"
    requissexual = "nssyynynssnnsnnn"
    orientations = [aceflux, acespike, asexual, demisexual, fictosexual, fraysexual, greysexual, lithosexual, reciprosexual, aegosexual, apothisexual, bellussexual, caedsexual, cupiosexual, myrsexual, quoisexual, requissexual]
    scores = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    orientations_to_strings = {aceflux: "aceflux", acespike: "acespike", asexual: "asexual", demisexual: "demisexual", fictosexual: "fictosexual", fraysexual: "fraysexual", greysexual: "greysexual", lithosexual: "lithosexual", reciprosexual: "reciprosexual", aegosexual: "aegosexual", apothisexual: "apothisexual", bellussexual: "bellussexual", caedsexual: "caedsexual", cupiosexual: "cupiosexual", myrsexual: "myrsexual", quoisexual: "quoisexual", requissexual: "requissexual"}
    user_input = ""
    print("""would you feel comfortable saying these phrases?
possible answers:
    n - no, that doesn't sound like me.
    y - yeah, i would say that for sure.
    s - sort of/sometimes
    r - i can't say for sure.""")
    user_input += input("1 - my sexual attraction changes but i always feel it less than allosexual people. ")
    user_input += input("2 - i feel sexual attraction on occasion, but i usually do not. ")
    user_input += input("3 - if and when i fantasise about sexual relationships, it is about other people having them, not including me. ")
    user_input += input("4 - i am disgusted by the idea of sex. ")
    user_input += input("5 - i don't want to have a sexual relationship, and i'm not sexually attracted to people. ")
    user_input += input("6 - i don't feel sexual attraction, but i think certain sexual things or the aesthetic of a sexual relationship is cool, and i would want that. ")
    user_input += input("7 - i have had past trauma or experiences that made me feel a lack of sexual attraction. ")
    user_input += input("8 - i dont experience sexual attraction, but i would want to have a sexual relationship. ")
    user_input += input("9 - i dont experience sexual attraction until i really know a person. ")
    user_input += input("10 - i am sexually attracted exclusively to fictional people. ")
    user_input += input("11 - i experience sexual atttraction, but once i form a deep bond with a person, i lose it. ")
    user_input += input("12 - sometimes i experience sexual attraction, sometimes i do not. ")
    user_input += input("13 - i feel sexual attraction, but the idea of someone being sexually attracted to me makes me uncomfortable, and sometimes makes me lose those sexual feelings. ")
    user_input += input("14 - i feel like i identify with a lot of ace spec identities at once or like i fluctuate too rapidly for me to figure out what i am. ")
    user_input += input("15 - i don't understand sexual attraction, so i cant tell if i feel it or not. ")
    user_input += input("16 - i don't feel sexual attraction, but the idea of someone being sexually attracted to me can sometimes make me feel sexual attraction. ")
    for a in range(len(orientations)):
        for b in range(16):
            if user_input[b] == orientations[a][b]: scores[a] += 1
    for c in range(5):
        print(orientations_to_strings.get(orientations[scores.index(max(scores))]))
        orientations.pop(scores.index(max(scores)))
        scores.remove(max(scores))

# ARO SPEC QUIZ
def aro_spec_quiz():
    aroflux = "yyssssnssssyssss"
    arospike = "synssnnssnsysyss"
    aromantic = "nsnsynnnnnnnnnnn"
    demiromantic = "synssnnsynnynsny"
    fictoromantic = "nsssyynnnynssnnn"
    frayromantic = "synssnnsnnyyysnn"
    greyromantic = "synsssnssssyssss"
    lithoromantic = "synsssnsnssyysnn"
    reciproromantic = "synsssnssnnynsny"
    aegoromantic = "nsynyynnnssnsnnn"
    apothiromantic = "nnsyynnnnnsnynnn"
    bellusromantic = "nnsnyynnsssnsnns"
    caedromantic = "nnnyynynssnnsnnn"
    cupioromantic = "nnnnsnnysnsnnnns"
    myrromantic = "yyssssnssssysyss"
    quoiromantic = "rrsrrrnrrrrrryyr"
    requisromantic = "nssyynynssnnsnnn"
    orientations = [aroflux, arospike, aromantic, demiromantic, fictoromantic, frayromantic, greyromantic, lithoromantic, reciproromantic, aegoromantic, apothiromantic, bellusromantic, caedromantic, cupioromantic, myrromantic, quoiromantic, requisromantic]
    scores = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    orientations_to_strings = {aroflux: "aroflux", arospike: "arospike", aromantic: "aromantic", demiromantic: "demiromantic", fictoromantic: "fictoromantic", frayromantic: "frayromantic", greyromantic: "greyromantic", lithoromantic: "lithoromantic", reciproromantic: "recipromantic", aegoromantic: "aegoromantic", apothiromantic: "apothiromantic", bellusromantic: "bellusromantic", caedromantic: "caedromantic", cupioromantic: "cupioromantic", myrromantic: "myrromantic", quoiromantic: "quoiromantic", requisromantic: "requisromantic"}
    user_input = ""
    print("""would you feel comfortable saying these phrases?
possible answers:
    n - no, that doesn't sound like me.
    y - yeah, i would say that for sure.
    s - sort of/sometimes
    r - i can't say for sure.""")
    user_input += input("1 - my romantic attraction changes but i always feel it less than alloromantic people. ")
    user_input += input("2 - i feel romantic attraction on occasion, but i usually do not. ")
    user_input += input("3 - if and when i fantasise about romantic relationships, it is about other people having them, not including me. ")
    user_input += input("4 - i am disgusted by the idea of romance. ")
    user_input += input("5 - i don't want to have a romantic relationship, and i'm not romantically attracted to people. ")
    user_input += input("6 - i don't feel romantic attraction, but i think certain romantic things or the aesthetic of a romantic relationship is cool, and i would want that. ")
    user_input += input("7 - i have had past trauma or experiences that made me feel a lack of romantic attraction. ")
    user_input += input("8 - i dont experience romantic attraction, but i would want to have a romantic relationship. ")
    user_input += input("9 - i dont experience romantic attraction until i really know a person. ")
    user_input += input("10 - i am romantically attracted exclusively to fictional people. ")
    user_input += input("11 - i experience romantic atttraction, but once i form a deep bond with a person, i lose it. ")
    user_input += input("12 - sometimes i experience romantic attraction, sometimes i do not. ")
    user_input += input("13 - i feel romantic attraction, but the idea of someone being romantically attracted to me makes me uncomfortable, and sometimes makes me lose those romantic feelings. ")
    user_input += input("14 - i feel like i identify with a lot of aro spec identities at once or like i fluctuate too rapidly for me to figure out what i am. ")
    user_input += input("15 - i don't understand romantic attraction, so i cant tell if i feel it or not. ")
    user_input += input("16 - i don't feel romantic attraction, but the idea of someone being romantically attracted to me can sometimes make me feel romantic attraction. ")
    for a in range(len(orientations)):
        for b in range(16):
            if user_input[b] == orientations[a][b]: scores[a] += 1
    for c in range(5):
        print(orientations_to_strings.get(orientations[scores.index(max(scores))]))
        orientations.pop(scores.index(max(scores)))
        scores.remove(max(scores))
        
# GENDER IDENTITY QUIZ
def gender_iden_quiz():
    pass

# ROMANTIC ORIENTATION QUIZ
def romantic_orient_quiz():
    androromantic = "cbbbbbbbab-bb"
    androgynoromantic = "bcbbbbbbab-bb"
    autoromantic = "bbcbbbbbab-ac"
    biromantic = "bbbcbbbbab-cc"
    gynoromantic = "bbbbcbbbab-bb"
    heteroromantic = "bbaabaaaaa-ca"
    homoromantic = "bbbabaaaab-ac"
    omniromantic = "ccbcccaaac-cc"
    panromantic = "ccbcacaaac-cc"
    polyromantic = "bbbcbaacab-bb"
    sapioromantic = "bbbbbbbcb-bb"
    skolioromantic = "bbbbbbbac-xx"
    orientations = [androromantic, androgynoromantic, autoromantic, biromantic, gynoromantic, heteroromantic, homoromantic, omniromantic, panromantic, polyromantic, sapioromantic, skolioromantic]
    scores = [0,0,0,0,0,0,0,0,0,0,0,0]
    orientations_to_strings = {androromantic: "androromantic", androgynoromantic: "androgynoromantic", autoromantic: "autoromantic", biromantic: "biromantic", gynoromantic: "gynoromantic", heteroromantic: "heteroromantic", homoromantic: "homoromantic", omniromantic: "omniromantic", panromantic: "panromantic", polyromantic: "polyromantic", sapioromantic: "sapioromantic", skolioromantic: "skolioromantic"}
    user_input = ""
    print("""report the amount you agree with each statement.
a - not at all.
b - i partially agree, or i do not know.
c - i agree.""")
    user_input += input("i am attracted to masculinity. ")
    user_input += input("i am attracted to androgeny. ")
    user_input += input("i am attracted to myself. ")
    user_input += input("i am attracted to two or more genders. ")
    user_input += input("i am attracted to femininity. ")
    user_input += input("i am attracted to all genders, but i have preference. i am not gender-blind. ")
    user_input += input("i am attracted to all genders, and i have no preference. i am gender-blind. ")
    user_input += input("i am attracted to multiple genders, but not all. ")
    user_input += input("i am attracted to intelligence, not gender. ")
    user_input += input("i am attracted to nonbinary people. ")
    user_input += "-"
    nonbinary = input("are you nonbinary/genderqueer? y/n: ")
    if nonbinary == "n":
        user_input += input("i am attracted to the opposite gender of my own. ")
        user_input += input("i am attracted to the same gender as my own. ")
    for a in range(len(orientations)):
        for b in range(10):
            if user_input[b] == orientations[a][b]: scores[a] += 2
            elif user_input[b] == 'b' and (orientations[a][b] == 'a' or orientations[a][b] == 'c'): scores[a] += 1
            elif (user_input[b] == 'a' or user_input[b] == 'c') and orientations[a][b] == 'b': scores[a] += 1
        if nonbinary == "n":
            for b in range(10, 12):
                if user_input[b] == orientations[a][b]: scores[a] += 2
                elif user_input[b] == 'b' and (orientations[a][b] == 'a' or orientations[a][b] == 'c'): scores[a] += 1
                elif (user_input[b] == 'a' or user_input[b] == 'c') and orientations[a][b] == 'b': scores[a] += 1
    for c in range(5):
        print(orientations_to_strings.get(orientations[scores.index(max(scores))]))
        orientations.pop(scores.index(max(scores)))
        scores.remove(max(scores))

# SEXUAL ORIENTATION QUIZ
def sexual_orient_quiz():
    androsexual = "cbbbbbbbab-bb"
    androgynosexual = "bcbbbbbbab-bb"
    autosexual = "bbcbbbbbab-ac"
    bisexual = "bbbcbbbbab-cc"
    gynosexual = "bbbbcbbbab-bb"
    heterosexual = "bbaabaaaaa-ca"
    homosexual = "bbbabaaaab-ac"
    omnisexual = "ccbcccaaac-cc"
    pansexual = "ccbcacaaac-cc"
    polysexual = "bbbcbaacab-bb"
    sapiosexual = "bbbbbbbcb-bb"
    skoliosexual = "bbbbbbbac-xx"
    orientations = [androsexual, androgynosexual, autosexual, bisexual, gynosexual, heterosexual, homosexual, omnisexual, pansexual, polysexual, sapiosexual, skoliosexual]
    scores = [0,0,0,0,0,0,0,0,0,0,0,0]
    orientations_to_strings = {androsexual: "androsexual", androgynosexual: "androgynosexual", autosexual: "autosexual", bisexual: "bisexual", gynosexual: "gynosexual", heterosexual: "heterosexual", homosexual: "homosexual", omnisexual: "omnisexual", pansexual: "pansexual", polysexual: "polysexual", sapiosexual: "sapiosexual", skoliosexual: "skoliosexual"}
    user_input = ""
    print("""report the amount you agree with each statement.
a - not at all.
b - i partially agree, or i do not know.
c - i agree.""")
    user_input += input("i am attracted to masculinity. ")
    user_input += input("i am attracted to androgeny. ")
    user_input += input("i am attracted to myself. ")
    user_input += input("i am attracted to two or more genders. ")
    user_input += input("i am attracted to femininity. ")
    user_input += input("i am attracted to all genders, but i have preference. i am not gender-blind. ")
    user_input += input("i am attracted to all genders, and i have no preference. i am gender-blind. ")
    user_input += input("i am attracted to multiple genders, but not all. ")
    user_input += input("i am attracted to intelligence, not gender. ")
    user_input += input("i am attracted to nonbinary people. ")
    user_input += "-"
    nonbinary = input("are you nonbinary/genderqueer? y/n: ")
    if nonbinary == "n":
        user_input += input("i am attracted to the opposite gender of my own. ")
        user_input += input("i am attracted to the same gender as my own. ")
    for a in range(len(orientations)):
        for b in range(10):
            if user_input[b] == orientations[a][b]: scores[a] += 2
            elif user_input[b] == 'b' and (orientations[a][b] == 'a' or orientations[a][b] == 'c'): scores[a] += 1
            elif (user_input[b] == 'a' or user_input[b] == 'c') and orientations[a][b] == 'b': scores[a] += 1
        if nonbinary == "n":
            for b in range(10, 12):
                if user_input[b] == orientations[a][b]: scores[a] += 2
                elif user_input[b] == 'b' and (orientations[a][b] == 'a' or orientations[a][b] == 'c'): scores[a] += 1
                elif (user_input[b] == 'a' or user_input[b] == 'c') and orientations[a][b] == 'b': scores[a] += 1
    for c in range(5):
        print(orientations_to_strings.get(orientations[scores.index(max(scores))]))
        orientations.pop(scores.index(max(scores)))
        scores.remove(max(scores))

romantic_orient_quiz()