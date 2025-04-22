import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker")

# Colors
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

# Game variables
cookies = 0
font = pygame.font.SysFont('Arial', 32)

def draw_cookie(x, y, radius):
    pygame.draw.circle(screen, BROWN, (x, y), radius)
    pygame.draw.circle(screen, BLACK, (x, y), radius, 2)
    # Cookie details
    pygame.draw.circle(screen, BLACK, (x-20, y-10), 5)
    pygame.draw.circle(screen, BLACK, (x+20, y-15), 5)
    pygame.draw.circle(screen, BLACK, (x+15, y+20), 5)
    pygame.draw.circle(screen, BLACK, (x-15, y+15), 5)

def main():
    global cookies
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check if click is on cookie (center at 200, 200, radius 100)
                if ((mouse_x - 200)**2 + (mouse_y - 200)**2) <= 100**2:
                    cookies += 1
        
        # Drawing
        screen.fill(WHITE)
        draw_cookie(200, 200, 100)
        
        # Display cookie count
        text = font.render(f"Cookies: {cookies}", True, BLACK)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, 400))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
