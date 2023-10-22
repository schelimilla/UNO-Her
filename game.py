import pygame
import random
import time

pygame.init()

screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

popup_screen_width = 400
popup_screen_height = 200
popup_screen = None
popup_open = False


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
women_in_stem_facts = {
    "Ada Lovelace": ["Ada Lovelace, born in 1815, is often recognized as the world's", "first computer programmer. She collaborated with Charles Babbage", "on his Analytical Engine and wrote detailed notes and algorithms", "for the machine, including an algorithm for calculating", "Bernoulli numbers. Her work laid the foundation for modern computer", "programming and computational thinking."],
    "Grace Hopper": ["Grace Hopper, born in 1906, was a pioneering American computer", "scientist and one of the first programmers of the Harvard Mark I computer", "during World War II. She played a significant role in the development", "of early programming languages and is often credited with", "coining the term \"debugging\" after removing a moth from", "a computer relay. Her work laid the foundation for", "modern computer programming, and she remains an", "iconic figure in the field of computer science."],
    "Jean Sammet": ["Jean Sammet was a pioneering American computer scientist known for", "her significant contributions to the development of the programming", "language COBOL (Common Business-Oriented Language) in the late 1950s. She played", "a crucial role in the design and development of COBOL, which became", "one of the first high-level programming languages to target", "business data processing. Sammet's work in programming language design", "and her dedication to improving the field of computer", "science left a lasting impact on the industry."],
    "Adele Goldberg": ["Adele Goldberg is a prominent computer scientist known for her", "contributions to the development of Smalltalk, a pioneering object-oriented", "programming language. She played a vital role in the development of graphical", "user interfaces, which are now widely used in modern computing."],
    "Barba Liskov": ["Barbara Liskov is a pioneering computer scientist known for her groundbreaking", "work in programming languages and software engineering. She is particularly", "renowned for developing the programming language CLU, which introduced", "key concepts like abstract data types and the Liskov Substitution Principle,", "which is a fundamental principle in object-oriented programming."],
    "Radia Perlman": ["Radia Perlman is a renowned computer scientist known for her pioneering work", "in network design and development. She is most famous for inventing", "the Spanning Tree Protocol (STP), a fundamental algorithm that revolutionized", "the way data is routed through complex networks, contributing significantly", "to the stability and scalability of modern Ethernet networks."],
    "Frances Allen": ["Frances Allen was a pioneering American computer scientist known", "for her significant contributions to the field of compiler design and optimization.", "She was the first woman to receive the Turing Award in 2006, one of the highest honors", "in computer science, for her groundbreaking work in program optimization and her", "influence on the design of programming languages."],
    "Shafi Goldwasser": ["Shafi Goldwasser is a renowned computer scientist and a pioneer", "in the field of cryptography. She is known for her groundbreaking work in the development", "of zero-knowledge proofs and has made significant contributions to complexity theory", "and the theory of cryptography. Goldwasser has received numerous awards", "and honors for her work, including the Turing Award in 2012, which she shared", "with Silvio Micali, for their transformative work in cryptography", "and their impact on internet security."],
    "Donna Strickland": ["Donna Strickland is a Canadian physicist known for her groundbreaking", "work in the field of laser physics. In 2018, she was awarded the Nobel Prize", "in Physics, becoming the third woman in history to receive the Nobel Prize", "in this category, for her contributions to the", "development of high-intensity, ultra-short optical pulses."],
    "Joan Clarke": ["Joan Clarke was a British cryptanalyst and mathematician", "who made significant contributions to breaking the German Enigma code", "during World War II as part of the Bletchley Park codebreaking team. She was", "known for her exceptional analytical skills and her work alongside", "figures like Alan Turing, helping to decipher encrypted messages critical to", "the war effort. Clarke's contributions to codebreaking remained relatively unknown", "until many years after the war due to the secrecy of her work at Bletchley Park."]
}
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
        if x >= 810 and x <= 910:
            return 7
        if x >= 940 and x <= 1040:
            return 8
        if x >= 1070 and x <= 1170:
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
    message = ["Let's play Womeno!", "This is UNO, with a spin! You will be playing against a computer.", "You may match cards in the pile by either color or person.", "Click on the card you want to play. Press 'd' if you want to draw a card.", "If you ever want to learn more about the woman on your card,", "simply right click on the card!", "Good luck, and press 'Enter' to begin :)"]
    font = pygame.font.Font (None, 45)
    msg_y = 200
    for m in message:
        text = font.render(m, True, (255, 255, 255))  # (R, G, B) for white
        screen.blit(text, (150, msg_y))
        msg_y += 30
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
            if event.button == 3 and your_turn:
                clicked_x, clicked_y = event.pos
                selected_index = find_card(clicked_x, clicked_y)
                card = player[selected_index - 1]
                if card[0] in women_in_stem:
                    message = women_in_stem_facts[card[0]]
                    msg_y = 150
                    for m in message:
                        font = pygame.font.Font(None, 40)
                        text = font.render(m, True, (255, 255, 255))  # (R, G, B) for white
                        screen.blit(text, (100, msg_y))
                        msg_y += 40
                else:
                    message = "ummm...are you sure you meant to click on this card?"
                    font = pygame.font.Font(None, 50)
                    text = font.render(message, True, (255, 255, 255))  # (R, G, B) for white
                    screen.blit(text, (100, msg_y))
                    msg_y += 40

                pygame.display.update()
                time.sleep(5)

            if event.button == 1 and your_turn:  # Left mouse button clicked
                print("MOUSE CLICKED")
                clicked_x, clicked_y = event.pos
                selected_index = find_card(clicked_x, clicked_y)
                print("Card selected at index:", selected_index)
                if selected_index != -1:
                    card = player[selected_index - 1]
                    if valid_play(play_stack[-1], card):
                        play_stack.append(card)
                        player.pop(selected_index - 1)
                        create_card_object(600, 130, rectangle_width * 1.5, rectangle_height * 1.5, play_stack[-1][0], play_stack[-1][1], True)
                        pygame.display.update()

                        if len(player) == 0:
                            screen.fill((0, 0, 0))
                            message = "You Win!"
                            font = pygame.font.Font(None, 75)
                            text = font.render(message, True, (255, 255, 255))  # (R, G, B) for white
                            screen.blit(text, (150, 300))
                            pygame.display.update()
                            time.sleep(10)
                            pygame.quit()
                            

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
        if len(computer) == 0:
            screen.fill((0, 0, 0))
            message = "Aww No! The Computer Won :("
            font = pygame.font.Font(None, 75)
            text = font.render(message, True, (255, 255, 255))  # (R, G, B) for white
            screen.blit(text, (100, 300))
            pygame.display.update()
            time.sleep(10)
            pygame.quit()
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

    # if len(player) == 0:
    #     message = "Yay you won!"
    #     font = pygame.font.Font(None, 36)
    #     text = font.render(message, True, (255, 255, 255))  # (R, G, B) for white
    #     screen.blit(text, (300, 380))

    # if len(computer) == 0:
    #     message = "Aww No! The Computer Won!"
    #     font = pygame.font.Font(None, 36)
    #     text = font.render(message, True, (255, 255, 255))  # (R, G, B) for white
    #     screen.blit(text, (300, 380))

    message = "The computer has: " + str(len(computer)) + " cards"
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, (255, 255, 255))  # (R, G, B) for white
    screen.blit(text, (20, 30))

    pygame.display.update()

pygame.quit()