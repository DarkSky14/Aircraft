import pygame.mixer, pygame.mixer_music

class Sound:
    def __init__(self) -> None:
        self.sound = pygame.mixer
        
    def create_channel(self, address, volume = 0.01, loops=0, maxtime=0, fade_ms=0):
        sound = self.sound.Sound(address)
        sound.set_volume(volume)
        play = sound.play(loops, maxtime, fade_ms)
        return play
    
    def stop_channel(self, sound: pygame.mixer.Sound):
        stop = sound.stop()
        return stop


class Music:
    def __init__(self, config, temp, volume: float = 0.01) -> None:
        self.music = pygame.mixer_music
        self.volume = volume
        self.config = config
        self.temp = temp
    
    def create_mus_channel(self, address, loops=-1, start=0, fade_ms=0):
        self.music.load(address, "music")
        self.music.set_volume(self.volume)
        play = self.music.play(loops, start, fade_ms)
        return play

    
    def music_all(self, name_track, loops=-1, start=0, fade_ms=100):    
        arg = self.temp.get_value("musicID")
 
        if self.config.check({"music": "False"}) == True: 
            if pygame.mixer_music.get_busy() == True:
                pygame.mixer_music.pause()
                       
        else:               
            if pygame.mixer_music.get_busy() == False:
                if self.temp.check({"musicID": "None"}) == True:
                    self.create_mus_channel(name_track, loops, start, fade_ms)
                    self.temp.update_dict({"musicID": name_track})

                else:
                    pygame.mixer_music.unpause()                
            
            elif pygame.mixer_music.get_busy() == True:
                if arg != name_track:
                    self.create_mus_channel(name_track,loops, start, fade_ms)
                    self.temp.update_dict({"musicID": name_track})
      
