def mergeword():
    word1=input("Enter the first word: ")
    word2=input("Enter the second word: ")
    len1, len2=len(word1), len(word2);
    result=""

    for i in range(max(len1, len2)):
        if i < len1:                     
            result+=word1[i]
        if i < len2:
            result+=word2[i]

    return result;
print(mergeword())