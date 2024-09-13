from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
  now = datetime.now()
  html = f'''
    <html>
      <body>
        <h1>Hello from vercel</h1>
        <p>The current time is {now}</p>
        <p>you successfully deployed it</p>
      </body>
    </html>
  '''
  
  return HttpResponse(html)
