import urllib.request
import io
import pygame
import copy
import random

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

BLACK = (0, 0 ,0)

def load_emoji_image(url, size=(40 , 40)):
    try:
        # User-Agent header lagana zaroori hai taaki GitHub block na kare
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            image_data = response.read()
        opened_image = io.BytesIO(image_data)
        surface = pygame.image.load(opened_image).convert_alpha()
        return pygame.transform.scale(surface, size)
        
    except Exception as e:
        print(f"Error loading image: {e}") # Isse terminal me error pata chal jayega
        surface = pygame.Surface(size)
        surface.fill((255, 0, 255)) 
        return surface

APPLE_IMG = load_emoji_image(
    "https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/1f34e.png"
)  # 🍎



def draw_board(board):
	
	for row , i in enumerate(board):
		for col , j in enumerate(i):
			if j is not None:
					
				if j.lower().startswith("s"):
					pygame.draw.rect(screen , (0 ,255 , 0) , (col * 40 , row *40 , 40 , 40))	
					
				elif j.lower() == "f":
					screen.blit(APPLE_IMG, (col * 40 , row * 40))
					
	pygame.draw.rect(screen, (255, 255, 255), (0 , 0, 25 * 40 , 25 * 40), 5)
	#pygame.display.flip()

	

def move_snake(board , direction = "right"):
	
	direc = direction.lower()[0]
	nxt = copy.deepcopy(board)
	growth = False
	
	head_row , head_col = None , None
	Tail_row , Tail_col = None , None
	
	for row , i in enumerate(board):
		for col , j in enumerate(i):		
			
			if j is not None:			
				if board[row][col].lower() == "sh":
					head_row , head_col  = row , col
				if board[row][col].lower() == "st":
					Tail_row , Tail_col  = row , col
	
	if direc == "l":
		nxt_row , nxt_col = head_row , head_col -1
		
	elif direc == "t":
		nxt_row , nxt_col = head_row -1 , head_col
		
	elif direc == "b":
		nxt_row , nxt_col = head_row + 1 , head_col 
		
	else:
		nxt_row , nxt_col = head_row , head_col  +1
	
	if 0 <= nxt_row < 25 and 0 <= nxt_col < 25:
		if board[nxt_row][nxt_col] is not None and board[nxt_row][nxt_col].lower() == "f":
			growth = True
		
	else:
		return board
		
	nxt[nxt_row][nxt_col] = "sh"
	nxt[head_row][head_col] = "s"
	
	
	if growth:
		while True:
			r = random.randint(0 , 24)
			cl = random.randint(0,24)
							
			if nxt[r][cl] is None:	
				nxt[r][cl] = "f"
				break
	else:
		nxt[Tail_row][Tail_col] = None
		
		possibilites = [[Tail_row ,Tail_col -1] , [Tail_row, Tail_col+1] , [Tail_row -1 , Tail_col] , [Tail_row +1 , Tail_col]]
		
		for i in possibilites:
			k , v= i[0] , i[1]
			
			if 0 <= k < 25 and 0 <= v < 25:
				if nxt[k][v] is not None and nxt[k][v].lower()[0] == "s":
					nxt[k][v] = "st"
					break
	return nxt
	
def check_collision(board , direction = "right"):
	direc = direction.lower()[0]
	
	for row , i in enumerate(board):
		for col , j in enumerate(i):		
		
			if j is not None:			
				if board[row][col].lower() == "sh":	
					if direc == "l":
						if col - 1 < 0:
							return None
							
						left = board[row][col -1]
						if left is not None and left.lower()[0] == "s":
							return None

							
					elif direc == "t":
						if row - 1 < 0:
							return None
							
						top = board[row -1][col]		
						if top is not None and top.lower()[0] == "s":
							return None
													
					elif direc == "b":
						try :
							bottom = board[row + 1][col]					
							if bottom is not None and bottom.lower()[0] == "s":
								return None
								
						except IndexError:
							return None
								
					else:
						try:
							right = board[row][col +1]
							if right is not None and right.lower()[0] == "s":
								return None
								
						except IndexError:
							return None	
	return True						

start_x = 0
start_y = 0
				
def get_swipe_direction(event , last_direction = "right"):
	
	global start_x , start_y
	
	if event.type == pygame.FINGERDOWN:
		start_x = event.x * 1000
		start_y = event.y * 1000

	if event.type == pygame.FINGERUP:
		x2 = event.x * 1000
		y2 = event.y * 1000
	
		dx = (start_x - x2)
		dy = (start_y - y2) 
		
		if abs(dx) >= 40 or abs(dy) >= 40:
			if abs(dx) > abs(dy):
				if dx > 0:
					new_direction = "Left"
				else:
					new_direction = "right"
			else:
				if dy > 0:
					new_direction = "top"
				else:
					new_direction = "bottom"
			return new_direction
			
		else:
			return last_direction			
	return last_direction
	
board = [ [None for i in range(25)] for _ in range (25)]
board[0][0] = "St"
board[0][1] = "Sh"
board[7][8] = "f"

direction = "right"

old_score = None
speed = 3
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False			
	
		direction = get_swipe_direction(event , direction)
		
	
	if check_collision(board , direction) is None :
		running = False
		
	board = move_snake(board , direction)

	
	screen.fill(BLACK)
	score = 0
	for i in board:
		for j in i:
			if j is not None and j.lower() == "s":
				score += 1
		
	if old_score is None:
		old_score = score
			
	if not running:

		font = pygame.font.Font(None, 80)
		text = font.render(f"Score -> {score}" , True, (255, 255, 255))
		screen.blit(text, (10, 10))

		
	draw_board(board)
	pygame.display.flip()
	
	if old_score < score and speed < 20:
		if speed > 10:
			speed += 0.25
		else:
			speed += 0.5
		old_score = score
	pygame.time.Clock().tick(speed)
	
pygame.quit()

