#배열처리
import random
ary=[0]*10
for i in range(0,10):
    ary[i]=random.randint(0,1000)
#배열 값의 합계
print(ary)
sum=0
for i in range(len(ary)):
    sum+= ary[i]
print(sum)



#배열 중 홀수만 합계



