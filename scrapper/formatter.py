import arabic_reshaper
from bidi.algorithm import get_display

def formatNumber(number)-> str:
    n = str(number)
    if len(n) ==1:
        n = "00"+n
    elif len(n) == 2:
        n="0"+n
    return n
def printa(str):
    reshaped_text = arabic_reshaper.reshape(str)    # correct its shape
    bidi_text = get_display(reshaped_text) 
    print(bidi_text)
