def balance(expression):
    seqq = []
    brackets = {')': '(', ']': '[', '}': '{', '>': '<'}
    
    for char in expression:
        if char in '([{<': seqq.append(char)
        elif char in ')]}>':
            if not seqq or not seqq.pop() == brackets[char]:  return False
            
    return not seqq

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None

def write_file(file_path, results):
    try:
        with open(file_path, 'w') as file:
            for result in results:
                file.write(f"{result}\n")
        print(f"The results have been successfully written to {file_path}")
    except IOError as e:
        print(f"File write error: {e}")


expressions = read_file('input.txt')
if expressions is not None:
    results = []
    for expression in expressions:
        results.append(balance(expression.strip()))
    
    write_file('output.txt', results)