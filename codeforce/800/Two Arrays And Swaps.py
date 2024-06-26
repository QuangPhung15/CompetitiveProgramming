def solve(n, k, nums1, nums2):
	nums1.sort()
	nums2.sort(reverse = True)

	for i in range(k):
		for j in range(n):
			if (nums1[j] < nums2[j]):
				nums1[j], nums2[j] = nums2[j], nums1[j]
				break

	return sum(nums1)

t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	nums1 = list(map(int, input().split()))
	nums2 = list(map(int, input().split()))
	print(solve(n, k, nums1, nums2))