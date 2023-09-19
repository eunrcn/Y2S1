.data
prompt: .asciiz "Enter an integer: "  # Prompt message
result: .asciiz "the answer = "        # Result message

.text

main:
    # Print a prompt asking the user to enter an integer
    li $v0, 4         # system call code for print_string
    la $a0, prompt    # address of prompt string
    syscall           # print the prompt

    # Read an integer from the console
    li $v0, 5         # system call code for read_int
    syscall           # read an integer, result in $v0

    # Print the result message
    li $v0, 4         # system call code for print_string
    la $a0, result    # address of result string
    syscall           # print the result string

    # Print the entered integer
    li $v0, 1         # system call code for print_int
    move $a0, $v0     # move the input integer to $a0
    syscall           # print the integer

    # Exit the program
    li $v0, 10        # system call code for exit
    syscall           # terminate program