def move_snake(board , direction = "right"):
	
	new_board = copy.deepcopy(board)
	
	for index , i in enumerate(board):
		for cell_index , j in enumerate(i):
			
			if j is not None:
				if board[index][cell_index].lower() == "sh":
					if direction.lower().startswith("l"): # left
						new_board[index][cell_index -1] = "SH"			 
					elif direction.lower().startswith("t"): # top
						new_board[index -1][cell_index] = "SH"			 
					elif direction.lower().startswith("b"): # bottom
						new_board[index +1][cell_index] = "SH"			 
					else: #right
						new_board[index][cell_index +1] = "SH"	
					new_board[index][cell_index] = "S"
						 
				elif board[index][cell_index].lower() == "st":
					if  board[index +1][cell_index] is not None and board[index +1][cell_index].lower() == "s":
						
						new_board[index +1][cell_index] = "st"
						
					elif  board[index - 1][cell_index] is not None and board[index - 1 ][cell_index].lower() == "s":
						
						new_board[index -1][cell_index] = "st"
						
					elif  board[index][cell_index - 1] is not None and board[index] [cell_index -1].lower() == "s":
						new_board[index][cell_index -1] = "st"
						
					elif  board[index][cell_index + 1] is not None and board[index] [cell_index +1].lower() == "s":
						
						new_board[index] [cell_index +1] = "st"
						
					new_board[index][cell_index] = None

	return new_board