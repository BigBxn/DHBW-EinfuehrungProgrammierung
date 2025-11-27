def mittelwert(liste):
    return sum(liste) / len(liste)

def median(liste):
    sortiert = sorted(liste)
    n = len(sortiert)
    mitte = n // 2

    if n % 2 == 1:
        return sortiert[mitte]
    else:
        return (sortiert[mitte - 1] + sortiert[mitte]) / 2

def minimum(liste):
    return min(liste)

def maximum(liste):
    return max(liste)

werte = [12, 5, 8, 21, 7, 14]

print("Liste:", werte)
print("Mittelwert:", mittelwert(werte))
print("Median:", median(werte))
print("Minimum:", minimum(werte))
print("Maximum:", maximum(werte))
