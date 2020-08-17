size(800, 800)
background('#004477')
noStroke()
csv = loadStrings('list_of_best-selling_video_games.csv')

barHeight = height/50
n = 1
colour = 0
rainbow = [
    '#FF0000',
    '#FF9900',
    '#FFFF00',
    '#00FF00',
    '#0099FF',
    '#6600FF'
]

for game in range(50):

    fill(rainbow[colour])
    w = csv[n].split('\t')[1]
    rect(0, 0, int(w)/210000, barHeight)
    
    fill('#000000')
    title = csv[n].split('\t')[2]
    text(title, 5, 13)
    translate(0, barHeight)
    
    n += 1
    if colour == 5:
        colour = 0
    else:
        colour += 1
