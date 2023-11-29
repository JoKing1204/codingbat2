from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from app.forms import fonttimes, teen_sum, xyz, centeredsavage


# Create your views here.
def font_times(request: HttpRequest) -> HttpRequest:
    form = fonttimes(request.GET)

    if form.is_valid():
        n = form.cleaned_data["n"]
        term = form.cleaned_data["term"]
        result = ""
        for i in range(n):
            result += term[:3]
        return render(request, "fonttime.html", {"form": form, "result": result})
    else:
        return render(request, "fonttime.html", {"form": form})


def fix_teen(n):
    if n == 13 or n == 14 or n == 15 or n == 16 or n == 17 or n == 18 or n == 19:
        return 0
    return n


def no_teen_sums(request: HttpRequest) -> HttpRequest:
    form = teen_sum(request.GET)

    if form.is_valid():
        X = form.cleaned_data["X"]
        Y = form.cleaned_data["Y"]
        Z = form.cleaned_data["Z"]

        result = fix_teen(X) + fix_teen(Y) + fix_teen(Z)

        return render(
            request,
            "noteen.html",
            {"form": form, "X": X, "Y": Y, "Z": Z, "result": result},
        )
    else:
        return render(request, "noteen.html", {"form": form})


def xzy_there(request: HttpRequest) -> HttpRequest:
    a = False
    form = xyz(request.GET)

    if form.is_valid():
        term = form.cleaned_data["term"]

        for i in range(len(term) - 2):
            if term[i : i + 3] == "xyz" and (i == 0 or term[i - 1] != "."):
                a = True

        return render(request, "xyz.html", {"form": form, "term": term, "a": a})
    else:
        return render(request, "xyz.html", {"form": form})


def centered_savage(request: HttpRequest) -> HttpRequest:
    form = centeredsavage(request.GET)

    if form.is_valid():
        X = form.cleaned_data["X"]
        Y = form.cleaned_data["Y"]
        Z = form.cleaned_data["Z"]

        numbers = [X, Y, Z]
        minimum = min(numbers)
        maximum = max(numbers)

        numbers.remove(minimum)
        numbers.remove(maximum)

        avg = sum(numbers) // len(numbers)

        return render(
            request, "cnetered.html", {"form": form, "X": X, "Y": Y, "Z": Z, "avg": avg}
        )
    else:
        return render(request, "cnetered.html", {"form": form})
