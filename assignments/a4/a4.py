"""
COMP1117A Assignment 4
Author: Cheng Ho Ming, Eric
"""
# For Python 3.7/3.8 compatibility
# Support type hints with subscript, e.g. list[str]
from __future__ import annotations

"""
Data structure for global_booking_list:
List of [<name>, <8-length telephone number>, <DD-MM-YYYY>, <number of seats>, <ticket code>]
Data structure for global_table_allocated:
List of [<DD-MM-YYYY>, <ticket code>, <table number>]
"""


def _load_files(filename: str) -> tuple[list, int]:
    """
    This function takes a filename and loads the file (.txt in this question)
    and returns a tuple of list and int. The list contains all the lines in the
    file and the integer are the number of lines in the file.
    """
    with open(filename) as file:
        data = file.read().splitlines()
    return data, len(data)


def load_files(filename: str) -> list:
    """
    A wrapper of _load_files function. This function additionally prints
    a line "Imported n table(s)." where n is the number of tables in the file.
    """
    temp = _load_files(filename)
    print(f"Imported {temp[1]} table(s).")
    return temp[0]


def _check_booking(date: str, global_booking_list: list) -> int:
    """
    This function takes a date and a global booking list and returns the
    number of bookings on that day.
    """
    # We can use list comprehension (PEP 202) to filter out the bookings that are not
    # on the date we want. Then we can use len() to count the number of bookings.
    return len([x for x in global_booking_list if x[2] == date])


def _request_booking(global_booking_list: list, *booking: str) -> [str, int]:
    """
    This function takes a booking and a global booking list and returns
    the date and a number indicating the ticket code of the booking.
    Currently, there are no code dealing with unsuccessful booking attempts.

    Format of the booking variable:
    <name>, <8-length telephone number>, <DD-MM-YYYY>, <number of seats>
    """
    # As mentioned, ticket codes for each day are unique. So we need to check
    # how many bookings are there for the day.
    num_of_bookings_in_day = _check_booking(booking[2], global_booking_list)
    # Ticket codes starts from 1, and initially _check_booking returns 0.
    num_of_bookings_in_day += 1
    global_booking_list.append([booking[0],
                                booking[1],
                                booking[2],
                                booking[3],
                                # We need to convert the number of bookings to string
                                # so that we can use it as ticket_code: str.
                                # Do not remove. Will break _ticket_allocated_for function.
                                # As the function compares x[1] == ticket_code,
                                # both x[1] and ticket_code must be string. Otherwise, the comparison
                                # will always be False.
                                # Faulty case: '1' == 1 -> False
                                str(num_of_bookings_in_day)
                                ]
                               )
    # return the date and the ticket code
    return booking[2], num_of_bookings_in_day


def request_booking(global_booking_list: list[str], *booking: str) -> None:
    """
    A wrapper of _request_booking function. This function additionally prints
    a line "Added booking. The ticket code for <date> is <ticket code>".
    """
    temp = _request_booking(global_booking_list, *booking)
    print(f"Added booking. The ticket code for {temp[0]} is {temp[1]}.")


def list_bookings(global_booking_list, global_table_allocated: list) -> None:
    """
    A wrapper of _list_bookings function. This function additionally prints the
    following text:
    Booking(s):
    <name>, <8-length telephone number>, <DD-MM-YYYY> (Ticket <ticket code>), <number of seats>
    , Allocated table: <allocated table>

    If there are no booking, it prints "No booking." instead.
    """
    temp = global_booking_list
    if len(temp) == 0:
        print("No booking.")
    else:
        print("Booking(s):")
        for x in temp:
            print(f"{x[0]}, {x[1]}, {x[2]} (Ticket {x[4]}), {x[3]}, "
                  f"Allocated table: {_table_allocated_for(x[2], x[4], global_table_allocated)}.")


def _table_allocated_for(date, ticket_code: str, global_table_allocated: list) -> int | None:
    """
    This function takes a date, ticket_code to check whether a booking has table allocated.
    If the booking has no table allocated, it returns None.
    """
    # We can use list comprehension (PEP 202) to filter out the bookings that are not
    # on the date we want.
    table_allocated = [x for x in global_table_allocated if x[0] == date and x[1] == ticket_code]
    if len(table_allocated) == 0:
        return None
    else:
        return table_allocated[0][2]


def _table_exists(table_number: str, table_file_list: list) -> bool:
    """
    This function takes a table number and a table file list and returns
    whether the table exists in the table file list.
    """
    return table_number in table_file_list


def _allocate_table(global_table_allocated: list, table_file_list: list,
                    date: str,
                    ticket_code: str,
                    table_number: str, ) -> int:
    """
    This function takes a date, a ticket code, and a table number and adds the
    table number to the global table allocated list.
    It returns 0 for successful allocation
    returns 1 for bookings that already have table allocated
    returns 2 for table not found
    """
    if _table_exists(table_number, table_file_list):
        if _table_allocated_for(date, ticket_code, global_table_allocated) is None:
            global_table_allocated.append([date, ticket_code, table_number])
            return 0
        else:
            return 1

    else:
        return 2


def allocate_table(global_table_allocated: list, table_file_list: list,
                   date: str,
                   ticket_code: str,
                   table_number: str) -> None:
    """
    A wrapper of _allocate_table function. This function additionally prints
    a line "Allocated table <table_number> to <date> (Ticket <ticket_code>)."
    """
    table_allocate_status = _allocate_table(global_table_allocated, table_file_list, date, ticket_code, table_number)
    if table_allocate_status == 0:
        print(f"Allocated table {table_number} to {date} (Ticket {ticket_code}).")
    if table_allocate_status == 1:
        print("Error: This booking has table allocated already.")
    if table_allocate_status == 2:
        print("Error: Table not found.")


def main() -> None:
    """
    Procedure of the main program:
     1. Load table file
     2. Wait for user commands:
         a. Book
             Example input:
                 Book|CK Lai|91234567|01-11-2023|10
         b. ListBookings
         c. AllocateTable
             Example input:
                 AllocateTable|01-11-2023|1|04
         d. Exit
    """
    # Initialize global_booking_list and global_table_allocated
    booking_list = []
    table_allocated = []
    command = input("Table file:\n")
    table_file = load_files(command)
    while True:
        command = input().split("|")
        # command[1:] returns tuple, so we need to unpack it using *.
        if command[0] == "Book":
            request_booking(booking_list, *command[1:])
        if command[0] == "ListBookings":
            list_bookings(booking_list, table_allocated)
        if command[0] == "AllocateTable":
            allocate_table(table_allocated, table_file, *command[1:])
        if command[0] == "Exit":
            print("Bye")
            break
        # For debugging purposes.
        # print(booking_list, table_allocated)


if __name__ == "__main__":
    main()
