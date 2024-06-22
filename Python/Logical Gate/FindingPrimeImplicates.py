def check(num1, num2):
    combine = ""
    count1 = 0
    for i in range(len(num1)):
        if num1[i] == num2[i]:
            count1 += 1
            combine += '-'
        else:
            combine += num1[i]
    if count1 == 1:
        return combine
    else:
        return None



def solution(minterm):
    num_length = minterm[0]
    minterm = minterm[2:]

    minterm_binary = list()
    for i in minterm:
        minterm_binary.append()