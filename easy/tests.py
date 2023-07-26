def first(message):
    def second():
        print('Wrapper function 1')
        return message().upper()
    return second


@first
def my_name():
    return 'My name is Kevin'


print(my_name())