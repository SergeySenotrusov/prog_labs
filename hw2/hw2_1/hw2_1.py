try:
    grade_avg = 0
    line_count = 0
    with open('input.txt', 'r') as file:
        for line in file:
            line_count += 1
            grade_avg += int(line.split(',')[1])
        
        grade_avg = grade_avg / line_count

    with open('input.txt', 'r') as file:
        with open('output.txt', 'w') as file2:
            for line in file:
                if int(line.split(',')[1]) >= grade_avg:
                    file2.write(line)

except FileNotFoundError:
    print("File 'input.txt' not found")