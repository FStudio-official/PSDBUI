import sqlite3

def dbui(dbn=str(),query=str()):
    dbc = sqlite3.connect(f'{dbn}.db')
    db = dbc.cursor()
    try:
        db.execute(query)
    except sqlite3.OperationalError:
        print("SyntaxError!"+query)
    listo1= db.fetchall()
    listo=list()
    for lis in listo1:
        lis2=lis
        inew=str(lis2).removesuffix(")").removeprefix("(")
        listo.append(inew)
    
    edata=list()
    maxlen=0
    for lis in listo:
        edata.append(list(str(lis).split(',')))
        for ed in edata:
            for e in ed:
                lene=len(e)
                if lene > maxlen: maxlen=lene
    
    Spalten=int()
    for ed in edata:
        for e in ed:
            Spalten+=1
        break
    Zlen=(maxlen*Spalten)+Spalten
    zlenl=str()
    for _ in range(Zlen):
        zlenl=zlenl+"-"
    for ed in edata:
        for e in ed:
            Spalten+=1
        break
    text=zlenl+"\n"
    for ed in edata:
        for e in ed:
            dif=maxlen-len(e)
            difstr=str()
            for _ in range(dif):
                difstr=difstr+" "
            text=text+"|"+e+difstr
        text=text+"|"+"\n"+zlenl+"\n"
    print(text)
    dbc.commit()
    dbc.close()