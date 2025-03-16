import pygame

pygame.init()

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Screen setup
screen_height = 700
screen_width = 700
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Homework Planner")

# Fonts
text_font = pygame.font.SysFont("Arial", 30)

# Function to draw text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Button class
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, self.rect, border_radius=10)
        draw_text(self.text, text_font, BLACK, self.rect.x + 10, self.rect.y + 10)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# Input field class
class InputBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = BLACK
        self.text = ""
        self.active = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        draw_text(self.text, text_font, BLACK, self.rect.x + 5, self.rect.y + 5)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.text = ""  # Clear text on enter
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

# Create button instances
start_button = Button(250, 300, 200, 50, "Start Planning")
back_button = Button(30, 640, 200, 50, "BACK")
plus_button = Button(140, 300, 50, 50, "+")

# Create input fields for new page
input_boxes = [InputBox(200, 200, 300, 40), InputBox(200, 260, 300, 40)]

# State control
home_page = True

run = True
while run:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if home_page:
            if start_button.is_clicked(event):
                home_page = False  # Switch to planner page
        else:
            for box in input_boxes:
                box.handle_event(event)
            if back_button.is_clicked(event):  # Press back button
                home_page = True  # Goes back to home page
            if plus_button.is_clicked(event):  # Press plus button
                input_boxes.append(InputBox(200, 320 + len(input_boxes) * 60, 300, 40))  # Add new input box

    if home_page:
        draw_text("Homework Planner", text_font, BLACK, 220, 150)
        start_button.draw(screen)
    else:
        draw_text("Enter your tasks:", text_font, BLACK, 140, 150)
        for box in input_boxes:
            box.draw(screen)
        back_button.draw(screen)
        plus_button.draw(screen)
    
    pygame.display.flip()

pygame.quit()
