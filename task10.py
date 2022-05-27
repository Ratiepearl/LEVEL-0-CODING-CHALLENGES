def common_letters(word1,word2):
    common1 = set(word1)
    common2 = set(word2)
    common = common1&common2
    return common    
print('common letters: ' , common_letters('house','computers'))

