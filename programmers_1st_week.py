# 콜라츠 추측
def Collatz_conjecture(num):
    i = 0

    while (i < 500):
        if (num == 1):
            break
        elif (num % 2 == 0):
            num = num / 2
        else:
            num = (num * 3) + 1
        i += 1

    if (i >= 500):
        answer = -1
    else:
        answer = i
    
    return answer

# 하샤드 수
def Harshad_number(num):
    str_num = str(num)

    sum_num = 0
    for i in range(len(str_num)):
        sum_num += int(str_num[i])

    if num % sum_num == 0:
        answer = True
    else:
        answer = False
    return answer

# 시저 암호
def Caesar_cipher(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == " ":
            answer += s[i]
        elif ord('A') <= ord(s[i]) <= ord('Z'):
            answer += chr(((ord(s[i])+n)-ord('A'))%26+ord('A'))
        elif ord('a') <= ord(s[i]) <= ord('z'):
            answer += chr(((ord(s[i])+n)-ord('a'))%26+ord('a'))

    return answer

# 이상한 문자 만들기
def strange_letters(s):
    answer = ""
    j = 0
    for i,s in enumerate(s):
        if s == " ":
            answer += s
            j = 0
            continue
        elif (j % 2 == 0):
            answer += s.upper()
        else:
            answer += s.lower()
        j +=1
    return answer

# 실패율
def failure_rate(N, stages):
    answer_dict0 = {}
    
    for i in range(1, N+1):
        if stages.count(i) == 0:
            values = 0
        else:
            values = stages.count(i) / len([x for x in stages if x >= i])
        answer_dict0.update({i : values})
            
    answer_dict1 = sorted(answer_dict0.items(), key=lambda x: x[1], reverse = True)
    answer = [x[0] for x in answer_dict1]
    
    return answer