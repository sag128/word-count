# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:09:09 2019

@author: sagar
"""

from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist= fulltext.split()
    worddic={}
    for word in wordlist:
        if word in worddic:
            
            worddic[word] +=1
        else:
            
            worddic[word] = 1
    
    sortedwords=sorted(worddic.items(),key=operator.itemgetter(1),reverse=True)
    print(sortedwords)
            
            
                
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})


def about(request):
    return render(request,'about.html')

