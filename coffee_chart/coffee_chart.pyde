coffees = [
  { 'name':'cafe con leche','espresso':50, 'hotwater':0, 'steamedmilk':30,'foamedmilk':0  },
  { 'name':'espresso',      'espresso':60, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'demi-creme',    'espresso':40, 'hotwater':0, 'steamedmilk':40,'foamedmilk':0  },
  { 'name':'americano',     'espresso':60, 'hotwater':30,'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'capucchino',    'espresso':40, 'hotwater':0, 'steamedmilk':30,'foamedmilk':30 },
  { 'name':'latte',         'espresso':35, 'hotwater':0, 'steamedmilk':10,'foamedmilk':30 },
  { 'name':'ristretto',     'espresso':30, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'macchiato',     'espresso':40, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':60 },
  { 'name':'flat white',    'espresso':40, 'hotwater':0, 'steamedmilk':60,'foamedmilk':0  }
]

size(800, 800)
background('#004477')

mug = 110
col = 1
row = 1

for coffee in coffees:
    x = width / 4 * col # 200
    y = height / 4 * row # 200
    level = 0
    
    #espresso
    noStroke()
    fill('#332222')
    espresso = coffee['espresso']
    rect(x-mug/2, y+mug/2-espresso-level, mug, espresso)
    level += espresso
    
    #hotwater
    fill('#0099FF')
    hotwater = coffee['hotwater']
    rect(x-mug/2, y+mug/2-hotwater-level, mug, hotwater)
    level += hotwater
    
    #steamedmilk
    fill('#FFFFFF')
    steamedmilk = coffee['steamedmilk']
    rect(x-mug/2, y+mug/2-steamedmilk-level, mug, steamedmilk)
    level += steamedmilk
    
    #foamedmilk
    fill('#DDDDDD')
    foamedmilk = coffee['foamedmilk']
    rect(x-mug/2, y+mug/2-foamedmilk-level, mug, foamedmilk)
    level += foamedmilk
    
    #mug
    stroke('#FFFFFF')
    strokeWeight(4)
    noFill()
    arc(x+mug/2,y, 40,40, -HALF_PI, HALF_PI)
    arc(x+mug/2,y, 65,65, -HALF_PI, HALF_PI)
    square(x-mug/2,y-mug/2, mug)
    
    #label
    fill('#FFFFFF')
    name = coffee['name']
    text(name, x-textWidth(name)/2, y+90)
    
    if col % 3 == 0:
        row += 1
        col = 1
    else:
        col += 1
