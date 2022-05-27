def Vowels(word): 
    list_vowels = ['a', 'e', 'i', 'o', 'u']
    result = list()
    for letter in word: 
        k = letter.lower()
        if ( k in list_vowels ) and (k not in result ):
            result.append(k)
    print ('Vowels:', result)  
Vowels('Umuzi')        


