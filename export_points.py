import c4d
from c4d import utils

def main():
    doc = c4d.documents.GetActiveDocument()
    selected = doc.GetActiveObjects(0)[0]
    points = selected.GetAllPoints()

    
    savePath=c4d.storage.SaveDialog()
    
    if savePath :
        f= open(savePath,"w+")
        print 'saving to :'+savePath
        f.write("{\"points\":[")
        for a in points :
            out = '{ \"x\":'+str( a.x) + ', \"y\":'+ str(a.y) + ', \"z\":'+str(a.z)+'},'
            f.write(out)
        f.write("]}")
    
        #f.write("This is line %d\r\n" % (i+1))
        
if __name__ == '__main__':
    main()