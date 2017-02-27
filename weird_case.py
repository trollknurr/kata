def to_weird_case(string):
    return ' '.join(
        map(
            lambda word: ''.join(
                map(
                    lambda (index, char): char.upper() if index % 2 == 0 else char.lower(),
                    enumerate(word)
                )
            ),
            string.split(' ')
        )
    )

print to_weird_case('This is a test')
