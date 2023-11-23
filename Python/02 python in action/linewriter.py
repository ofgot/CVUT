def writeTextToFile(parametr):
    STATICKY_TEXT = "This is my static text which must be added to file." \
                    " It is very long text and I do not know what they want" \
                    " to do with this terrible text. "

    fin = open("data.txt", "w")
    fin.write(STATICKY_TEXT + str(parametr))
    fin.close()

    return fin.name
