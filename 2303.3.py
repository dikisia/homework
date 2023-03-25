tracks = {}
while True:
    chart_position = input("Введите место в чарте (или 'off' для выхода): ")
    if chart_position == "off":
        break
    artist = input("Введите исполнителя: ")
    track_name = input("Введите название трека: ")
    tracks[(chart_position, artist)] = track_name

print(tracks)