size(800, 800)
background('#004477')
noStroke()
csv = loadStrings('list_of_best-selling_video_games.csv')

w = csv[1].split('\t')[1]
rect(0, 0, int(w)/1000000, 10)
