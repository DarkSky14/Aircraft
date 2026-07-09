from pygame import mixer, mixer_music


class Sound:
    def __init__(self, address) -> None:
        self.sound = mixer
        self.load = self.sound.Sound(address)

    def create_channel(self, volume=0.01, loops=0, maxtime=0, fade_ms=0):
        self.load.set_volume(volume)
        play = self.load.play(loops, maxtime, fade_ms)
        return play

    def stop_channel(self):
        self.load.stop()


class Music:
    def __init__(self, config, address: str, volume: float = 0.01) -> None:
        self.volume = volume
        self.config = config
        self.address = address
        self.archive = 0

    @staticmethod
    def music_get():
        """Get music object."""
        return mixer_music

    def music_pause(self):
        self.archive = (mixer_music.get_pos() / 1000) + self.archive
        mixer_music.pause()

    def set_position(self, pos=0):
        self.archive = pos

    def music_unpause(self, loops=-1, fade_ms=100):
        if self.config.check({"music": "True"}):
            mixer_music.set_volume(self.volume)
            mixer_music.play(loops, self.archive, fade_ms)
        else:
            self.set_position()

    def music_load(self, address):
        self.address = address
        mixer_music.load(self.address)

    def create_mus_channel(self, loops=-1, start=0, fade_ms=0):
        mixer_music.load(self.address, self.address)
        mixer_music.set_volume(self.volume)
        mixer_music.play(loops, start, fade_ms)

    def music_play(self):
        mixer_music.play(-1, 0, 100)

    def music_all(self, name_track, loops=-1, start=0, fade_ms=100):
        if self.config.check({"music": "False"}):
            if mixer_music.get_busy():
                mixer_music.pause()

        else:
            if not mixer_music.get_busy():
                self.music_load(name_track)
                self.create_mus_channel(loops, start, fade_ms)

            else:
                if self.address != name_track:
                    self.music_load(name_track)
                    self.create_mus_channel(loops, start, fade_ms)
