"""Dictionary related utility functions."""

__author__ = "730400691"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is in the second parameter."""
    result: list[str] = []

    for row in table:
        column_value: str = row[column_name]
        result.append(column_value)

    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into one represented as a dictionary of columns."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = table[0]
    for column_name in first_row:
        result[column_name] = column_values(table, column_name)

    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column based table with only the first n rows of data for each column."""
    result: dict[str, list[str]] = {}

    for column in column_table:
        if n >= len(column_table[column]):
            return column_table
        number_of_entries: int = 0
        column_list: list[str] = []
        while number_of_entries < n:
            column_list.append(column_table[column][number_of_entries])
            number_of_entries += 1
        
        result[column] = column_list  

    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for name in column_names:
        column_list: list[str] = []
        if name in column_table: 
            for item in column_table[name]:
                column_list.append(item)
        result[name] = column_list

    return result 


def concat(column_table_one: dict[str, list[str]], column_table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}

    for column_one in column_table_one:
        column_list_one: list[str] = []
        for item_one in column_table_one[column_one]:
            column_list_one.append(item_one)
        result[column_one] = column_list_one

    for column_two in column_table_two:
        column_list_two: list[str] = []
        for item_two in column_table_two[column_two]:
            column_list_two.append(item_two)
        if column_two in result:
            result[column_two] += column_list_two
        else:
            result[column_two] = column_list_two

    return result 


def count(values: list[str]) -> dict[str, int]:
    """Given a list, will produce a dictionary where aech key is a unique value in the given list and each value is the count of how many times that appears."""
    result: dict[str, int] = {}

    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


def filtering(starting: dict[str, list[str]], qz: str, lower_c1: int, upper_c1: int, un: str, lower_c2: int, upper_c2: int) -> dict[str, list[str]]:
    """Produces a new dictionary that only contains values that meet certain criteria for each column involved."""
    result: dict[str, list[str]] = {}

    column_list_qz: list[str] = []
    column_list_un: list[str] = []
    total: int = len(starting[qz])
    i: int = 0
    while i < total:
        item_qz: str = starting[qz][i]
        item_qz_int: int = int(item_qz, 10)

        item_un: str = starting[un][i]
        item_un_int: int = int(item_un, 10)

        if item_qz_int >= lower_c1 and item_qz_int <= upper_c1:
            column_list_qz.append(item_qz)
            if item_un_int >= lower_c2 and item_un_int <= upper_c2:
                column_list_un.append(item_un)
            else: 
                column_list_qz.pop(len(column_list_qz) - 1)
        i += 1
    result[qz] = column_list_qz
    result[un] = column_list_un

    return result


def total(counted: dict[str, int]) -> int:
    """Totals up the integers obtained in the count function."""
    totaled: int = 0
    for column in counted:
        totaled += counted[column]
    
    return totaled 
