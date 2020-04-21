def solution(lines):
    max_count = 0
    for i in range(len(lines)):
        _, time, T = lines[i].split(' ')
        h, m, s = map(float, time.split(':'))
        processing_start_time = round(s + m * 60 + h * 3600, 3)
        processing_end_time = round(processing_start_time + 1 - 0.001, 3)
        count = 1

        for j in range(i+1, len(lines)):
            _, time, T = lines[j].split(' ')
            h, m, s = map(float, time.split(':'))
            end_time = round(s + m * 60 + h * 3600, 3)
            start_time = round(end_time - float(T.strip('s')) + 0.001, 3)
            if processing_start_time <= start_time <= processing_end_time or processing_start_time <= end_time <= processing_end_time:
                count += 1
            elif processing_start_time >= start_time and processing_end_time <= processing_end_time:
                count +=1

        max_count = max(max_count, count)
    return max_count


print(solution(	["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))