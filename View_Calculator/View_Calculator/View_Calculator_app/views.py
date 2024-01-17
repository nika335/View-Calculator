from django.http import HttpResponse


def odd_or_even(requet, number):
    if number % 2 == 0:
        number = "even"
    else:
        number = "odd"
    return(HttpResponse(f"This number is {number}"))





