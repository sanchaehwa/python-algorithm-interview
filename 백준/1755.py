class Solution():
    def playNumber(self, number: str):
        num1, num2 = map(int, number.split())
        dictionary = {
            1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'
        }
        reverse_dict = {v: str(k) for k, v in dictionary.items()}

        result = []
        final = []

        for i in range(num1, num2 + 1):
            if i < 10:
                val = dictionary[i]
                result.append(val)
            else:
                digits = list(map(int, str(i)))
                word = ' '.join(dictionary[d] for d in digits)
                result.append(word)

        for k in sorted(result):
            words = k.split()
            n1 = words[0]
            n2 = words[1] if len(words) > 1 else None
            number1 = reverse_dict.get(n1)
            number2 = reverse_dict.get(n2) if n2 else ''
            final.append(number1 + number2)
        for i in range(len(final)):
            print(final[i],end=' ')
            if (i+1) %10 ==0:
                print() #줄바꿈
    

number = input()
solution = Solution()
solution.playNumber(number)