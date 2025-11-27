
def vowels(s):
    ans = 0
    for i in s.lower():
        if i in "aeyuio":
            ans+=1
    print(ans)





vowels("hello")