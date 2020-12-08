

def main():
    n = int(input())
    results = []
    for i in range(n):
        nums = list(map(int, input().split(' ')))
        init_nums = nums
        while not all(x == nums[0] for x in nums):
            nums = sorted(nums)
            nums[-1] = nums[-1] - nums[0]
        nums[-1] = int(init_nums[0] * init_nums[-1] / nums[0])
        results.append('({})'.format(' '.join(map(str, nums))))
    print(' '.join(results))



if __name__ =='__main__':
    main()