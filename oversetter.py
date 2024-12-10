def translator():
    # Ordbok som inneholder oversettelser
    translation_dict = {
        'hello': {
            'en': 'hello',
            'es': 'hola',
            'no': 'hallo'
        },
        'goodbye': {
            'en': 'goodbye',
            'es': 'adiós',
            'no': 'ha det'
        },
        'please': {
            'en': 'please',
            'es': 'por favor',
            'no': 'vær så snill'
        },
        'thank you': {
            'en': 'thank you',
            'es': 'gracias',
            'no': 'takk'
        },
        'yes': {
            'en': 'yes',
            'es': 'sí',
            'no': 'ja'
        },
        'no': {
            'en': 'no',
            'es': 'no',
            'no': 'nei'
        }
    }

    print("Welcome to the Python Translator!")
    print("Languages supported: en (English), es (Spanish), no (Norwegian)")

    while True:
        # Brukerinput
        word = input("Enter the word you want to translate (or write #stop to exit): ").lower()

        if word == "#stop":
            print("Exiting the translator. Goodbye!")
            break

        # Finn riktig nøkkel uavhengig av språk
        found_word = None
        for key, translations in translation_dict.items():
            if word in translations.values():
                found_word = key
                break

        # Oversettelse
        if found_word:
            translations = translation_dict[found_word]
            print("Translations:")
            print(f"English: {translations['en']}")
            print(f"Spanish: {translations['es']}")
            print(f"Norwegian: {translations['no']}")
        else:
            print(f"Sorry, the word '{word}' is not in the dictionary.")

# Kjører oversettelsesprogrammet
translator()
