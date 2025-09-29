students = []
# En evig loop som kör tills användaren avslutar programmet
while True:
    # Menyval för användaren 
    print("\nMeny:")
    print("1. Lägg till student")
    print("2. Lista alla studenter")
    print("3. Avsluta")
    choice = input("Välj ett alternativ (1-3): ")
#if sats för valen i menyn
    if choice == "1":
        namn = input("Ange studentens namn: ")
        ålder = input("Ange studentens ålder: ")
        student = {"namn": namn, "ålder": ålder}
        students.append(student)
        print(f"Studenten {namn} har lagts till.")


# elif för att visa listan med studenter, Enumerate för att få både index och värde
    elif choice == "2":
        print("\nLista över studenter:")
        for i, student in enumerate(students, 1):
            print(f"{i}. Namn: {student['namn']}, Ålder: {student['ålder']}")
        if not students:
            print("Inga studenter tillagda.")
    elif choice == "3":
        print("Avslutar programmet.")
        break
    else:
        print("Ogiltigt val, försök igen.")
#Först steget för Menyn där tillägg av studenter med namn och ålder. Även en visning av listan vid tillägg.