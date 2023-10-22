# Это заготовка проекта, скопируй её себе в редактор кода.

import pygame as pg

# Инициализация pg
pg.init()

# Размеры окна
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550

button_width=200
button_height=60

dog_width=350
dog_height=550

icon_size=80
padding=5 #отступ
text_size=40

font=pg.font.Font(None,text_size)
mini_font=pg.font.Font(None,15)

def load_image(file,width,height):
    image= pg.image.load(file)
    image=pg.transform.scale(image,(width,height))
    return image

def text_render(text):
    return font.render(str(text),True,'black')

class Button:
    def __init__(self,text,x,y,width=button_width,height=button_height,text_font=font):
        self.idle_image=load_image('images/button.png',width,height)
        self.pressed_image=load_image('images/button_clicked.png',width,height)
        self.image=self.idle_image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

        self.text_font=text_font

        self.text=text_render(text)
        self.text_rect=self.text.get_rect()
        self.text_rect.center=self.rect.center

        self.is_pressed=False

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        screen.blit(self.text,self.text_rect)

    def update(self):
        mouse_pos=pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if self.is_pressed:
                self.image=self.pressed_image
            else:
                self.image=self.idle_image

    def is_clicked(self,event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button==1:
            if self.rect.collidepoint(event.pos):
                self.is_pressed=True
        elif event.type == pg.MOUSEBUTTONUP and event.button==1:
            self.is_pressed=False


class Game:
    def __init__(self):

        # Создание окна
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("MY_PET")

        self.happiness=100
        self.health=100
        self.satiety=100
        self.money=10


        self.background=load_image('images/background.png',SCREEN_WIDTH,SCREEN_HEIGHT)

        self.dog_image=load_image('images/dog.png',dog_width,dog_height)
        self.happiness_image=load_image('images/happiness.png',icon_size,icon_size)
        self.satiety_image=load_image('images/satiety.png',icon_size,icon_size)
        self.health_image=load_image('images/health.png',icon_size,icon_size)
        self.money_image=load_image('images/money.png',icon_size,icon_size)
        button_x=SCREEN_WIDTH-button_width-padding

        self.eat_button=Button('еда',button_x,padding+icon_size)
        self.clothes_button=Button("одежда",button_x,padding+icon_size+padding+button_height)
        self.games_button=Button("игры",button_x,padding+icon_size+padding+button_height+padding+button_height)
        self.upgrade_button=Button("улучшить",SCREEN_WIDTH-icon_size,0,
                                   width=button_width // 3, height=button_height//3,
                                   text_font=mini_font)
    

        self.buttons=[self.eat_button, self.clothes_button, self.games_button, self.upgrade_button]

        self.INCREASE_COINS=pg.USEREVENT +1
        pg.time.set_timer(self.INCREASE_COINS,700)

        self.NEW_DAY=pg.USEREVENT +2
        pg.time.set_timer(self.NEW_DAY,1000*3600*24)

        self.run()


    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            
            self.eat_button.is_clicked(event)
            self.clothes_button.is_clicked(event)
            self.games_button.is_clicked(event)

            if event.type==self.INCREASE_COINS:
                self.money+=1


    def update(self):
        self.eat_button.update()
        self.clothes_button.update()
        self.games_button.update()



    def draw(self):
        self.screen.blit(self.background, (0,0))

        self.screen.blit(self.dog_image, (SCREEN_WIDTH // 2-dog_width//2, SCREEN_HEIGHT // 2-dog_height//2+100))

        self.screen.blit(self.happiness_image, (padding,padding))
        self.screen.blit(text_render(self.happiness),(padding+icon_size, padding*6))

        self.screen.blit(self.satiety_image, (padding,padding+icon_size))
        self.screen.blit(text_render(self.satiety),(padding+icon_size, padding*22))

        self.screen.blit(self.health_image, (padding,padding+icon_size+icon_size))
        self.screen.blit(text_render(self.health),(padding+icon_size, padding*38))

        self.screen.blit(self.money_image, (SCREEN_WIDTH-padding-icon_size,padding))
        self.screen.blit(text_render(self.money),(SCREEN_WIDTH-padding-icon_size-text_size-len(str(self.money))*10, padding*7))


        self.eat_button.draw(self.screen)
        self.clothes_button.draw(self.screen)
        self.games_button.draw(self.screen)
        
        pg.display.flip()


if __name__ == "__main__":
    Game()