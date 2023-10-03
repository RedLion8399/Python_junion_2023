from daten import woerterbuch
gespiegelt = {}

# Wörterbuch.items gibt bei jedem Schleifendurchlauf eine Liste mit zwei Elementen aus, wobei am Index 0 der key und bei [1] der Value steht.
for i in woerterbuch.items():
    gespiegelt[i[1]] = i[0]