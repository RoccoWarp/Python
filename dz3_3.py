def thesaurus(*names):
    dic_names = {}
    for name in names:
        if name[0] in dic_names:
            dic_names[name[0]].append(name)
        else:
            dic_names[name[0]] = [name]
    return dic_names


print(thesaurus('Lorgar', 'Roboute ', 'Leman', 'Horus', 'Mortarion'))
