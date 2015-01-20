from django.shortcuts import render

from django.http import HttpResponse

def index (request):
    return HttpResponse ("Rango says hey there world! :) <br/> <a href='/rango/about'>About</a> ")

def about (request):
    return HttpResponse ("Rango says here is the about page ^.^ <a href='/rango/'>Index</a> <br/> This tutorial has been put together by Kristina Lazarova: 2088209l </br>")
