#현재 보다 커 , 근데 그 큰 숫자들중에서 이제 제일작아, 현재 다음으로 오는 수 를 구하라, 다음 순서
class Solution:
    def largeAndSmallNumber(self, number: str) -> int:
        nums = list(map(int, number.strip()))
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:  # 변곡점 발생
                for j in range(len(nums) - 1, i, -1):  # 뒤에서부터 i보다 큰 수 찾기
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]  # 스왑
                        break
                nums[i + 1:] = sorted(nums[i + 1:])  # 뒷부분 정렬
                print(''.join(map(str, nums)))
                return
        print(0)  

        
number = input()
solution = Solution()
solution.largeAndSmallNumber(number)