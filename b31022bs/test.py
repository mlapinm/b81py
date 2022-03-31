text1 = """<p>The transition out of the Stone Age occurred between 6000 BCE and 2500 <a href="/wiki/BCE" class="mw-redirect" title="BCE">BCE</a> for much of humanity living in <a href="/wiki/North_Africa" title="North Africa">North Africa</a> and <a href="/wiki/Eurasia" title="Eurasia">Eurasia</a>. The first evidence of human <a href="/wiki/Metallurgy" title="Metallurgy">metallurgy</a> dates to between the <a href="/wiki/5th_millennium_BC" title="5th millennium BC">5th</a> and <a href="/wiki/6th_millennium_BC" title="6th millennium BC">6th</a> <a href="/wiki/Millennium" title="Millennium">millennium</a> BCE in the archaeological sites of <a href="/wiki/Majdanpek" title="Majdanpek">Majdanpek</a>, <a href="/w/index.php?title=Yarmovac&amp;action=edit&amp;redlink=1" class="new" title="Yarmovac (page does not exist)">Yarmovac</a>, and <a href="/wiki/Plo%C4%8Dnik" title="Plocnik">Plocnik</a> in modern-day Serbia (<a href="/wiki/Prokuplje#Archaeological_findings" title="Prokuplje">a copper axe from 5500 BCE</a> belonging to the <a href="/wiki/Vinca_culture" class="mw-redirect" title="Vinca culture">Vinca culture</a>), though not conventionally considered part of the Chalcolithic or "Copper Age", this provides the earliest known example of copper metallurgy.<sup id="cite_ref-11" class="reference"><a href="#cite_note-11">[11]</a></sup> Note the <a href="/wiki/Rudna_Glava" class="mw-redirect" title="Rudna Glava">Rudna Glava</a> mine in <a href="/wiki/Serbia" title="Serbia">Serbia</a>. <a href="/wiki/%C3%96tzi_the_Iceman" class="mw-redirect" title="Otzi the Iceman">Otzi the Iceman</a>, a <a href="/wiki/Mummy" title="Mummy">mummy</a> from about 3300 BCE carried with him a copper axe and a flint knife.</p>"""

text2 = """<a href="#cite_ref-Kandel_2000_7-0"><sup><i><b>a</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-1"><sup><i><b>b</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-2"><sup><i><b>c</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-3"><sup><i><b>d</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-4"><sup><i><b>e</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-5"><sup><i><b>f</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-6"><sup><i><b>g</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-7"><sup><i><b>h</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-8"><sup><i><b>i</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-9"><sup><i><b>j</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-10"><sup><i><b>k</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-11"><sup><i><b>l</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-12"><sup><i><b>m</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-13"><sup><i><b>n</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-14"><sup><i><b>o</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-15"><sup><i><b>p</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-16"><sup><i><b>q</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-17"><sup><i><b>r</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-18"><sup><i><b>s</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-19"><sup><i><b>t</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-20"><sup><i><b>u</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-21"><sup><i><b>v</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-22"><sup><i><b>w</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-23"><sup><i><b>x</b></i></sup></a> 
<a href="#cite_ref-Kandel_2000_7-24"><sup><i><b>y</b></i></sup></a>"""

text3 = """<a href="#cite_ref-Kandel_2000_7-0"><sup><i><b>a</b></i></sup>
</a> 
<a href="#cite_ref-Kandel_2000_7-1"><sup><i><b>b</b></i></sup></a>
<p>2</p>
<a></a> """


from bs4 import BeautifulSoup

def get_linkslen(soup):
  aa = soup.find_all('a')
  kk = []
  k = 1
  for e in aa:
      a = e.find_next_sibling()
      if a and a.name == 'a':
          k +=1
      else:
          kk += [k]
          k = 1
  return max(kk)



soup = BeautifulSoup(text3, 'lxml')

res = get_linkslen(soup)

print(res)

# print(soup)