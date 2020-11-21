def maxd(s):
    k=len(s)
    if k==0 or k==1:
        print(k)
    maxi=count(s)
    mini=k+1
    a={}
    st=0
    a[s[st]]=1
    for i in range(1,k):
        if s[i] in a:
            a[s[i]]+=1
        else:
            a[s[i]]=1
        if len(a)==maxi:
            while st<i and a[s[st]]>1:
                a[s[st]]-=1
                st+=1
            if mini>i+1-st:
                mini=i+1-st
    print(mini)
 
    
def count(s):
    p={}
    for i in s:
        if i in p:
            p[i]+=1
        else:
            p[i]=1
    return len(p)
    
s=str(input())
maxd(s)
