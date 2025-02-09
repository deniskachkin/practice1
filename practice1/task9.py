print ('Введите плей-лист папы:')
song_1 = input()
song_2 = input()
song_3 = input()
song_4 = input()
song_5 = input()
print ('Плей-лист мамы:')
playlist = [song_1, song_2, song_3, song_4, song_5]
for songs in reversed(playlist):
  print(songs)