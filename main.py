import pygame
import random


pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Rock Paper Scissors")

white = (255, 255, 255)
grey = (70, 70, 70)
menu_font = pygame.font.Font("freesansbold.ttf", 64)
font = pygame.font.Font("freesansbold.ttf", 32)
font2 = pygame.font.Font("freesansbold.ttf", 80)

background_img = pygame.image.load("image/bg.png")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

rock_button_img_original = pygame.image.load("image/rock.png")
rock_button_img_original = pygame.transform.scale(rock_button_img_original, (180, 180))

paper_button_img_original = pygame.image.load("image/paper.png")
paper_button_img_original = pygame.transform.scale(paper_button_img_original, (180, 180))

scissor_button_img_original = pygame.image.load("image/scissor.png")
scissor_button_img_original = pygame.transform.scale(scissor_button_img_original, (180, 180))

return_button_img_original = pygame.image.load("image/backward.png")
return_button_img_original = pygame.transform.scale(return_button_img_original, (100, 100))

image_button_img_original = pygame.image.load("image/infobutton.png")
image_button_img_original = pygame.transform.scale(image_button_img_original, (50, 50))

menu_img = pygame.image.load("image/menubg.png")
menu_img = pygame.transform.scale(menu_img, (900, 900))

rock_button_img = rock_button_img_original
paper_button_img = paper_button_img_original
scissor_button_img = scissor_button_img_original
return_button_img = return_button_img_original
image_button_img = image_button_img_original

win_text = font2.render('You Win', True, (0, 255, 0))
tie_text = font2.render('It\'s a Tie', True, (255, 255, 0))
lose_text = font2.render('You Lose', True, (255, 0, 0))
computer_text = font.render('', True, (0, 0, 0))

ai = ["rock", "paper", "scissors"]
ai_choice = ""
player = 0
outcome = 0
win_case = 0
button_enlarged = False
enlarged_time = 0

pygame.mixer.music.load("sound/music.mp3")
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

# Load sound effects
click_sound = pygame.mixer.Sound("sound/clicksound.mp3")
win_sound = pygame.mixer.Sound("sound/victory.mp3")
lose_sound = pygame.mixer.Sound("sound/lose.mp3")
tie_sound = pygame.mixer.Sound("sound/tie.mp3")

player_wins = 0
bot_wins = 0


def win_check():
    global outcome, ai, player, ai_choice, player_wins, bot_wins
    if ai_choice == ai[0]:
        if player == 1:
            outcome = 3
        if player == 2:
            outcome = 1
            player_wins += 1
        if player == 3:
            outcome = 2
            bot_wins += 1
    if ai_choice == ai[1]:
        if player == 1:
            outcome = 2
            bot_wins += 1
        if player == 2:
            outcome = 3
        if player == 3:
            outcome = 1
            player_wins += 1
    if ai_choice == ai[2]:
        if player == 1:
            outcome = 1
            player_wins += 1
        if player == 2:
            outcome = 2
            bot_wins += 1
        if player == 3:
            outcome = 3
    return outcome


def display_menu():
    screen.fill(grey)
    screen.blit(menu_img, (0, 0))
    title_text = menu_font.render("Rock Paper Scissors", True, (255, 255, 255))
    screen.blit(title_text, (450 - title_text.get_width() / 2, 300))
    start_text = menu_font.render("Click to start", True, (255, 255, 255))
    screen.blit(start_text, (450 - start_text.get_width() / 2, 400))


def display_game():
    screen.blit(background_img, (0, 0))
    screen.blit(rock_button_img, (50, 650))
    screen.blit(paper_button_img, (350, 650))
    screen.blit(scissor_button_img, (650, 650))
    screen.blit(computer_text, (20, 50))
    screen.blit(return_button_img, (50, 370))
    screen.blit(image_button_img, (750, 507))

    player_win_text = font.render(f'Player Wins: {player_wins}', True, (0, 255, 0))
    bot_win_text = font.render(f'Bot Wins: {bot_wins}', True, (255, 0, 0))
    screen.blit(player_win_text, (180, 430))
    screen.blit(bot_win_text, (180, 370))

    if win_case == 1:
        screen.blit(win_text, (50, 200))
    elif win_case == 2:
        screen.blit(lose_text, (50, 200))
    elif win_case == 3:
        screen.blit(tie_text, (50, 200))


running = True
menu_mode = True

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if menu_mode:
                menu_mode = False
                click_sound.play()
            else:
                mouse_pos = event.pos
                if rock_button_img.get_rect(topleft=(50, 650)).collidepoint(mouse_pos):
                    player = 1
                    ai_choice = ai[random.randint(0, 2)]
                    computer_text = font.render(f'The computer chose {ai_choice}', True, (255, 255, 255))
                    win_case = win_check()
                    rock_button_img = pygame.transform.scale(rock_button_img_original, (220, 220))
                    button_enlarged = True
                    enlarged_time = current_time
                    click_sound.play()
                    if win_case == 1:
                        win_sound.play()
                    elif win_case == 2:
                        lose_sound.play()
                    elif win_case == 3:
                        tie_sound.play()
                elif paper_button_img.get_rect(topleft=(350, 650)).collidepoint(mouse_pos):
                    player = 2
                    ai_choice = ai[random.randint(0, 2)]
                    computer_text = font.render(f'The computer chose {ai_choice}', True, (255, 255, 255))
                    win_case = win_check()
                    paper_button_img = pygame.transform.scale(paper_button_img_original, (220, 220))
                    button_enlarged = True
                    enlarged_time = current_time
                    click_sound.play()
                    if win_case == 1:
                        win_sound.play()
                    elif win_case == 2:
                        lose_sound.play()
                    elif win_case == 3:
                        tie_sound.play()
                elif scissor_button_img.get_rect(topleft=(650, 650)).collidepoint(mouse_pos):
                    player = 3
                    ai_choice = ai[random.randint(0, 2)]
                    computer_text = font.render(f'The computer chose {ai_choice}', True, (255, 255, 255))
                    win_case = win_check()
                    scissor_button_img = pygame.transform.scale(scissor_button_img_original, (220, 220))
                    button_enlarged = True
                    enlarged_time = current_time
                    click_sound.play()
                    if win_case == 1:
                        win_sound.play()
                    elif win_case == 2:
                        lose_sound.play()
                    elif win_case == 3:
                        tie_sound.play()
                elif return_button_img.get_rect(topleft=(50, 370)).collidepoint(mouse_pos):
                    menu_mode = True
                    player_wins = 0
                    bot_wins = 0
                    click_sound.play()
                elif image_button_img.get_rect(topleft=(750, 507)).collidepoint(mouse_pos):
                    image_to_display = pygame.image.load("image/hint.png")
                    image_to_display = pygame.transform.scale(image_to_display, (600, 600))
                    screen.blit(image_to_display, (150, 150))
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    screen.fill(grey)
                    pygame.display.flip()

    if menu_mode:
        display_menu()
    else:
        display_game()

    if button_enlarged and current_time - enlarged_time >= 300:
        rock_button_img = rock_button_img_original
        paper_button_img = paper_button_img_original
        scissor_button_img = scissor_button_img_original
        button_enlarged = False

    pygame.display.flip()

pygame.quit()
