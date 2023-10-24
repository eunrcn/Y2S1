from pentago import *

def test():
    
    # ***************** check_move ***************** #
    print()
    
    # check that you are not changing the input
    board_in = np.array([
        [0,0,0,0,0,0],
        [1,2,1,2,1,2],
        [2,1,2,1,2,1],
        [2,1,0,1,2,1],
        [1,2,1,2,1,2],
        [1,2,1,2,1,2]])
    board_out = board_in.copy()
    check_move(board_in, 0, 2)
    if ((board_in == board_out).all()): print("test check_move input - OK !")
    else: print("test check_move input - Problem: you are changing the input  !")
    
    # simple insertion possible empty
    board = np.zeros((6,6))
    if check_move(board, 3, 2): print("test check_move 1 - OK !")
    else: print("test check_move 1 - Problem in the check_move function output !")
    
    # simple insertion possible
    board = np.array([
        [1,2,1,2,1,2],
        [1,2,1,2,1,2],
        [2,1,2,1,2,1],
        [2,1,0,1,2,1],
        [1,2,1,2,1,2],
        [1,2,1,2,1,2]])
    if check_move(board, 3, 2): print("test check_move 2 - OK !")
    else: print("test check_move 2 - Problem in the check_move function output !")
    
    # simple insertion impossible turn 1 
    board = np.array([        
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]])
    if not check_move(board, 3, 2): print("test check_move 3 - OK !")
    else: print("test check_move 3 - Problem in the check_move function output !")
    
    # simple insertion impossible turn 2 
    board = np.array([      
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,2,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]])
    if not check_move(board, 3, 2): print("test check_move 4 - OK !")
    else: print("test check_move 4 - Problem in the check_move function output !")
    
   
    # ***************** apply_move ***************** #
    print()
    
    # check that you are not changing the input 
    board_in = np.array([     
        [0,0,0,1,2,1],
        [0,0,0,0,0,0],
        [0,0,0,2,1,2],
        [1,2,1,1,2,1],
        [0,0,0,0,0,0],
        [2,1,2,2,1,2]])
    board_out = board_in.copy()
    apply_move(board_in,1,1,1,7)
    apply_move(board_in,2,1,1,7)
    if ((board_in == board_out).all()): print("test apply_move input - OK !")
    else: print("test apply_move input - Problem: you are changing the input  !")

    # insert marble with rot on empty submatrix
    board_in = np.array([     
        [0,0,0,1,2,1],
        [0,0,0,0,0,0],
        [0,0,0,2,1,2],
        [1,2,1,1,2,1],
        [0,0,0,0,0,0],
        [2,1,2,2,1,2]])
    board_out = np.array([
        [0,0,0,1,2,1],
        [0,1,0,0,0,0],
        [0,0,0,2,1,2],
        [1,2,1,1,2,1],
        [0,0,0,0,0,0],
        [2,1,2,2,1,2]])
    board_tmp = apply_move(board_in,1,1,1,7)
    if ((board_tmp == board_out).all()): print("test apply_move 1 - OK !")
    else: print("test apply_move 1 - Problem in the apply_move function output  !")
    
    # insert marble with rot 
    board_in = np.array([     
        [0,2,1,2,1,2],
        [1,2,1,2,1,2],
        [2,1,2,1,2,1],
        [2,1,0,1,2,1],
        [1,2,1,2,1,2],
        [1,2,1,2,1,2]])
    board_out = np.array([
        [2,1,1,2,1,2],
        [1,2,2,2,1,2],
        [2,1,1,1,2,1],
        [2,1,0,1,2,1],
        [1,2,1,2,1,2],
        [1,2,1,2,1,2]])
    board_tmp = apply_move(board_in,1,0,0,7)
    if ((board_tmp == board_out).all()): print("test apply_move 2 - OK !")
    else: print("test apply_move 2 - Problem in the apply_move function output  !")
    
    
    
    # ***************** check_victory ***************** #
    print()
    
    # check that you are not changing the input 
    board_in = np.array([  
        [0,0,0,0,0,0],
        [0,1,0,0,1,2],
        [0,0,0,0,1,2],
        [0,0,2,0,1,0],
        [2,2,0,0,1,0],
        [0,0,0,0,1,0]])
    board_out = board_in.copy()
    check_victory(board_in, 1, 7)
    check_victory(board_in, 2, 7)
    if ((board_in == board_out).all()): print("test check_victory input - OK !")
    else: print("test check_victory input - Problem: you are changing the input  !")    
        
    # simple nowin
    board = np.array([ 
        [0,0,0,0,0,0],
        [0,1,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]])
    if check_victory(board, 1, 7)==0: print("test check_victory 1 - OK !")
    else: print("test check_victory 1 - Problem in the check_victory function output !")
    
    # win vertical
    board = np.array([  
        [0,0,0,0,0,0],
        [0,1,0,0,1,2],
        [0,0,0,0,1,2],
        [0,0,2,0,1,0],
        [2,2,0,0,1,0],
        [0,0,0,0,1,0]])
    if check_victory(board, 1, 7)==1: print("test check_victory 2 - OK !")
    else: print("test check_victory 2 - Problem in the check_victory function output !")
    
    # win 6-in-a-row
    board = np.array([  
        [0,0,0,0,1,0],
        [0,1,0,0,1,2],
        [0,0,0,0,1,2],
        [0,0,2,0,1,0],
        [2,2,0,0,1,0],
        [0,0,0,0,1,0]])
    if check_victory(board, 1, 1)==1: print("test check_victory 3 - OK !")
    else: print("test check_victory 3 - Problem in the check_victory function output !")
    
    # win 2nd player
    board = np.array([  
        [0,0,0,0,0,0],
        [0,1,0,0,2,1],
        [0,0,0,0,2,1],
        [0,0,1,0,2,0],
        [0,1,0,0,2,0],
        [0,0,0,0,2,0]])
    if check_victory(board, 1, 7)==2: print("test check_victory 4 - OK !")
    else: print("test check_victory 4 - Problem in the check_victory function output !") 

    # win horizontal
    board = np.array([  
        [0,0,0,0,0,0],
        [0,1,0,0,2,2],
        [0,0,0,0,0,2],
        [0,0,0,2,0,0],
        [0,2,0,0,0,0],
        [1,1,1,1,1,0]])
    if check_victory(board, 1, 7)==1: print("test check_victory 5 - OK !")
    else: print("test check_victory 5 - Problem in the check_victory function output !")
    
    # win diagonal
    board = np.array([   
        [0,0,0,0,0,0],
        [0,1,0,0,1,2],
        [0,0,0,0,2,1],
        [0,0,0,2,0,0],
        [0,1,2,0,0,0],
        [0,2,0,0,0,1]])
    if check_victory(board, 1, 7)==2: print("test check_victory 6 - OK !")
    else: print("test check_victory 6 - Problem in the check_victory function output !")
    
    
    # win vertical before rotation
    board = np.array([   
        [0,0,0,0,0,0],
        [0,1,0,1,1,0],
        [0,0,0,2,2,0],
        [0,0,2,0,1,0],
        [2,2,0,0,1,0],
        [0,0,0,0,1,0]])
    if check_victory(board, 1, 1)==1: print("test check_victory 7 - OK !")
    else: print("test check_victory 7 - Problem in the check_victory function output !")
    
    # draw full nowin
    board = np.array([   
        [2,1,2,1,2,1],
        [2,1,2,1,2,1],
        [1,2,1,2,1,2],
        [1,2,1,2,1,2],
        [2,1,2,1,2,1],
        [2,1,2,1,2,1]])
    if check_victory(board, 1, 8)==3: print("test check_victory 8 - OK !")
    else: print("test check_victory 8 - Problem in the check_victory function output !")
    
    
    
    # ***************** computer_move ***************** #
    print()
    
    # check that you are not changing the input
    board_in = np.array([ 
        [2,1,1,2,1,2],
        [1,2,2,2,1,2],
        [2,1,1,1,2,1],
        [2,1,0,1,2,1],
        [1,2,1,2,1,2],
        [1,2,1,2,1,2]])
    board_out = board_in.copy()
    computer_move(board_in, 1, 1)
    computer_move(board_in, 1, 2)
    computer_move(board_in, 2, 1)
    computer_move(board_in, 2, 2)
    if ((board_in == board_out).all()): print("test computer_move input - OK !")
    else: print("test computer_move input - Problem: you are changing the input  !")
      
    # random unique position choice
    board = np.array([ 
        [2,1,1,2,1,2],
        [1,2,2,2,1,2],
        [2,1,1,1,2,1],
        [2,1,0,1,2,1],
        [1,2,1,2,1,2],
        [1,2,1,2,1,2]])
    expected_output = [(3,2,1),(3,2,2),(3,2,3),(3,2,4),(3,2,5),(3,2,6),(3,2,7),(3,2,8)]
    output = computer_move(board, 1, 1)
    if tuple(output) in expected_output: print("test computer_move 1 - OK !")
    else: print("test computer_move 1 - Problem in the computer_move function output  !")
    
    # random multiple position choices
    board = np.array([ 
        [2,0,1,2,1,2],
        [1,2,2,2,1,0],
        [2,1,1,1,2,1],
        [2,1,0,1,2,1],
        [1,2,1,2,1,2],
        [1,0,1,2,1,2]])
    expected_output = [(3,2,1),(3,2,2),(3,2,3),(3,2,4),(3,2,5),(3,2,6),(3,2,7),(3,2,8),
     (0,1,1),(0,1,2),(0,1,3),(0,1,4),(0,1,5),(0,1,6),(0,1,7),(0,1,8),
     (1,5,1),(1,5,2),(1,5,3),(1,5,4),(1,5,5),(1,5,6),(1,5,7),(1,5,8),
     (5,1,1),(5,1,2),(5,1,3),(5,1,4),(5,1,5),(5,1,6),(5,1,7),(5,1,8)]
    output = computer_move(board, 1, 1)
    if tuple(output) in expected_output: print("test computer_move 2 - OK !")
    else: print("test computer_move 2 - Problem in the computer_move function output  !")
    
    # random unique position choice
    board = np.array([ 
        [2,1,1,2,1,2],
        [1,2,2,2,1,2],
        [2,1,1,1,2,1],
        [2,1,0,1,2,1],
        [1,2,1,2,1,2],
        [1,2,1,2,1,2]])
    expected_output = [(3,2,1),(3,2,2),(3,2,3),(3,2,4),(3,2,5),(3,2,6),(3,2,7),(3,2,8)]
    output = computer_move(board, 1, 2)
    if tuple(output) in expected_output: print("test computer_move 3 - OK !")
    else: print("test computer_move 3 - Problem in the computer_move function output  !")
    
    # random multiple position choices
    board = np.array([ 
        [2,0,1,2,1,2],
        [1,2,2,2,1,0],
        [2,1,1,1,2,1],
        [2,1,0,1,2,1],
        [1,2,1,2,1,2],
        [1,0,1,2,1,2]])
    expected_output = [(3,2,1),(3,2,2),(3,2,3),(3,2,4),(3,2,5),(3,2,6),(3,2,7),(3,2,8),
     (0,1,1),(0,1,2),(0,1,3),(0,1,4),(0,1,5),(0,1,6),(0,1,7),(0,1,8),
     (1,5,1),(1,5,2),(1,5,3),(1,5,4),(1,5,5),(1,5,6),(1,5,7),(1,5,8),
     (5,1,1),(5,1,2),(5,1,3),(5,1,4),(5,1,5),(5,1,6),(5,1,7),(5,1,8)]
    output = computer_move(board, 1, 2)
    if tuple(output) in expected_output: print("test computer_move 4 - OK !")
    else: print("test computer_move 4 - Problem in the computer_move function output  !")
    
    # smart win unique position choice after rot
    board = np.array([ 
        [2,1,2,0,1,2],
        [2,1,2,0,0,1],
        [1,2,1,1,2,1],
        [1,2,1,0,1,0],
        [2,1,2,1,1,2],
        [2,1,2,2,1,2]])
    expected_output = [(1,4,1)]
    output = computer_move(board, 1, 2)
    if tuple(output) in expected_output: print("test computer_move 5 - OK !")
    else: print("test computer_move 5 - Problem in the computer_move function output  !")
  
   
test()