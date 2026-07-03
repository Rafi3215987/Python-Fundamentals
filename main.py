_kolarNam = list()

_kolarNam.append("champaKola")
print(_kolarNam)

kolarNam  : set[str] = set()

kolarNam.add("chamPaKola")
kolarNam.add("golPaKola")

print(kolarNam)

__kolarNam : dict[int, str] = dict()

__kolarNam[0] = "champaKola"

print(__kolarNam)

___kolarNam : tuple[str] = tuple()

#___kolarNam.insert("paglaKola") this is not possible because tuples are immutable

print(___kolarNam)