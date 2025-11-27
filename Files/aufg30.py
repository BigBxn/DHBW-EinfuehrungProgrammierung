def ist_sicher(passwort):
    if len(passwort) < 8:
        return False

    if not any(character.isdigit() for character in passwort):
        return False

    if not any(character.isupper() for character in passwort):
        return False

    return True


pw = input("Bitte ein Passwort eingeben: ")

if ist_sicher(pw):
    print("Das Passwort ist sicher.")
else:
    print("Das Passwort ist NICHT sicher.")
