import pygame
import random
import time

pygame.init()

screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# player = pygame.Rect((300, 250, 50, 50))

def create_card_object(x, y, width, height, text, card_color, center_pile):
    # Create a pygame.Rect for the card's rectangle
    card_rect = pygame.Rect(x, y, width, height)
    
    # Create a font and render the text
    font = pygame.font.Font(None, 15)  # You can choose a different font and size
    text_surface = font.render(text, True, (255, 255, 255))  # white font color
    text_rect = text_surface.get_rect()
    text_rect.center = card_rect.center  # Center the text on the card
    
    # Fill the card with a background color (white in this case)
    if card_color == "green":
        color = (50, 168, 105)
    elif card_color == "purple":
        color = (143, 50, 168)
    elif card_color == "brown":
        color = (168, 94, 50)
    elif card_color == "blue":
        color = (50, 162, 168)
    else:
        color = (255, 255, 255)
        text_surface = font.render(text, True, (0, 0, 0))  # black font color

    pygame.draw.rect(screen, color, card_rect)
    
    if text == "Ada Lovelace":
        image = pygame.image.load('ada_lovelace.png')
        # resized_image = pygame.transform.scale(image, (79, 130))
    elif text == "Adele Goldberg":
        image = pygame.image.load('adele_goldberg.jpeg')
        # resized_image = pygame.transform.scale(image, (79, 130))
    elif text == "Barba Liskov":
        image = pygame.image.load('barbara_liskov.png')
        # resized_image = pygame.transform.scale(image, (79, 130))
    elif text == "Donna Strickland":
        image = pygame.image.load('donna_strickland.png')
        # resized_image = pygame.transform.scale(image, (79, 130))
    elif text == "Frances Allen":
        image = pygame.image.load('frances_allen.jpeg')
        # resized_image = pygame.transform.scale(image, (79, 130))
    elif text == "Grace Hopper":
        image = pygame.image.load('grace_hopper.png')
        # resized_image = pygame.transform.scale(image, (79, 130))
    elif text == "Jean Sammet":
        image = pygame.image.load('jean_sammet.png')
        # resized_image = pygame.transform.scale(image, (79, 130))
    elif text == "Joan Clarke":
        image = pygame.image.load('joan_clarke.jpeg')
        # resized_image = pygame.transform.scale(image, (79, 130))
    elif text == "Radia Perlman":
        image = pygame.image.load('radia_perlman.png')
        # resized_image = pygame.transform.scale(image, (79, 130))
    elif text == "Shafi Goldwasser":
        image = pygame.image.load('shafi_goldwasser.png')
        # resized_image = pygame.transform.scale(image, (79, 130))
    elif text == "skip":
        image = pygame.image.load('skip.jpg')
        # print("SKIP")
        # resized_image = pygame.transform.scale(image, (79, 130))
    elif text == "reverse":
        image = pygame.image.load('reverse.jpg')
        # resized_image = pygame.transform.scale(image, (79, 130))
    elif text == "wild":
        image = pygame.image.load('wild.png')
        # resized_image = pygame.transform.scale(image, (79, 130))
    else:
        print(text)
        image = pygame.image.load('tbd.jpg')
        resized_image = pygame.transform.scale(image, (75, 50))

    if center_pile == False:
        resized_image = pygame.transform.scale(image, (79, 130))
    else:
        resized_image = pygame.transform.scale(image, (130, 205))
    image_surface = pygame.Surface(resized_image.get_size())
    image_surface.blit(resized_image, (0, 0))

    # Draw the text on the card
    # screen.blit(text_surface, text_rect)
    screen.blit(image_surface, (card_rect.x + 10, card_rect.y + 10))


    
    # Return the card's rectangle
    return card_rect


women_in_stem = ["Ada Lovelace", "Grace Hopper", "Jean Sammet", "Adele Goldberg", "Barba Liskov", "Radia Perlman", "Frances Allen", "Shafi Goldwasser", "Donna Strickland", "Joan Clarke"]
colors = ["green", "purple", "brown", "blue"]
operations = ["reverse", "skip"]

cards = []
for color in colors:
    for woman in women_in_stem:
        card = (woman, color)
        cards.append(card)
        cards.append(card)
    for operation in operations:
        card = (operation, color)
        cards.append(card)
        cards.append(card)
for i in range(4):
    cards.append(("wild", "white"))

random.shuffle(cards)

player = [cards.pop(), cards.pop(), cards.pop(), cards.pop(), cards.pop()]
computer = [cards.pop(), cards.pop(), cards.pop(), cards.pop(), cards.pop()]

play_stack = [cards.pop()]

def find_card(x, y):
    if y >= 420 and y <= 570:
        if x >= 30 and x <= 130:
            return 1
        if x >= 160 and x <= 260:
            return 2
        if x >= 290 and x <= 390:
            return 3
        if x >= 420 and x <= 520:
            return 4
        if x >= 550 and x <= 650:
            return 5
        if x >= 680 and x <= 780:
            return 6
        if x >= 710 and x <= 810:
            return 7
        if x >= 840 and x <= 940:
            return 8
        if x >= 970 and x <= 1070:
            return 9
    return -1

def valid_play(top_card, played_card):
    if top_card[0] == 'wild':
        return True
    if(top_card[1] == played_card[1]) or top_card[0]==played_card[0] or played_card[0] == "wild" or played_card[0] == "wild +4":
        return True
    return False

# Rectangle dimensions-
rectangle_width = 100
rectangle_height = 150

# Number of rectangles
num_rectangles = 9  # You can change this to the desired number

# Calculate horizontal spacing between rectangles
spacing = (screen_width - (rectangle_width * num_rectangles)) / (num_rectangles + 1)
print(spacing)

run = True
start = False
while run == True and start == False:
    screen.fill((0, 0, 0))
    message = "Here are the instructions! Press enter to begin!"
    font = pygame.font.Font (None, 36)
    text = font.render(message, True, (255, 255, 255))  # (R, G, B) for white
    screen.blit(text, (350, 50))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start = True
                your_turn = True
                tries = 0
                break
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
                
while run == True and start == True:
    # Starting position for the first rectangle
    x = 30
    y = 420
    stop_display_cards = False
    first_draw = True
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and your_turn:  # Left mouse button clicked
                print("MOUSE CLICKED")
                clicked_x, clicked_y = event.pos
                selected_index = find_card(clicked_x, clicked_y)
                if selected_index != -1:
                    # print("Card selected at index:", selected_index)
                    card = player[selected_index - 1]
                    if valid_play(play_stack[-1], card):
                        play_stack.append(card)
                        player.pop(selected_index - 1)
                        create_card_object(600, 130, rectangle_width * 1.5, rectangle_height * 1.5, play_stack[-1][0], play_stack[-1][1], True)
                        pygame.display.update()

                        if len(player) == 0:
                            message = "Yay you won!"
                            font = pygame.font.Font(None, 36)
                            text = font.render(message, True, (255, 255, 255))  # (R, G, B) for white
                            screen.blit(text, (300, 380))
                            pygame.display.update()
                            time.sleep(10)
                            run = False

                        your_turn = False
                        if (play_stack [-1][0] == "reverse") or play_stack[-1][0] == 'skip':
                            your_turn = True
        if event.type == pygame.KEYDOWN and your_turn:
            if event.key == pygame.K_d:
                if len(player) < 9:
                    draw_card = cards.pop()
                    player.append(draw_card)
                    screen.fill((0, 0, 0))
                    create_card_object(600, 130, rectangle_width * 1.5, rectangle_height * 1.5, play_stack[-1][0], play_stack[-1][1], True)
                    x = 30
                    for i in range(len(player)):
                        p = player[i]
                        # if i == len(player) - 1:
                        create_card_object(x, y, rectangle_width, rectangle_height, p[0], p[1], False)
                        x += rectangle_width + spacing
                        if i == len(player) - 1:
                            stop_display_cards = True

                    pygame.display.update()
                    first_draw = False
                    # time.sleep(2)
                

                else:
                    tries += 1
                if tries == 2:
                    new_card = cards.pop()
                    play_stack.append(new_card)
                    tries = 0
                your_turn = False

        
    if your_turn:
        message = "It's your turn to play!"
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, (255, 255, 255))  # (R, G, B) for white
        screen.blit(text, (550, 50))

    else:
        message = "The computer is playing now!"
        font = pygame.font.Font (None, 36)
        text = font.render(message, True, (255, 255, 255))  # (R, G, B) for white
        screen.blit(text, (550, 50))

        # screen.fill((0, 0, 0))
        # create_card_object(600, 130, rectangle_width * 1.5, rectangle_height * 1.5, play_stack[-1][0], play_stack[-1][1], True)
        x = 30
        for i in range(len(player)):
            p = player[i]
            create_card_object(x, y, rectangle_width, rectangle_height, p[0], p[1], False)
            x += rectangle_width + spacing
            if i == len(player) - 1:
                stop_display_cards = True

        pygame.display.update()
        time.sleep(1)
        first_draw = False

        valid = False
        for i in range(len(computer)):
            card = computer[i]
            if valid_play(play_stack[-1], card):
                play_stack.append(card)
                computer.pop(i)
                valid = True
                break
        if valid == False:
            if len(computer) < 9:
                draw_card = cards.pop()
                computer.append(draw_card)
            else:
                tries += 1
            if tries == 2:
                new_card = cards.pop()
                play_stack.append(new_card)
                tries = 0
            # your_turn = False

        your_turn = True

    if first_draw:
        create_card_object(600, 130, rectangle_width * 1.5, rectangle_height * 1.5, play_stack[-1][0], play_stack[-1][1], True)

        for i in range(len(player)):
            p = player[i]
            create_card_object(x, y, rectangle_width, rectangle_height, p[0], p[1], False)
            x += rectangle_width + spacing
            if i == len(player) - 1:
                stop_display_cards = True

    if len(cards) == 0:
        cards = play_stack[0:len(play_stack) - 2]
        random.shuffle(cards)

    if len(player) == 0:
        message = "Yay you won!"
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, (255, 255, 255))  # (R, G, B) for white
        screen.blit(text, (300, 380))

    if len(computer) == 0:
        message = "Aww No! The Computer Won!"
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, (255, 255, 255))  # (R, G, B) for white
        screen.blit(text, (300, 380))

    message = "The computer has: " + str(len(computer)) + " cards"
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, (255, 255, 255))  # (R, G, B) for white
    screen.blit(text, (20, 30))

    pygame.display.update()

pygame.quit()