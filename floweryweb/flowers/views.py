from django.shortcuts import render

from django.http import HttpResponse

import sqlite3

def index(request):
    
    conn = sqlite3.connect('flowers2019.db')
    c = conn.cursor()

    query = "SELECT * FROM flowers"
    c.execute(query)

    listings = c.fetchall()

    context = {
        'listings': listings
    }
    return render(request, 'index.html', context)
