"""Print out all the melons in our inventory."""


from melons import melons


def print_all_melons(melons):
    """Print every melon and corresponding attributes"""

    for melon_name, attributes in melons.items():
        print(melon_name)

        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

        print('==================')



"""def print_melon(name, seedless, price):
    'Print each melon with corresponding attribute information.'

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])"""
