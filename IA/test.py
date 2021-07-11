def formatdata(data, outbpf,con)#Output data, output data, equal spacing
    data = blured
    lon = np.linspace(-180, 180, nx)
    # lon = np.round(lon,2)
    lat = np.linspace(90,-90, ny)
    # lat = np.round(lat,2)
    lon, lat = np.meshgrid(lon, lat)
    layers = np.arange(np.min(data),np.max(data),con)#Set equal spacing to con
    C = plt.contour(lon,lat,data,layers)
    values = C.layers
    axes = C.allsegs
    # axes = np.round(axes,2)
    ddict = []
    #Propose drawing image data from the returned results
    for layer in range(len(values)):
        # print(layer)
        buf = buffer(values[layer],axes[layer])
        ddict.append(dict(buf))
    #Here is the output in GEOJSON format, adjust by yourself
    # geojson = codecs.open(outbpf,"w", encoding='utf-8')
     
    jsondata = {"type":"FeatureCollection", "features":ddict}
    #Output to bpf binary format
    ed = geobuf.encode(jsondata)
    with open(outbpf, "wb") as f:
        f.write(ed)
        print("bpf write success")
    # geojson.write(json.dumps({"type":"FeatureCollection", "features":ddict}) + '\n')
    # geojson.close()
    # plt.show()
    print('create contour success^_^')
 
def buffer(value,axes):
    ####Convert an array to a list
    temp = axes
    t = []
    for i in range(len(axes)):
        temp[i] = np.round(temp[i],5)
        tt = temp[i].tolist()
        t.append(tt)
    # temp = axes.tolist()
    ct = {"type":"Feature",
            "properties":{'Counter':value},
            "geometry":{
                "type":"MultiLineString",
                "coordinates":t
                }
    }
    
    return ct