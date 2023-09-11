# 문제 난이도  : 하
# 문제 유형 : 배열, 구현
# 추천 풀이 시간 : 15분

a = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1, 8):
    if a[i] > a[i-1]:
        descending = False
    elif a[i] < a[i-1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')

"""
Javascript Code

let input = require("fs").readFileSync("/dev/stdin");
input = input.toString().split("\n");
arr = input[0].split(' ').map(Number)

let ascending = true
let descending = true
for (let i = 0; i < arr.length; i++){
  if (arr[i] < arr[i-1]){
    ascending = false
  } else if (arr[i] > arr[i-1]){
    descending = false
  }
}

if(ascending){
  console.log('ascending')
} else if (descending){
  console.log('descending')
} else {
  console.log('mixed')
}
"""