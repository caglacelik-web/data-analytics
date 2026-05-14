# Open and create about_me.txt in append mode
f = open('about_me.txt', 'a')

# Write additional information to the file
f.write('\nMy perfect night out would be going to a nice restaurant for dinner, ')
f.write('then watching a movie or going for a walk along the lake.')

f.close()