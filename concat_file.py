import os

def concat(outpath, filepaths, filter=None, startswith=None, endswith=None):
    outdir = os.path.split(outpath)[0]
    if(not os.path.exists(outdir)):
        os.makedirs(outdir)
    
    outf = open(outpath, 'a')
    if (startswith is not None):
        for line in startswith:
            outf.writelines(line)
            
    for fp in filepaths:
        with open(fp, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            for line in lines:
                if(filter is None or filter(line)):
                    outf.write(line)
            
    if (endswith is not None):
        for line in endswith:
            outf.writelines(line)
    outf.close()    

def main():
    concat('./outfile.py', './demo.py')

if __name__ == '__main__':
    main()