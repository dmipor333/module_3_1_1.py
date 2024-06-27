def is_contains():
    string = 'Copibara'
    list_to_search = ['Colibri', 'COMBAT', 'Copibara']  # Copibara ~ COPYbara
    def string_info():
        string = 'Copibara'
        string1 = {len(string), string.upper(), string.lower()}
        return string1
    win = string_info()
    print(win)
    print(string in list_to_search)
is_contains()
