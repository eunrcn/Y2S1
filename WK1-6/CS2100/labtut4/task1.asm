.data
str: .asciiz "the answer = "
.text

main:
    # Read an integer from the console
    li   $v0, 5       # System call code for read_int
    syscall
    move $t0, $v0     # Move the integer value to temporary register $t0

    # Print "the answer = "
    li   $v0, 4       # System call code for print_string
    la   $a0, str     # Address of the string to print
    syscall

    # Print the integer value
    li   $v0, 1       # System call code for print_int
    move $a0, $t0     # Move the integer value to argument register $a0
    syscall

    # Exit the program
    li   $v0, 10      # System call code for exit
    syscall
