def counterLetter(test_str):
    all_freq = {}
  
    for i in test_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq

def solution(s1, s2):
    count=0
    count2=0
    result=0
    counterS1=counterLetter(s1)
    counterS2=counterLetter(s2)
    print(counterS1)
    print(counterS2)
    keys1=counterS1.keys()
    keys2=counterS2.keys()
    difference = keys1-keys2
    for keys in counterS1:
        if keys in difference:
            pass
        else:
            a=counterS1[keys]
            b=counterS2[keys]
            count=(a-b)
            print(count)
            if count <0:
                count2=count*(-1)
                if a>b:
                    count=a-count2
                else:
                    count=b-count2
                print(count)

            else:
                if a>b:
                    count=a-count
                else:
                    count=b-count
                print(count)
        result+=count
        count=0
    print(result)

    return count2

s1="aabcc"
s2="adcaa"
solution(s1,s2)

