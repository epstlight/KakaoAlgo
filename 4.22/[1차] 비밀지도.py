def solution(n, arr1, arr2):
    answer = []
    tempArr = [[0] * n for _ in range(n)]
    for j in range(len(arr1)):
        temp = str(format(arr1[j], 'b'))
        index = n - 1
        for i in range(len(temp) - 1, -1 , -1):
            if temp[i] == "1":
                tempArr[j][index] = 1
            index -= 1

    for j in range(len(arr2)):
        temp = str(format(arr2[j], 'b'))
        index = n - 1
        for i in range(len(temp) - 1, -1 , -1):
            if temp[i] == "1":
                tempArr[j][index] = 1
            index -= 1

    for arr in tempArr:
        temp = ""
        for number in arr:
            if number:
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
    return answer