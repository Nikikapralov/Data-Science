import csv


def order_and_sort_the_additional_data(additional_data_path):
    to_sort = []
    with open(additional_data_path, 'r') as additional_data:
        csv_reader = csv.DictReader(additional_data)
        for row in csv_reader:
            to_sort.append(row)
    data_sorted = sorted(to_sort, key=lambda x: (x['location'], x['date']))
    return data_sorted


def write_to_new_file(updated_data_path, row, is_first):
    with open(updated_data_path, 'a', newline='') as file:
        header = ['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases']
        writer = csv.DictWriter(file, header)
        if is_first:
            writer.writeheader()
            writer.writerow(row)
        else:
            writer.writerow(row)


def update_case_numbers(original_data_path, additional_data_path, updated_data_path):
    sorted_additional_data = order_and_sort_the_additional_data(additional_data_path)
    is_first = True
    with open(original_data_path, 'r') as data:
        csv_reader = csv.DictReader(data)
        first_iteration = True
        current_total_cases = 0
        start = 0
        for row in csv_reader:
            current_country = row['iso_code']
            if first_iteration:
                previous_country = current_country
                first_iteration = False
            if previous_country != current_country:
                current_total_cases = 0
            try:
                for row_update_index in range(start, start + 1):
                    if sorted_additional_data[row_update_index]['iso_code'] == row['iso_code']:
                        if sorted_additional_data[row_update_index]['date'] == row['date']:
                            new_cases_to_add = float(sorted_additional_data[row_update_index]['new_cases'])
                            row['new_cases'] = float(row['new_cases']) + new_cases_to_add
                            current_total_cases += new_cases_to_add
                            start = row_update_index + 1
            except IndexError:
                pass
            row['total_cases'] = float(row['total_cases']) + current_total_cases
            write_to_new_file(updated_data_path, row, is_first)
            is_first = False
            previous_country = current_country


original_data_path = r''
additional_data_path = r''
updated_data_path = r''
update_case_numbers(original_data_path, additional_data_path, updated_data_path)
