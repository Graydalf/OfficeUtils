import concat_file as cf
import os

class PretreatmentObj:
    def __init__(self, outpath):
        self.outpath = outpath
        self.filepaths = []


class AndroidStringsConcat:

    def __init__(self):
        self.default_filenames = ['strings.xml', 'strings_v17.xml', 'strings_v181.xml', 'strings_v182.xml', 'strings_v210.xml', 'strings_v220.xml', 'strings_v230.xml', 'strings_v250.xml', 'strings_v260.xml']
        self.default_res_path = '/Users/chenqi/Proj/EBooking/android/EBookingAndroid/EBookingApp/src/main/res'
        self.default_values = ['values', 'values-en', 'values-ja', 'values-ko', 'values-th-rTH', 'values-vi-rVN', 'values-zh-rCN']
        self.default_out_dir = './out/'

    def pretreatment(self):
        pos = []
        # values_dirs = [x for x in os.listdir(self.default_res_path) if os.path.isdir(x) and os.path.split(x)[1].startswith(self.default_values_pre)]

        for values in self.default_values:
            p = PretreatmentObj(os.path.join(self.default_out_dir, values))
            pos.append(p)
            values = os.path.join(self.default_res_path, values)
            for fname in self.default_filenames:
                fpath = os.path.join(values, fname)
                if(not os.path.exists(fpath)):
                    continue
                p.filepaths.append(fpath)
        return pos
    
    def startswith(self):
        return ['<?xml version="1.0" encoding="utf-8"?>', '<resources xmlns:xliff="urn:oasis:names:tc:xliff:document:1.2">']

    def endswith(self):
        return ['</resources>']

    def filter_xml_head(self, line):
        if(line.strip().startswith('<?xml') or line.strip().startswith('<resources') or line.strip().startswith('</resources')):
            return False
        return True
        
    def concat(self):
        pos = self.pretreatment()
        for po in pos:
            print(po.outpath)
            cf.concat(po.outpath, po.filepaths, self.filter_xml_head, self.startswith(), self.endswith())


def main():
    asc = AndroidStringsConcat()
    asc.concat()

if __name__ == '__main__':
    main()