import sys

test_case_cnt = 1
for i, line in enumerate(sys.stdin):
    if i != 0:
        if i % 2 == 0:
            nums = list(map(int,line.split()))
            nums.sort()
            max_straight = 0
            for j in range(len(nums)):
                if nums[j] > max_straight:
                    max_straight += 1
            print("Case #" + str(test_case_cnt) + ": " + str(max_straight))
            test_case_cnt += 1

