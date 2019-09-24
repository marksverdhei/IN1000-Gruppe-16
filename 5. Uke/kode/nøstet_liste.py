buss1 = ["09:00", "13:00", "17:00"]
buss2 = ["08:15", "14:15", "20:15"]
buss3 = ["15:27", "16:27", "17:27"]

busstider = [buss1, buss2, buss3]

for i in range(len(busstider)):
    print("Buss", i+1)
    for tid in busstider[i]:
        print(tid)
