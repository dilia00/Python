from view import operator, numbers, print_res
from data_base import write_data, read_data, write_data_res
from funcs import do_it


def click():
    x = numbers()
    y = numbers()
    z = operator()
    write_data(x, y, z)
    res = do_it(read_data())
    write_data_res(res)
    print_res(res)
