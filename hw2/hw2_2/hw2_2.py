try:
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    symb_rmv = input("Enter the characters: ")

    def remove_symbols(line, symbols):
        while line and line[-1] in symbols:
            line = line[:-1]
        return line

    processed_lines = []
    for line in lines:
        line = line.rstrip()
        line = remove_symbols(line, symb_rmv) + ';'
        symb_rmv.append(line[::-1])

    with open('output.txt', 'w') as file:
        for line in processed_lines:
            file.write(line + '\n')

except FileNotFoundError:
    print("File 'input.txt' not found")