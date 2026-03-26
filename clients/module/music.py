import pygame.mixer, pygame.mixer_music

class Sound:
    def __init__(self, address) -> None:
        self.sound = pygame.mixer
        self.load = self.sound.Sound(address)
        
    def create_channel(self, volume = 0.01, loops=0, maxtime=0, fade_ms=0):
        self.load.set_volume(volume)
        play = self.load.play(loops, maxtime, fade_ms)
        return play
    
    def stop_channel(self):
        stop = self.load.stop()
        return stop


class Music:
    def __init__(self, config, temp, address, volume: float = 0.01) -> None:
        self.music = pygame.mixer_music
        self.volume = volume
        self.config = config
        self.adress = address
        self.music.load(self.adress)
        self.temp = temp
        self.archive = 0

    def music_stop(self, fade_ms=100):
        self.music.fadeout(fade_ms)

    def music_get(self):
        return self.music
    
    def music_pause(self):
        self.archive = (self.music.get_pos() / 1000) + self.archive
        self.music.pause()

    def set_position(self, pos = 0):
        self.archive = pos

    def music_unpause(self, loops=-1, fade_ms=100):
        if self.config.check({"music": "True"}): 
            self.music.set_volume(self.volume)
            self.music.play(loops, self.archive, fade_ms)
        else:
            self.set_position()
    
    def music_load(self, address):
        self.adress = address
        self.music.load(self.adress)
    
    def create_mus_channel(self, loops=-1, start=0, fade_ms=0):
        self.music_load(self.adress)
        self.music.set_volume(self.volume)
        self.music.play(loops, start, fade_ms)

    def music_play(self):
        self.music.play(-1, 0, 100)

    def music_all(self, name_track, loops=-1, start=0, fade_ms=100):    
        arg = self.temp.get_value("musicID")
 
        if self.config.check({"music": "False"}): 
            if self.music.get_busy() == True:
                self.music.pause()
                       
        else:               
            if self.music.get_busy() == False:
                self.music_load(name_track)
                self.create_mus_channel(loops, start, fade_ms)
                self.temp.update_dict({"musicID": name_track})           
            
            elif self.music.get_busy() == True:
                if arg != name_track:
                    self.music_load(name_track)
                    self.create_mus_channel(loops, start, fade_ms)
                    self.temp.update_dict({"musicID": name_track})
      
