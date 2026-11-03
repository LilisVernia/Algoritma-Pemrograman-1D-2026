def palindron(kata):
    kata_balik= kata[::-1]

    print("hasil kata balik = ", kata_balik)

    if kata == kata_balik:
         print("Termasuk palindrom")
    else:
         print("Bukan termasuk palindrom")

kata = input("Masukan kata= ")
palindron(kata)

