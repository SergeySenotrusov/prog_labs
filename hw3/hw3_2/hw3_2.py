def get_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = {}
            current_store = None
            for line in file:
                line = line.strip()
                if line.startswith('{') or line.startswith('}'):
                    continue
                elif line.startswith('"') and line.endswith(': {'):
                    current_store = line.split('"')[1]
                    data[current_store] = {}
                elif ':' in line:
                    product, sales = line.split(':')
                    product = product.strip().strip('"')
                    sales = int(sales.strip().strip(','))
                    data[current_store][product] = sales
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None
    except ValueError as e:
        print(f"Data processing error: {e}")
        return None

def set_data(file_path, total_sales):
    try:
        with open(file_path, 'w') as file:
            file.write('{\n')
            for i, (product, sales) in enumerate(total_sales.items()):
                file.write(f'    "{product}": {sales}')
                if i < len(total_sales) - 1:
                    file.write(',\n')
                else:
                    file.write('\n')
            file.write('}\n')

        print(f"The results have been successfully written to {file_path}")
    except IOError as e:
        print(f"File write error: {e}")

def sales_count(data):
    total_sales = {}
    for store, products in data.items():
        for product, sales in products.items():
            if product not in total_sales:
                total_sales[product] = 0
            total_sales[product] += sales
    return total_sales

set_data('output.txt', sales_count(get_data('input.txt')))