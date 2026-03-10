import pygame.event, pygame.time
import sys
from pygame import (
    QUIT, KEYDOWN, K_ESCAPE,
    MOUSEBUTTONDOWN, MOUSEBUTTONUP, K_UP, K_DOWN
)

class EventControl:
    def __init__(self, debounce_ms = 200):
        self.debounce_ms = debounce_ms
        self._last_click_time = 0
        self.click = False   
        self.choose_button = 0
        self.fake_choose_button = 0
        self.wait_button = 0
        
    def event_pool(self):         
        for event in pygame.event.get():
            self.event = event

    def mouse_get(self):
        self.mx, self.my = pygame.mouse.get_pos() 

    def MOUSEBUTTONDOWN(self):
            self.set_click(False)
            if self.comparison_type(MOUSEBUTTONDOWN) and self.choose_button == 1:
                self.set_choose_button(0) 
                now = pygame.time.get_ticks()  
                if now > self.debounce_ms + self._last_click_time:                
                    self._last_click_time = now
                    self.set_click(True)      

    def event_button_check(self, standart, nostandart, sound_and_func):
        if self.fake_choose_button == 1 and self.wait_button == 1:
            self.fake_choose_button = 0
        elif self.fake_choose_button == 1:
            self.wait_button = 1
            self.fake_choose_button = 0
            nostandart()
            sound_and_func()
        else:
            self.wait_button = 0
            standart()
    
    def set_click(self, click: bool):
        self.click = click
    
    def get_click(self):
        return self.click
    
    def set_choose_button(self, choose: int):
        self.choose_button = choose

    def set_choose_fake_button(self, fake_choose: int):
        self.fake_choose_button = fake_choose
    
    def comparison_type(self, event_type):
        return self.event.type == event_type
    
    def comparison_key(self, event_key):
        return self.event.key == event_key
    
    def set_key(self, event_key):
        self.event.key = event_key
    