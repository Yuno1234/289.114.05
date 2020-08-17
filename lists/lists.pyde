size(600, 600)
background('#004477')
noStroke()

rainbow = [
    '#FF0000',
    '#FF9900',
    '#FFFF00',
    '#00FF00',
    '#0099FF',
    '#6600FF'
]

translate(0, height/10*2)
bandsize = height/10

for color in rainbow:
    fill(color)
    rect(0,0, width, bandsize)
    translate(0, bandsize)
    
students = [
    ['Sam',24],
    ['Jo',18],
    ['Ed',31]
]

print(students[0][1])   #24
print(students[2][1])   #31 
