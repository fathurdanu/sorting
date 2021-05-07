def radixLSD(data):
    RADIX = 10
    list_bantu = [[] for i in range(20)]  
    posisi_terakhir = False
    pembagi = 1
    while not posisi_terakhir:
        posisi_terakhir = True
       
        for i in data:
            tmp = i // pembagi
            if i < 0:
                list_bantu[(tmp % RADIX)].append(i)
            else:
                list_bantu[(tmp % RADIX)+10].append(i)
            if posisi_terakhir and tmp > 0:
                posisi_terakhir = False

        a = 0
        for nilai in list_bantu:
            for i in nilai:
                data[a] = i
                a += 1
            nilai.clear()
        pembagi *= RADIX
        
    return data

if __name__ == "__main__":
    arr1 = [2,4,6,8,-23,7,5,3,1,-1,-6]
    print(radixLSD(arr1))
