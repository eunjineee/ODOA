def solution(k, tangerine):
	# 딕셔너리 만들기
	ans_dict = {}
	for i in tangerine:
		if i in ans_dict:
			ans_dict[i] += 1
		else:
			ans_dict[i] = 1
	
	ans_list = list(ans_dict.values())
	ans_list.sort(reverse=True)

	ans = 0
	total = 0
	while total < k:
		total += ans_list[ans]
		ans += 1
	
	return ans

print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4,[1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2,[1, 1, 1, 1, 2, 2, 2, 3]))