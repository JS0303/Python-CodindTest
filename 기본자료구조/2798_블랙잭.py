# 문제 난이도 : 하
# 문제 유형 : 배열, 완전 탐색
# 추천 풀이 시간 : 20분
n,m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

result = 0
length = len(data)

count = 0
for i in range(0, length):
	for j in range(i + 1, length):
		for k in range(j + 1, length):
			sum_value = data[i] + data[j] + data[k]
			if sum_value <= m:
				result = max(result, sum_value)

print(result)

"""
Javascript Code

let input = require("fs").readFileSync("/dev/stdin");
input = input.toString().split("\n");
let n = parseInt(input[0].split(' ')[0])
let m = parseInt(input[0].split(' ')[1])
let arr = input[1].split(' ').map(Number)
let result = 0

for (let i = 0; i < arr.length; i++){
  for (let j = i + 1; j < arr.length; j++){
    for (let k = j + 1; k < arr.length; k++){
      let sum_value = arr[i] + arr[j] + arr[k]
      if (sum_value <= m) {
        result = Math.max(result, sum_value)        
      }
    }
  }
}

console.log(result)
"""