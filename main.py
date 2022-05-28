# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word,anagram):    
    check = len(word) ==len(anagram)

    if check == True:
        count1 = {}
        for i in word :
            if i in count1:
                count1[i] += 1
            else:
                count1[i] = 1
        #print(count1)

        count2 = {}
        for i in anagram :
            if i in count2:
                count2[i] += 1
            else:
                count2[i] = 1
        #print(count2)

        if count1 == count2:
            print("True")
        else:
            print("False")
    
    else:
        print("False")


find_anagram("hello", "check")
find_anagram("below", "elbow") 
    
        







           

                    

                   
                
        

    
    

