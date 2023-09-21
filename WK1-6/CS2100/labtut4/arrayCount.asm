# arrayCount.asm
  .data 
arrayA: .word 1, 2, 3, 4, 5, 6, 7, 8  # arrayA has 8 values
count:  .word 999             # dummy value

  .text
main:
    # code to setup the variable mappings
    la $t0, arrayA    
    addi $t1, $zero, 0  # i = 0
    addi $t2, $zero, 8  # Set len
    addi $t8, $zero, 0  # count = 0

    # code for reading in the user value X
    li $v0, 5          
    syscall            
    add $t6, $v0, $zero       # put X in $t6

    # Generate the mask 
    sub $t5, $t6, 1    

    # code for counting multiples of X in arrayA
     loop:
        bge $t1, $t2, printResult  # If i >= 5
        sll $t3, $t1, 2           # i*4
        add $t4, $t0, $t3         
        lw $t7, 0($t4)            
        and $t9, $t7, $t5        # $t9 = $t7 mod X
        bne $t9, $zero, skip
        addi $t8, $t8, 1  # result++

    skip:
        addi $t1, $t1, 1  # i++
        j loop

    # code for printing result
    printResult:
        sw $t8, count
        add $a0, $t8, $zero   
        li $v0, 1      
        syscall

    # code for terminating program
    li  $v0, 10
    syscall

