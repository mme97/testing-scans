def keyerror_noncompliant():
    mydict = {1: 1, 2: 2, 3: 3}
    key = 5
    print('mydict', mydict)
    try:
        # Noncompliant: uses [] which causes exception when key is not found.
        count = mydict[key]
    except KeyError:
        count = 0
    return count
