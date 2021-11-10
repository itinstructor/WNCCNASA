# Example of how to use a timer event
# to run a function at a predetermined interval

import pygame

pygame.init()
window = pygame.display.set_mode((200, 200))

# Create clock object
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)
counter = 10
text = font.render(str(counter), True, (0, 128, 0))

# Create timer event object
timer_event = pygame.USEREVENT+1

# Set the timer to fire the even every 1000 ms
# When the timer fires, it will appear on the event queue
# This is a non blocking call, the program continues until the timer fires
pygame.time.set_timer(timer_event, 1000)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Check event queue for the timer event
        elif event.type == timer_event:
            # Code to run here
            counter -= 1
            text = font.render(str(counter), True, (0, 128, 0))
            if counter == 0:
                # Stop timer event with a 0 parameter
                pygame.time.set_timer(timer_event, 0)

    window.fill((255, 255, 255))
    text_rect = text.get_rect(center=window.get_rect().center)
    window.blit(text, text_rect)
    pygame.display.flip()
