# I have created this file

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyse(request):
    # Get the text
    text_input = request.POST.get("text", default="default")

    # checkboxes values
    removepunc = request.POST.get("removepunc", default="off")
    fullcaps = request.POST.get("fullcaps", default="off")
    newlineremover = request.POST.get("newlineremover", default="off")
    spaceremover = request.POST.get("spaceremover", default="off")
    charcount = request.POST.get("charcount", default="off")

    # check which checkbox is on
    if removepunc == "on":
        punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
        analysed = ""
        for char in text_input:
            if char not in punctuations:
                analysed += char
        params = {"purpose": "Remove Punctuations", "analysed_text": analysed}
        text_input = analysed

    if fullcaps == "on":
        analysed = ""
        for char in text_input:
            analysed += char.upper()
        params = {"purpose": "Changed to Uppercase", "analysed_text": analysed}
        text_input = analysed

    if newlineremover == "on":
        analysed = ""
        for char in text_input:
            if char != "\n" and char != "\r":
                analysed += char
        params = {"purpose": "New Lines Removed", "analysed_text": analysed}
        text_input = analysed

    if spaceremover == "on":
        analysed = ""
        for index, char in enumerate(text_input):
            if not text_input[index] == " " and text_input[index + 1] == " ":
                analysed += char

        params = {"purpose": "Extra Space have been removed", "analysed_text": analysed}
        text_input = analysed

    # if charcount == "on":
    #     count = 0
    #     for char in text_input:
    #         if char != " ":
    #             count += 1

    #     params = {"purpose": "Character in your Text", "analysed_text": count}

    if (
        removepunc != "on"
        and spaceremover != "on"
        and newlineremover != "on"
        and fullcaps != "on"
    ):
        return HttpResponse("Error")
    return render(request, "analyse.html", params)
