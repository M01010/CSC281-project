from functions import findMissing

isbns = ["15688?111x",
         "1X688?111X",
         "156881111?",
         "000000000?",
         "493?568419",
         "493??68419",
         "4930568419",
         "15@881111X",
         "007288008?",
         "0072880?82",
         "12345?789X",
         "188879997?",
         "?888799978",
         "1888?99978",
         "0321500?18",
         "030640615?",
         "12345",
         "15688A1115",
         "18887999?8"
         ]
for isbn in isbns:
    print(f"ISBN:", isbn)
    try:
        result = findMissing(isbn)
        print("Correct ISBN is:", result)
    except Exception as e:
        print(e)
    print()
