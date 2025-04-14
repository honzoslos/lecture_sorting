import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    slovnik = {}
    with open (file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {"series_1":[],"series_2":[],"series_3":[]}
        for row in reader:
            for key,value in row.items():
                data[key].append(int(value))
    return data

def selection_sort(list_of_number):
    # searched_number = float("inf")
    # lenght_of_list = len(list_of_number)
    # for idx_1 in range(lenght_of_list):
    #
    #     for idx_2,number in enumerate(list_of_number):
    #         if number <= searched_number:
    #             searched_number = number
    #             idx_20 = idx_2
    #         searched_number = float("inf")
    #     list_of_number[idx_1],list_of_number[idx_20] = list_of_number[idx_20],list_of_number[idx_1]
    n = len(list_of_number)
    for min_idx in range(n):
        j = min_idx
        for i in range(min_idx + 1,n):
            if list_of_number[min_idx] > list_of_number[i]:
                min_idx = i
    #prvni vec v materialech, hledani indexu nejmensiho cisla
        list_of_number[j],list_of_number[min_idx] = list_of_number[min_idx], list_of_number[j]
        print(list_of_number)
#skoro funguje :/
        return list_of_number


def bubble_sort(numbers):
    compare_number = float("-inf")
    for positon in range(len(numbers)):
        for number in numbers[0:numbers]:
            # if numbers[number] == numbers[-1]:
            #     break
            if numbers[number] >= numbers[number+1]:
                numbers[number], numbers[number+1] = numbers[number+1], numbers[number]
    return numbers

def insertion_sort(numbers):
    for number in numbers:
        if number == numbers[0]:
            continue
        if number < numbers[number -1]:
            pom_reg = number
            number[number] = numbers[number -1]
            numbers[number - 1] = pom_reg

            pocet = len(numbers[:number])
            while number != numbers[0]:
                if numbers[pocet] < numbers[pocet-1]:
                    pom_reg = numbers[pocet]
                    numbers[pocet] = numbers[pocet-1]
                    numbers[pocet-1] = pom_reg
                else:
                    break
        else:
            continue

    return numbers



def main():
    data = read_data("numbers.csv")
    print(data)
    list_of_nums = [15,12,8,32]
    print(insertion_sort(data["series_1"]))

    pass


if __name__ == '__main__':
    main()
