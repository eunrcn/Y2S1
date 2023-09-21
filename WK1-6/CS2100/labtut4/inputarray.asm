# inputArrayCount.asm
  .data 
arrayA: .word 1, 2, 3, 4, 5, 6, 7, 8  # arrayA has 8 values
count:  .word 999                     # dummy value
abc: .word 123

  .text
main:
    # code to setup the variable mappings
    la $t0, arrayA    
    addi $t1, $zero, 0  # i = 0
    addi $t2, $zero, 8  # Set len
    addi $t8, $zero, 0  # count = 0

    # code for reading in the user value X
    read: 
        beq $t1, $t2, readX  # If 8 values are read, proceed to read X
        li $v0, 5          
        syscall  
        sw $v0, 0($t0)
        addi $t0, $t0, 4
        addi $t1, $t1, 1 
        add $t6, $v0, $zero          
        #move $t6, $v0      # put X in $t6
        j read
    
    readX:
        li $v0, 5 # Read X
        syscall
        add $t6, $v0, $zero 
        #move $t6, $v0
        sub $t5, $t6, 1 # mask  

    # Reset variables
    la $t0, arrayA    
    addi $t1, $zero, 0 # i =0
    addi $t8, $zero, 0 # count = 0

    # code for counting multiples of X in arrayA
     loop:
        bge $t1, $t2, printResult  # If i >= 5       
        lw $t7, 0($t0)            
        and $t9, $t7, $t5        # $t9 = $t7 mod X
        bne $t9, $zero, skip     
        addi $t8, $t8, 1  # result++

    skip:
        addi $t0, $t0, 4   
        addi $t1, $t1, 1  # i++
        j loop

    # code for printing result
    printResult:
        sw $t8, count
        add $a0, $t8, $zero
        #move $a0, $t8  
        li $v0, 1      
        syscall

    # code for terminating program
    li  $v0, 10
    syscall