"""
    Author: Morgan
    Type: else
    Project name: AK47
    Version: 1.1.4
    Function: card game AK47
    Date: 13/08/2021
"""

import pygame
import random as r
from pygame.locals import *

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 128, 0)
orange = (255, 127, 0)
blue = (0, 20, 255)
brown = (128, 64, 0)
violet = (127, 0, 255)
sea_green = (46, 139, 87)
grey = (127, 127, 127)
spring_green = (60, 179, 113)
lime = (0, 255, 0)
mid_night_blue = (25, 25, 112)

# screen's size
screen_width = 1472
screen_height = 828

# pokers
cards_back = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/card_back.png'
aa = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/a_club.png'
ba = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/a_diamond.png'
ca = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/a_heart.png'
da = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/a_spade.png'
a2 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/2_club.png'
b2 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/2_diamond.png'
c2 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/2_heart.png'
d2 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/2_spade.png'
a3 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/3_club.png'
b3 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/3_diamond.png'
c3 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/3_heart.png'
d3 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/3_spade.png'
a4 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/4_club.png'
b4 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/4_diamond.png'
c4 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/4_heart.png'
d4 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/4_spade.png'
a5 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/5_club.png'
b5 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/5_diamond.png'
c5 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/5_heart.png'
d5 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/5_spade.png'
a6 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/6_club.png'
b6 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/6_diamond.png'
c6 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/6_heart.png'
d6 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/6_spade.png'
a7 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/7_club.png'
b7 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/7_diamond.png'
c7 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/7_heart.png'
d7 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/7_spade.png'
a8 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/8_club.png'
b8 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/8_diamond.png'
c8 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/8_heart.png'
d8 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/8_spade.png'
a9 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/9_club.png'
b9 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/9_diamond.png'
c9 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/9_heart.png'
d9 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/9_spade.png'
a10 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/1_club.png'
b10 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/1_diamond.png'
c10 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/1_heart.png'
d10 = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/1_spade.png'
aj = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/j_club.png'
bj = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/j_diamond.png'
cj = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/j_heart.png'
dj = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/j_spade.png'
aq = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/q_club.png'
bq = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/q_diamond.png'
cq = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/q_heart.png'
dq = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/q_spade.png'
ak = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/k_club.png'
bk = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/k_diamond.png'
ck = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/k_heart.png'
dk = '/Users/Jane/PycharmProjects/pycharmtest/cardgame/k_spade.png'
help_pic = '/Users/Jane/PycharmProjects/pycharmtest/resources/help.png'
back_pic = '/Users/Jane/PycharmProjects/pycharmtest/resources/back.png'
yn = '/Users/Jane/PycharmProjects/pycharmtest/resources/yes_no.png'
y = '/Users/Jane/PycharmProjects/pycharmtest/resources/yes.png'
n = '/Users/Jane/PycharmProjects/pycharmtest/resources/no.png'

# shuffle
cards_list = [aa, a2, a3, a4, a5, a6, a7, a8, a9, a10, aj, aq, ak, ba, b2, b3, b4, b5, b6, b7, b8, b9, b10, bj, bq, bk, ca, c2, c3, c4, c5, c6, c7, c8, c9, c10, cj, cq, ck, da, d2, d3, d4, d5, d6, d7, d8, d9, d10, dj, dq, dk]
r.shuffle(cards_list)

lista = [cards_list[0], cards_list[1], cards_list[2], cards_list[3], cards_list[4], cards_list[5]]
listb = [cards_list[51]]
listc = [cards_list[6], cards_list[7], cards_list[8], cards_list[9], cards_list[10], cards_list[11], cards_list[12], cards_list[13], cards_list[14], cards_list[15], cards_list[16], cards_list[17], cards_list[18], cards_list[19], cards_list[20], cards_list[21], cards_list[22], cards_list[23], cards_list[24], cards_list[25], cards_list[26], cards_list[27], cards_list[28], cards_list[29], cards_list[30], cards_list[31], cards_list[32], cards_list[33], cards_list[34], cards_list[35], cards_list[36], cards_list[37], cards_list[38], cards_list[39], cards_list[40], cards_list[41], cards_list[42], cards_list[43], cards_list[44]]
listd = [cards_list[50], cards_list[49], cards_list[48], cards_list[47], cards_list[46], cards_list[45]]

global card_width
global card_height
global ccw
global cch
global turn
card_width = 700
card_height = 591
ccw = 700
cch = 70
turn = 1
game_screen = pygame.display.set_mode((screen_width, screen_height))

def start_interface():
    game_screen.fill(sea_green)
    rules_font = pygame.font.SysFont("monospace", 40)
    rp = rules_font.render('How to play:', 1, white)
    rp1 = rules_font.render('1.Choose one card in your cards similar to the single card on your right.', 1, white)
    rp2 = rules_font.render('2.Otherwise, click the cards pile on your left.', 1, white)
    rw = rules_font.render('How to win:', 1, white)
    rw1 = rules_font.render('1.You left with no cards', 1, white)
    rw2 = rules_font.render('2.You have fewer cards than your component when there is no cards on your left.', 1, white)
    rw3 = rules_font.render("3.You have eight or fewer cards contain the 'A', 'K', '4', '7' cards.", 1, white)
    start_font = pygame.font.SysFont("monospace", 100)
    game_screen.blit(rp, (screen_width / 2 - 50, 100))
    game_screen.blit(rp1, (screen_width / 6, 180))
    game_screen.blit(rp2, (screen_width / 6, 260))
    game_screen.blit(rw, (screen_width / 2 - 50, 340))
    game_screen.blit(rw1, (screen_width / 6, 420))
    game_screen.blit(rw2, (screen_width / 6, 500))
    game_screen.blit(rw3, (screen_width / 6, 580))
    game_screen.blit(pygame.image.load(back_pic), (screen_width - 150, screen_height - 150))
    pygame.display.update()

def game_interface():
    # initial display
    game_screen.fill(sea_green)
    pygame.display.set_caption("Welcome To AK47!!!!!!!!!!!!!!!")
    font = pygame.font.SysFont("monospace", 50)
    welcome = font.render("Welcome To AK47!!!", 1, white)
    yours = font.render("Your cards: ", 1, orange)
    computer_s = font.render("The computer's cards:", 1, blue)
    game_screen.blit(welcome, (10, 10))
    pygame.draw.rect(game_screen, black, (0, 413, 1472, 2))
    pygame.draw.rect(game_screen, spring_green, (1000, 335, 111, 167))
    pygame.draw.rect(game_screen, green, (700, 591, 111, 167))
    pygame.draw.rect(game_screen, green, (700, 70, 111, 167))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_back), (111, 167)), (200, 335))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_list[0]), (111, 167)), (card_width, card_height))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_list[1]), (111, 167)), (card_width + 20, card_height))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_list[2]), (111, 167)), (card_width + 40, card_height))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_list[3]), (111, 167)), (card_width + 60, card_height))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_list[4]), (111, 167)), (card_width + 80, card_height))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_list[5]), (111, 167)), (card_width + 100, card_height))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_back), (111, 167)), (ccw, cch))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_back), (111, 167)), (ccw + 20, cch))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_back), (111, 167)), (ccw + 40, cch))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_back), (111, 167)), (ccw + 60, cch))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_back), (111, 167)), (ccw + 80, cch))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_back), (111, 167)),  (ccw + 100, cch))
    game_screen.blit(pygame.image.load(help_pic), (screen_width - 100, 0))
    help = font.render("HELP", 1, black)
    game_screen.blit(help, (screen_width - 95, 100))
    game_screen.blit(yours, (50, 591))
    game_screen.blit(computer_s, (50, 70))
    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_list[51]), (111, 167)), (1000, 335))
    pygame.draw.rect(game_screen, sea_green, (170, 530, 400, 50))
    card_num = font.render('{} cards left'.format(len(listc)), 1, lime)
    game_screen.blit(card_num, (170, 530))
    your_turn = font.render('your turn', 1, white)
    game_screen.blit(your_turn, (card_width, card_height + 180))
    pygame.display.update()

def computer():
    global game_screen
    global turn
    global lista, listb, listc, listd
    for i in range(1, len(listd) + 1):
        if listd[i - 1][49] == listb[0][49] or listd[i - 1][51] == listb[0][51]:
            game_screen.blit(pygame.transform.smoothscale(pygame.image.load(listd[i - 1]), (111, 167)), (1000, 335))
            listb.remove(listb[0])
            listb.append(listd[i - 1])
            listd.remove(listd[i - 1])
            pygame.draw.rect(game_screen, sea_green, (ccw, cch, 650, 167))
            for j in range(1, len(listd)+1):
                game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_back), (111, 167)),  (ccw + 20 * (j - 1), cch))
            turn = 1
            break
    else:
            listd.append(listc[0])
            game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_back), (111, 167)), (ccw + 20 * (len(listd) - 1), cch))
            listc.remove(listc[0])
            turn = 1

def again():
    global do_main
    # game_screen.blit(pygame.image.load(yn), (20, 150))
    game_screen.blit(pygame.image.load(y), (50, 180))
    game_screen.blit(pygame.image.load(n), (160, 180))
    af = pygame.font.SysFont("monospace", 60)
    ask = af.render("Play again?", 1, mid_night_blue)
    game_screen.blit(ask, (20, 150))
    x1, y1 = pygame.mouse.get_pos()
    if 50 < x1 < 160 and 180 < y1 < 240:
        # shuffle again
        r.shuffle(cards_list)
        lista = [cards_list[0], cards_list[1], cards_list[2], cards_list[3], cards_list[4], cards_list[5]]
        listb = [cards_list[51]]
        listc = [cards_list[6], cards_list[7], cards_list[8], cards_list[9], cards_list[10], cards_list[11], cards_list[12], cards_list[13], cards_list[14], cards_list[15], cards_list[16], cards_list[17], cards_list[18], cards_list[19], cards_list[20], cards_list[21], cards_list[22], cards_list[23], cards_list[24], cards_list[25], cards_list[26], cards_list[27], cards_list[28], cards_list[29], cards_list[30], cards_list[31], cards_list[32], cards_list[33], cards_list[34], cards_list[35], cards_list[36], cards_list[37], cards_list[38], cards_list[39], cards_list[40], cards_list[41], cards_list[42], cards_list[43], cards_list[44]]
        listd = [cards_list[50], cards_list[49], cards_list[48], cards_list[47], cards_list[46], cards_list[45]]
        game_screen.fill(sea_green)
        game_interface()
        pygame.display.update()
    if 160 < x1 < 270 and 180 < y1 < 240:
        do_main = False

def main():
    """
        main function
        __version__ = 1.1.4
    """
    global do_main
    global turn
    global lista, listb, listc, listd
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("monospace", 50)
    game_interface()
    do_main = True
    while do_main:
        pygame.draw.rect(game_screen, sea_green, (170, 530, 400, 50))
        card_num = font.render('{} cards left'.format(len(listc)), 1, lime)
        game_screen.blit(card_num, (170, 530))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                do_main = False
            if event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                pygame.draw.rect(game_screen, sea_green, (600, 540, 700, 50))
                # 点help
                if screen_width - 100 < x < screen_width and 0 < y < 150:
                    start_interface()
                # 点back
                if screen_width - 150 < x < screen_width and screen_height - 100 < y < screen_height:
                    game_screen.fill(sea_green)
                    pygame.display.set_caption("Welcome To AK47!!!!!!!!!!!!!!!")
                    font = pygame.font.SysFont("monospace", 50)
                    welcome = font.render("Welcome To AK47!!!", 1, white)
                    yours = font.render("Your cards: ", 1, orange)
                    computer_s = font.render("The computer's cards:", 1, blue)
                    game_screen.blit(welcome, (10, 10))
                    pygame.draw.rect(game_screen, black, (0, 413, 1472, 2))
                    pygame.draw.rect(game_screen, spring_green, (1000, 335, 111, 167))
                    pygame.draw.rect(game_screen, green, (700, 591, 111, 167))
                    pygame.draw.rect(game_screen, green, (700, 70, 111, 167))
                    game_screen.blit(pygame.image.load(help_pic), (screen_width - 100, 0))
                    help = font.render("HELP", 1, black)
                    game_screen.blit(help, (screen_width - 95, 100))
                    game_screen.blit(yours, (50, 591))
                    game_screen.blit(computer_s, (50, 70))
                    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_back), (111, 167)), (200, 335))
                    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(listb[0]), (111, 167)), (1000, 335))
                    pygame.draw.rect(game_screen, sea_green, (170, 530, 400, 50))
                    card_num = font.render('{} cards left'.format(len(listc)), 1, lime)
                    game_screen.blit(card_num, (170, 530))
                    your_turn = font.render('your turn', 1, white)
                    game_screen.blit(your_turn, (card_width, card_height + 180))
                    pygame.display.update()
                    for j in range(1, len(lista) + 1):
                        game_screen.blit(pygame.transform.smoothscale(pygame.image.load(lista[j - 1]), (111, 167)),  (card_width + 20 * (j - 1), card_height))
                    for j in range(1, len(listd)+1):
                        game_screen.blit(pygame.transform.smoothscale(pygame.image.load(cards_back), (111, 167)),  (ccw + 20 * (j - 1), cch))
                for i in range(1, len(lista) + 1):
                    # 点a出牌
                    if i < len(lista):
                        if card_width + 20 * (i - 1) < x < card_width + 20 * i and card_height < y < card_height + 167:
                            if lista[i - 1][49] == listb[0][49] or lista[i - 1][51] == listb[0][51]:
                                game_screen.blit(pygame.transform.smoothscale(pygame.image.load(lista[i - 1]), (111, 167)), (1000, 335))
                                listb.remove(listb[0])
                                listb.append(lista[i - 1])
                                lista.remove(lista[i - 1])
                                pygame.draw.rect(game_screen, sea_green, (card_width, card_height, 700, 167))
                                for j in range(1, len(lista) + 1):
                                    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(lista[j - 1]), (111, 167)),  (card_width + 20 * (j - 1), card_height))
                                pygame.display.flip()
                                turn = 0
                            else:
                                message = font.render('Please choose the right card.', 1, orange)
                                game_screen.blit(message, (600, 545))
                    if i == len(lista):
                        if card_width + 20 * (i - 1) < x < card_width + (20 * (i - 1) + 111) and card_height < y < card_height + 167:
                            if lista[i - 1][49] == listb[0][49] or lista[i - 1][51] == listb[0][51]:
                                game_screen.blit(pygame.transform.smoothscale(pygame.image.load(lista[i - 1]), (111, 167)), (1000, 335))
                                listb.remove(listb[0])
                                listb.append(lista[i - 1])
                                lista.remove(lista[i - 1])
                                pygame.draw.rect(game_screen, sea_green, (card_width, card_height, 700, 167))
                                for j in range(1, len(lista) + 1):
                                    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(lista[j - 1]), (111, 167)),  (card_width + 20 * (j - 1), card_height))
                                pygame.display.flip()
                                turn = 0
                            else:
                                message = font.render('Please choose the right card.', 1, orange)
                                game_screen.blit(message, (600, 545))
                # 点C发牌
                if 200 < x < 311 and 335 < y < 495:
                    lista.append(listc[0])
                    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(listc[0]), (111, 167)), (card_width + 20 * (len(lista) - 1), card_height))
                    listc.remove(listc[0])
                    turn = 0
                # computer's turn
                if turn == 0 and len(listc) != 0:
                    computer()
                    pygame.draw.rect(game_screen, sea_green, (170, 530, 400, 50))
                    card_num = font.render('{} cards left'.format(len(listc)), 1, lime)
                    game_screen.blit(card_num, (170, 530))
                    your_turn = font.render('your turn', 1, white)
                    game_screen.blit(your_turn, (card_width, card_height + 180))
                # claim winner
                if len(listc) != 0 and len(listd) == 0:
                    alose = font.render("You lose!!!", 1, white)
                    game_screen.blit(alose, (736, 400))
                    pygame.draw.rect(game_screen, green, (700, 70, 111, 167))
                    again()
                if len(listc) != 0 and len(lista) == 0:
                    awin = font.render("You won!!!", 1, white)
                    game_screen.blit(awin, (736, 400))
                    pygame.draw.rect(game_screen, green, (700, 591, 111, 167))
                    again()
                if len(listc) == 0:
                    pygame.draw.rect(game_screen, sea_green, (111, 167, 200, 335))
                    pygame.draw.rect(game_screen, black, (0, 413, 1472, 2))
                    game_screen.blit(pygame.transform.smoothscale(pygame.image.load(listb[0]), (111, 167)), (1000, 335))
                    if len(lista) < len(listd):
                        awin = font.render("You won!!!", 1, white)
                        game_screen.blit(awin, (736, 400))
                        again()
                    if len(lista) >= len(listd):
                        awin = font.render("You lose", 1, orange)
                        game_screen.blit(awin, (736, 400))
                        again()
                lista2 = []
                for e in range(1, len(lista) + 1):
                    lista2.append(lista[e - 1][49])
                    if 'a' in lista2:
                        if 'k' in lista2:
                            if '4' in lista2:
                                if '7' in lista2:
                                    if len(lista) <= 8:
                                        awin = font.render("You won!!!", 1, white)
                                        game_screen.blit(awin, (736, 400))
                                        again()
                # listd2 = []
                # for e in range(1, len(listd) + 1):
                                    #     listd2.append(listd[e - 1][49])
                                    # if 'a' in listd2:
                                    #     if 'k' in listd2:
                                    #         if '4' in listd2:
                                    #             if '7' in listd2:
                                    #                 if len(listd) <= 8:
                                    #                     alose = font.render("You lose!!!", 1, white)
                                    #                     game_screen.blit(alose, (736, 400))
                                    #                     do_main = False
                pygame.display.update()
                clock.tick(60)

if __name__ == '__main__':
    main()
