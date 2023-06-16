"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn]."""

def shuffle(liste,n):
    newListe = []
    
    for i in range(n):
        newListe.append(liste[i])
        newListe.append(liste[i+n])
    
    return newListe

print(shuffle(liste=[1,2,3,4],n = 2))