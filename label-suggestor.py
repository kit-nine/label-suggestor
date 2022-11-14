# ok so basically theres a few things i need to do manually (like a big sad loser ong) and those are:
#   - make a dictionary of every sexuality this thing is gonna have
#   - create the key for each sexuality
# and then the program will
#   - ask whether the user wants to find an ace/aro spec orientation, a romantic/sexual orientation, or a gender identity
#   - ask the user questions where each answer has a value
#   - use the value that the user inputs to find the associated orientation/identity names
#   - show them to the user in order of most similar -> least similar to the user input
# how the values work
#   - each question corresponds to an index
#   - each question can be answered by one of four options
#   - i answer each question from the perspective of each sexuality and that string becomes the value
#   - the string made from the answers of the user are compared to the rest of the values, each correct letter being a point, and then the labels are displayed in order of largest amount of points to smallest amount of points

# ACE SPEC QUIZ

# would you feel comfortable saying these phrases?
# possible answers:
#  n - no, that doesn't sound like me.
#  y - yeah, i would say that for sure.
#  s - sort of/sometimes
#  r - i don't really know whether i would...

# questions:
#  0 - my sexual attraction changes but i always feel it less than allosexual people.
#  1 - i feel sexual attraction on occasion, but i usually do not.
#  2 - if and when i fantasise about sex, it is about other people having it, not including me.
#  3 - i am disgusted by the idea of sex.
#  4 - i don't want to have sex and i'm not sexually attracted to people.
#  5 - i don't feel sexual attraction, but i think certain sexual things or the aesthetic of a sexual relationship is cool and i would want that.
#  6 - i have had past trauma or experiences that made me feel a lack of sexual attraction.
#  7 - i dont experience sexual attraction, but i would want to have a sexual relationship.
#  8 - i dont experience sexual attraction until i really know a person.
#  9 - i am sexually attracted exclusively to fictional people.
#  10 - i experience sexual atttraction, but once i form a deep bond with a person i lose it.
#  11 - sometimes i experience sexual attraction, sometimes i do not.
#  12 - i feel sexual attraction, but the idea of someone being sexually attracted to me makes me uncomfortable, and sometimes makes me lose those sexual feelings.
#  13 - i feel like i identify with a lot of ace spec identities at once or like i fluctuate too rapidly for me to figure out what i am.
#  14 - i don't understand sexual attraction, so i cant tell if i feel it or not.
#  15 - i don't feel sexual attraction, but the idea of someone being sexually attracted to me can 
aceflux = "yyssssnssssysyss"
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

# ARO SPEC QUIZ
def aro_spec_quiz():
    aroflux = "yyssssnssssysyss"
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
    score_0, score_1, score_2, score_3, score_4, score_5, score_6, score_7, score_8, score_9, score_10, score_11, score_12, score_13, score_14, score_15, score_16 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    orientations = [aroflux, arospike, aromantic, demiromantic, fictoromantic, frayromantic, greyromantic, lithoromantic, reciproromantic, aegoromantic, apothiromantic, bellusromantic, caedromantic, cupioromantic, myrromantic, quoiromantic, requisromantic]
    scores = [score_0, score_1, score_2, score_3, score_4, score_5, score_6, score_7, score_8, score_9, score_10, score_11, score_12, score_13, score_14, score_15, score_16]
    orientations_to_scores = {aroflux: score_0, arospike: score_1, aromantic: score_2, demiromantic: score_3, fictoromantic: score_4, frayromantic: score_5, greyromantic: score_6, lithoromantic: score_7, reciproromantic: score_8, aegoromantic: score_9, apothiromantic: score_10, bellusromantic: score_11, caedromantic: score_12, cupioromantic: score_13, myrromantic: score_14, quoiromantic: score_15, requisromantic: score_16}
    user_input = ""
    print("""would you feel comfortable saying these phrases?
possible answers:
    n - no, that doesn't sound like me.
    y - yeah, i would say that for sure.
    s - sort of/sometimes
    r - i can't say for sure.""")
    user_input += input("1 - my romantic attraction changes but i always feel it less than alloromantic people.")
    user_input += input("2 - i feel romantic attraction on occasion, but i usually do not.")
    user_input += input("3 - if and when i fantasise about romantic relationships, it is about other people having them, not including me.")
    user_input += input("4 - i am disgusted by the idea of romance.")
    user_input += input("5 - i don't want to have a romantic relationship, and i'm not romantically attracted to people.")
    user_input += input("6 - i don't feel romantic attraction, but i think certain romantic things or the aesthetic of a romantic relationship is cool, and i would want that.")
    user_input += input("7 - i have had past trauma or experiences that made me feel a lack of romantic attraction.")
    user_input += input("8 - i dont experience romantic attraction, but i would want to have a romantic relationship.")
    user_input += input("9 - i dont experience romantic attraction until i really know a person.")
    user_input += input("10 - i am romantically attracted exclusively to fictional people.")
    user_input += input("11 - i experience romantic atttraction, but once i form a deep bond with a person, i lose it.")
    user_input += input("12 - sometimes i experience romantic attraction, sometimes i do not.")
    user_input += input("13 - i feel romantic attraction, but the idea of someone being romantically attracted to me makes me uncomfortable, and sometimes makes me lose those romantic feelings.")
    user_input += input("14 - i feel like i identify with a lot of aro spec identities at once or like i fluctuate too rapidly for me to figure out what i am.")
    user_input += input("15 - i don't understand romantic attraction, so i cant tell if i feel it or not.")
    user_input += input("16 - i don't feel romantic attraction, but the idea of someone being romantically attracted to me can sometimes make me feel romantic attraction.")
    for a in orientations:
        for b in range(15):
            if user_input[b] == a[b]:
                c = orientations_to_scores.get(a)
                c += 1
# GENDER IDENTITY QUIZ

# ROMANTIC ORIENTATION QUIZ

# SEXUAL ORIENTATION QUIZ

aro_spec_quiz()