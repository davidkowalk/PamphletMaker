from PyPDF2 import PdfFileReader, PdfFileWriter

def display_error(message, exit_after = True):
    print(message)

    if exit_after:
        exit()

def rearange_pdf(path):

    """
    Takes pdf-path, rearanges the pages and returns pdf-writer object.
    """

    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(path)

    document_length = pdf_reader.getNumPages()
    print(f"Document has {document_length} pages")

    if document_length % 4 != 0:
        display_error("The page-count of your document must be divisible by 4")

    sequence = generate_squence(document_length)

    for page in sequence:
        pdf_writer.addPage(pdf_reader.getPage(page))

    return pdf_writer


def generate_squence(pages):

    assert pages % 4 == 0

    max_page = pages-1
    min_page = 0

    arangement = list()

    while max_page > min_page:
        arangement.append(max_page)
        arangement.append(min_page)

        max_page -= 1
        min_page += 1

        arangement.append(min_page)
        arangement.append(max_page)

        max_page -= 1
        min_page += 1

    return arangement

def test_sequence():
    n = int(input("Number of Pages: "))
    print(generate_squence(n))

def main():

    in_path = input("File: ")
    writer = rearange_pdf(in_path)

    out_path = input("Output: ")
    with open(out_path, "wb") as file:
        writer.write(file)

if __name__ == '__main__':
    #test_sequence()
    main()
