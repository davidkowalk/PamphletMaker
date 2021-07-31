def generate_squence(pages):

    assert pages % 4 == 0

    max_page = pages
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

    arangement.append(min_page)

    return arangement

def main():

    n = int(input("Number of Pages:"))
    print(generate_squence(n))

if __name__ == '__main__':
    main()
