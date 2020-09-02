from win32com.client import constants, gencache
from pathlib import Path
from loguru import logger
import pythoncom


def word_2_pdf(wordPath: Path, pdfPath: Path):
    """
        word转pdf
        :param wordPath: word文件路径
        :param pdfPath:  生成pdf文件路径
    """
    try:
        pythoncom.CoInitialize()
        word = gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(str(wordPath), ReadOnly=1)
        doc.ExportAsFixedFormat(str(pdfPath),
                                constants.wdExportFormatPDF,
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
        word.Quit(constants.wdDoNotSaveChanges)
        return True
    except Exception as e:
        logger.info(e)
        return False
