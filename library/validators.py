from pathlib import Path
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PDFRequired:

    def __call__(self, file):
        if Path(file.name).suffix.lower() != ".pdf":
            raise ValidationError("PDF file is required")
        # Decode the first 4 bytes of PDF file, If pdf file, first 4 bytes of file = %PDF
        f = file.open("rb")  # Don't close this file, because this file will be used during signals, saving, etc
        f.seek(0)
        first_four_bytes = f.read(4)
        if first_four_bytes.decode("ascii", errors="ignore") != "%PDF":
            raise ValidationError("PDF file is required")
        f.seek(0)  # Restore file cursor to beginning
        return file


@deconstructible
class NonMaliciousPDFRequired:

    def __call__(self, file):
        """TODO: Implement this to screen against malicious PDF, Scan for Javascript and OpenAction objects"""
        return file
