ImeFajla = input("Molim unesite ime fajla")
if len(ImeFajla) < 1 : name = "mbox-short.txt"
tekst = open(ImeFajla)
Rjecnik = dict()

for lines in tekst:
    if lines.startswith("From "):
        words = lines.split()
        email = words[1]
        Rjecnik[email] = Rjecnik.get(email, 0)+1
                   
BigRij = None
BigBroj = None

for k, v in Rjecnik.items():
    if BigBroj is None or BigBroj < v:
        BigBroj = v
        BigRij = k
print(BigRij, BigBroj)