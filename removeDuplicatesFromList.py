def removeDuplicatesFromList(l):
    i = 0
    while i < len(l):
        g = len(l) - 1
        while g > i:
            if l[i] == l[g]:
                del l[g]
            g -= 1
        i += 1