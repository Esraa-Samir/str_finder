from dictionary import Dictionary

if __name__ == '__main__':
    dictionary = Dictionary(['helloworld', 'foo', 'bar', 'stylight_team', 'eso', ])
    result = dictionary.find_v1("seo")
    output = []
    for r in result:
        output.append(r)

    print(r)
