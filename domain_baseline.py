"""Local, synthetic BIFF12 baseline, with no external files or office suite."""
import io, os, struct, sys, unittest, zipfile
sys.path.insert(0,os.getcwd())
from pyxlsb import biff12, open_workbook
from pyxlsb.reader import RecordReader, BIFF12Reader
from pyxlsb.worksheet import Worksheet
from pyxlsb.stringtable import StringTable
from pyxlsb.workbook import Workbook

def integer(value): return struct.pack('<I',value)
def string(value): return integer(len(value))+value.encode('utf-16le')
def record(tag, data=b''):
    # BIFF12 record identifiers retain continuation bits in their constant.
    out=bytearray() if tag else bytearray(b'\0')
    while tag:
        out.append(tag&255); tag >>= 8
    size=len(data)
    while size>=128:
        out.append((size&127)|128);size >>= 7
    out.append(size)
    return bytes(out)+data

def sheet():
    return b''.join([record(biff12.DIMENSION,integer(0)+integer(2)+integer(0)+integer(1)),
        record(biff12.SHEETDATA),record(biff12.ROW,integer(0)),
        record(biff12.FLOAT,integer(0)+integer(0)+struct.pack('<d',12.5)),
        record(biff12.ROW,integer(2)),record(biff12.BOOL,integer(1)+integer(0)+b'\x01'),
        record(biff12.SHEETDATA_END)])

class Baseline(unittest.TestCase):
    def test_scalars(self):
        with RecordReader(integer(23)+string('采集')) as r:
            self.assertEqual(r.read_int(),23)
            self.assertEqual(r.read_string(),'采集')
    def test_rows_and_rewind(self):
        with Worksheet('sample',io.BytesIO(sheet())) as w:
            self.assertEqual([[c.v for c in row] for row in w.rows()],[[12.5,None],[None,None],[None,True]])
            self.assertEqual([r[0].r for r in w.rows(sparse=True)],[0,2])
    def test_stringtable(self):
        body=record(biff12.SST,integer(2)+integer(2))+record(biff12.SI,b'\0'+string('甲'))+record(biff12.SI,b'\0'+string('乙'))+record(biff12.SST_END)
        with StringTable(io.BytesIO(body)) as table:
            self.assertEqual(table[1],'乙')
    def test_zip_workbook(self):
        buf=io.BytesIO()
        with zipfile.ZipFile(buf,'w') as z:
            z.writestr('xl/_rels/workbook.bin.rels','<Relationships><Relationship Id="rId1" Target="worksheets/sheet1.bin"/></Relationships>')
            z.writestr('xl/workbook.bin',record(biff12.SHEET,integer(0)+integer(1)+string('rId1')+string('观测'))+record(biff12.SHEETS_END))
            z.writestr('xl/worksheets/sheet1.bin',sheet())
        buf.seek(0)
        with Workbook(zipfile.ZipFile(buf)) as book:
            self.assertEqual(book.sheets,['观测'])
            with book.get_sheet('观测') as w:
                self.assertEqual(next(w.rows())[0].v,12.5)
    def test_close(self):
        fp=io.BytesIO(sheet())
        w=Worksheet('sample',fp);w.close()
        self.assertTrue(fp.closed)

if __name__=='__main__':unittest.main()
