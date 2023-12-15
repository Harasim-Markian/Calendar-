import datetime
ban = input("Enter a Date(format: dd.mm.yy):")
day, month, year = (int(x) for x in ban.split('.'))
banan = datetime.date(year, month, day)
print(banan.strftime("%A"))