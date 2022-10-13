import orjson

font_size = 8
px_conversion = 4/5
WIDTH = 550
displayable_characters = int(WIDTH / (px_conversion * font_size))

############# Formatting Stuff ############3
hr = "${hr 1}"
bold = "${font monospace:bold:size=8}"
italic = "${font monospace:italic:size=8}"
light = "${font monospace:light:size=8}"
alignr = "${alignr}"

############# Formatting Stuff ############3

with open('/home/sterlingbutters/Utilities/conky-tools/mail.json', 'rb') as f:
    MAIL_DICT = orjson.loads(f.read())

for email in MAIL_DICT.keys():

    # To scroll vis characters
    with open('/home/sterlingbutters/Utilities/conky-tools/mail.json', 'wb') as f:
        MAIL_DICT[email]['m'] += 1
        STRING = MAIL_DICT[email]['Body']
        b = displayable_characters
        if MAIL_DICT[email]['m'] + b >= len(STRING):
            MAIL_DICT[email]['m'] = 0
        f.write(orjson.dumps(MAIL_DICT))

        print(hr)
        print(bold + "Subject: " + MAIL_DICT[email]['Subject'] + alignr + italic + "Date: " + MAIL_DICT[email]['Date'])
        print(italic + "From: " + MAIL_DICT[email]['From'] + light)
        print()
        print("{}".format(STRING[MAIL_DICT[email]['m']: b + MAIL_DICT[email]['m']]))
        print(hr)

    # To scroll by words
    # with open('/home/sterlingbutters/Utilities/conky-tools/mail.json', 'w') as f:
    #     MAIL_DICT[email]['m'] += 2      # Number of words to "load" at one time
    #     words = MAIL_DICT[email]['Body'].split()
    #     b = 20                          # Guess for number of words that can fit in WIDTH
    #     test = len(" ".join(words[a+MAIL_DICT[email]['m'] : b+MAIL_DICT[email]['m']]))
    #     while test > displayable_characters:
    #         b -= 1
    #         test = len(" ".join(words[MAIL_DICT[email]['m']: b + MAIL_DICT[email]['m']]))
    #
    #     if MAIL_DICT[email]['m'] + b >= len(words):
    #         MAIL_DICT[email]['m'] = 0
    #
    #     json.dump(MAIL_DICT, f, indent=4)
    #
    #     print(hr)
    #     print(bold+"Subject: "+ MAIL_DICT[email]['Subject']+alignr+italic+"Date: "+MAIL_DICT[email]['Date'])
    #     print(italic+"From: "+MAIL_DICT[email]['From']+light)
    #     print()
    #     print("{}".format(" ".join(words[a + MAIL_DICT[email]['m']: b + MAIL_DICT[email]['m']])))
    #     print(hr)

