class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1;
        zeros=0
        for num in nums:
            if num != 0:
                product *=num
            else:
                zeros+=1

        res =[]
        if zeros==0:
            for num in nums:
                res.append(int(product/num))
        elif zeros==1:
            for num in nums:
                if num==0:
                    res.append(product)
                else:
                    res.append(0)
        else:
            for num in nums:
                res.append(0)
        return res