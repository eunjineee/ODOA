T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    nums = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            hey = nums[i][j:j+M]
            if hey[:] == hey[::-1]:
                print(f'#{t}',end=" ")
                print(*hey,sep= "")
                break
        
    for i in range(N):
        for j in range(N):
            if i > j:
                nums[i][j], nums[j][i] = nums[j][i], nums[i][j]

    for i in range(N):
        for j in range(N-M+1):
            hey = nums[i][j:j+M]
            if hey[:] == hey[::-1]:
                print(f'#{t}',end=" ")
                print(*hey,sep= "")
                break



'''
3
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
20 13
ECFQBKSYBBOSZQSFBXKI
VBOAIDLYEXYMNGLLIOPP
AIZMTVJBZAWSJEIGAKWB
CABLQKMRFNBINNZSOGNT
NQLMHYUMBOCSZWIOBINM
QJZQPSOMNQELBPLVXNRN
RHMDWPBHDAMWROUFTPYH
FNERUGIFZNLJSSATGFHF
TUIAXPMHFKDLQLNYQBPW
OPIRADJURRDLTDKZGOGA
JHYXHBQTLMMHOOOHMMLT
XXCNJGTXXKUCVOUYNXZR
RMWTQQFHZUIGCJBASNOX
CVODFKWMJSGMFTCSLLWO
EJISQCXLNQHEIXXZSGKG
KGVFJLNNBTVXJLFXPOZA
YUNDJDSSOPRVSLLHGKGZ
OZVTWRYWRFIAIPEYRFFG
ERAPUWPSHHKSWCTBAPXR
FIKQJTQDYLGMMWMEGRUZ
'''