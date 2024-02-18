import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_populations.svg')