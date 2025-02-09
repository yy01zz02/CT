        # print(post_id)
img = Image(imagelocation)
count = 0
maxglosim = 0
maxlocsim = 0
maximum = 0
gridmax=0
vectormax=0

for f in col.find():
    llfeature = pickle.loads(f['llfeature'])
    glfeature = pickle.loads(f['glfeature'])
    count = count+1
    perc = (count/360)  * 100
    sys.stdout.write("\r%d%%" % perc)
    sys.stdout.flush()
    locsim = np.absolute((llfeature-img.llfeature).sum())
    glosim = np.logical_xor(glfeature,img.glfeature).sum()
    distance = locsim+glosim
    if(glosim>maxglosim):