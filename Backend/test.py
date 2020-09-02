from zipfile import ZipFile, ZIP_DEFLATED
from openpyxl import Workbook
from openpyxl.xml.functions import tostring
from openpyxl.writer.excel import ExcelWriter
from openpyxl.packaging.extended import ExtendedProperties
from openpyxl.xml.constants import(
    ARC_APP,
    ARC_CORE,
    ARC_THEME,
    ARC_STYLE,
    ARC_ROOT_RELS,
    ARC_WORKBOOK
)

def get_bin_wb(obj:Workbook, filename):
    archive = ZipFile(filename, "w", ZIP_DEFLATED, allowZip64 = True)
    writer = ExcelWriter(obj, archive)

    props = ExtendedProperties()
    archive.writestr(ARC_APP, tostring(props.to_tree()))
    archive.writestr(ARC_CORE, tostring(obj))
    archive.close()
