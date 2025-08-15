class Solution:
    def dna(self) -> None:
        # DNA의 수 d, 문자열 길이 m
        d, m = map(int, input().split())
        dna = [list(input()) for _ in range(d)]  # d개의 문자열 입력
        d1 = ''  # 정답 DNA 문자열
        cnt = 0  # Hamming Distance 합계

        for i in range(m):  # 각 열 (문자 위치)별로
            hamming = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
            for j in range(d):  # 각 DNA에서 해당 위치 문자 세기
                hamming[dna[j][i]] += 1
            # 가장 많이 나온 문자 중 사전 순으로 가장 빠른 문자 선택
            max_count = max(hamming.values())
            candidates = [key for key, val in hamming.items() if val == max_count]
            char = min(candidates)
            d1 += char
        # Hamming Distance 계산
        for seq in dna:
            for i in range(m):
                if seq[i] != d1[i]:
                    cnt += 1
        print(d1)
        print(cnt)

solution = Solution()
solution.dna()