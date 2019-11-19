def nss(n):
    s1  = (n * (n+1) * ((2*n)+1))/6
    s2  = ((n*(n+1))/2)**2
    return int(s2-s1)
if __name__ == "__main__":
    n = int(input())
    if(n>=0):
        print(nss(n))
