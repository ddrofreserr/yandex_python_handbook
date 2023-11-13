def cycle(nums):
    for each in nums:
        yield each
        nums += [each]
