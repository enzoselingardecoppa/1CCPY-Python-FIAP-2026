for ex in range(2, 2001, 1):
    primo = True
    for divisor in range(2, ex, 1):
        if ex % divisor == 0:
            primo = False
            break

    if primo:
        print(ex)




