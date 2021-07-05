
def myScpdataset(scpfile):
    scpdata=[]
    with open(scpfile,'r',encoding='utf-8') as f:
        for pairs in f.readlines():
            wavdir=pairs.split('|')[0]
            spkid=int(pairs.split('|')[1])-1
            scpdata.append((wavdir,spkid))
        f.close()
    return scpdata
        

if __name__=="__main__":
    pass



















