class MusicLibrary():
    def __init__(self):
        self.music_dict = {}

    def add_track(self, artist, track):
        if isinstance(artist, str) and isinstance(track, str):
            if artist in self.music_dict:
                song_list = self.music_dict[artist]
                song_list.append(track)
                self.music_dict[artist]  = song_list
                print(f'You have added {track} by {artist} to your music library')
            else:
                self.music_dict[artist] = [track]
                print(f'You have added {track} by {artist} to your music library.')
        else:
            raise Exception('Error: Ensure that both inputs are of type string')
    
    def view_artists(self):
        print('You have the following artists in your library:')
        for artist in self.music_dict.keys():
            print(f' * {artist}')
    
    def view_tracks_by_artist(self, artist):
        if isinstance(artist, str):
            if artist not in self.music_dict:
                print(f'{artist} does not exist in library. Use the add_track method first.')
            else:
                print(f'You have the following tracks by {artist} in your library:')
                for i in range(len(self.music_dict[artist])):
                    print(f' * {self.music_dict[artist][i]}')
        else:
            raise Exception('Error: Ensure that input is of type string')

    def view_library(self):
        for artist in self.music_dict:
            print(f'{artist}:')
            for i in range(len(self.music_dict[artist])):
                print(f' * {self.music_dict[artist][i]}')
    
    def remove_track(self, artist, track):
        if isinstance(artist, str) and isinstance(track, str):
            if artist not in self.music_dict or track not in self.music_dict[artist]:
                print(f'Either the artist {artist} or the track {track} does not exist in library. Please check input.')
            else:
                index_of_track = self.music_dict[artist].index(track)
                self.music_dict[artist].pop(index_of_track)
                print(f'You have removed {track} by {artist} from your music library.')
                if len(self.music_dict[artist]) == 0:
                    del self.music_dict[artist]
        else:
            raise Exception('Error: Ensure that both inputs are of type string')
    
    def remove_artist(self, artist):
        if isinstance(artist, str):
            if artist not in self.music_dict:
                print(f'{artist} does not exist in library.')
            else:
                del self.music_dict[artist]
                print(f'You have deleted {artist} and all their songs from your library.')
        else:
            raise Exception('Error: Ensure that both inputs are of type string')