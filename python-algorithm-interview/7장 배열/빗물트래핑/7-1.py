#투 포인터, 빗물 트래핑 - 비 온 후 많은 물이 쌓일 수 있는 지 구하는 문제
#왼,오의 최대 높이가 곧 많은 물이 쌓일수있는거

class Solution():
    def trap(self,height:list[int])->int:
        
        if not height:
            return 0
        volumn = 0  #물 높이
        
        left,right = 0, len(height) - 1

        left_max,right_max = height[left],height[right]
        
        while left < right:
            left_max,right_max = max(height[left],left_max),max(height[right],right_max)
            if left_max <= right_max:
                # 더 높은쪽으로
                volumn += left_max - height[left] 
                left += 1
            else:
                volumn += right_max - height[right]
                right -= 1
        return volumn


height = list(map(int, input().split()))
solution = Solution()
print(solution.trap(height))