.data
prompt: .asciiz "Enter a 5-digit number: "  # Prompt message
result: .asciiz "You entered: "             # Result message

.text

main:
    # Print a prompt asking the user to enter a 5-digit number
    li $v0, 4         # system call code for print_string
    la $a0, prompt    # address of prompt string
    syscall           # print the prompt

    # Read a string from the console
    li $v0, 8         # system call code for read_string
    la $a0, buffer    # address of input buffer
    li $a1, 10        # maximum number of characters to read (including newline)
    syscall           # read a string, result in $a0

    # Convert the input string to an integer
    li $v0, 4         # system call code for print_string
    la $a0, result    # address of result string
    syscall           # print the result string

    la $a0, buffer    # address of input buffer
    li $v0, 5         # system call code for parse_int
    syscall           # parse the integer, result in $v0

    # Check if the entered integer is a 5-digit number
    bge $v0, 10000, print_result  # If >= 10000, print the result
    j invalid_input             # Otherwise, it's not a 5-digit number

print_result:
    # Print the entered integer
    move $a0, $v0     # move the parsed integer to $a0
    li $v0, 1         # system call code for print_int
    syscall           # print the integer

    # Exit the program
    li $v0, 10        # system call code for exit
    syscall           # terminate program

invalid_input:
    # Print an error message for invalid input
    li $v0, 4         # system call code for print_string
    la $a0, invalid   # address of invalid input message
    syscall           # print the error message

    # Exit the program
    li $v0, 10        # system call code for exit
    syscall           # terminate program

# Data section for an input buffer and an error message
buffer: .space 12     # Reserve space for 12 characters (maximum input length)
invalid: .asciiz "Invalid input. Please enter a 5-digit number.\n"
