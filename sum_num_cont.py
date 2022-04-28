#!/usr/bin/env python3
# Created by Marc Coffi
# Created in April 2022
# This program calculate the sum how numbers based on user's choice


def main():
    while True:
        # Declaring variables
        counter = 0
        total_sum_list = []

        # Ask user how much number they want to add up
        user_input = input("How many numbers would you like to enter?: ")

        try:
            # Casting to int
            user_input_as_int = int(user_input)
            # Check if the input is a positive number
            if user_input_as_int <= 0:
                print(
                    "Invalid number. You cannot input a negative number.\nPlease input a positive number."
                )
                break

        except:
            # If the user enters a invalid input
            print("Invalid number. Please input a positive number.")
            break

        while counter < user_input_as_int:

            # Ask user to input their number
            user_num = input("Enter a number: ")

            try:
                # Casting to int
                user_num_as_int = int(user_num)

                # Check if the input is a positive number
                if user_num_as_int <= 0:
                    print(
                        "Invalid number. You cannot input a negative number.\nPlease input a positive number."
                    )
                    continue

                # Add number to list
                total_sum_list.append(user_num_as_int)

                # Add the user number to the total sum
                # total_sum += user_num_as_int
                counter += 1

            except:
                # If the user enters a invalid input
                print("Invalid number. Please input a positive number.")

        total_sum = sum(total_sum_list)

        # Display total sum
        print(*total_sum_list, sep=" + ", end=" ")
        print("= {}".format(total_sum))
        print("The total sum of the numbers is {}.".format(total_sum))
        break


if __name__ == "__main__":
    main()
