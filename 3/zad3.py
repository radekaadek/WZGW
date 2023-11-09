# of 3
# Przeniesienie współrzędnych geodezyjnych na
# powierzchni elipsoidy – zadanie wprost (algorytm
# Kivioja)
# Aby wykonać zadanie wprost przeniesienia współrzędnych, możemy wykorzystać algo-
# rytm całkowania numerycznego zaproponowany w 1971 r. w pracy 1. Jest to nieskompli-
# kowany algorytm polegający na wykorzystaniu równań różniczkowych pierwszego rzędu
# dla linii geodezyjnej przedstawionych w równaniu 1., wynikających bezpośrednio z ele-
# mentarnego trójkąta na powierzchni elipsoidy, przedstawionego na rysunku 1:
# Rysunek 1: Elementarny trójkąt na powierzchni elipsoidy
# dϕ
# ds = cos A
# M , dλ
# ds = sin A
# N cos ϕ. (1)
# Długości promieni przekrojów w kierunku południka M i I wertykału N można obliczyć
# ze wzorów:
# Algorytm wykorzystuje również równanie Clairauta linii geodezyjnej:
# N cos ϕ sin A = c = const (2)
# wyrażające własność linii geodezyjnej mówiącą o tym, że iloczyn promienia równoleżnika
# p = N cos ϕ i sinusa jej azymutu w danym punkcie jest wartością stałą dla całej linii.
# 1L. Kivioja, „Computation of geodetic direct and indirect problems by computers accumulating in-
# crements from geodetic line elements,” Bulletin G´eod´esique (1946-1975), vol. 99, no. 1, pp. 55–63, 1971.
# 1
# Korzystając z własności dp
# ds = cos A sin ϕ i różniczkując równanie 2 względem s otrzymamy
# równanie różniczkowe pierwszego rzędu dla azymutu:
# dA
# ds = sin A tg ϕ
# N . (3)
# Realizacja równań 1, 2, 3 dla krótkich odcinków pozwala rozwiązać skutecznie zadanie
# wprost przeniesienia współrzędnych. Algorytm Kivioji stosujemy dla linii o długości do
# 150 kilometrów.
# Mając dane współrzędne ϕ1, λ1 punktu początkowego P1 oraz długość linii geodezyjnej
# s i jej azymut A1−2 w punkcie początkowym, możemy przystąpić do realizacji algorytmu.
# 1. Pierwszym krokiem jest podzielenie linii geodezyjnej na n elementów ds
# ds = s
# n, (4)
# gdzie ds < (1 ÷ 1.5) km, bądź dsi = 1 km, a ostatni element dsn < 1 km.
# 2. Obliczamy główne promienie krzywizny M i N w punkcie wyjściowym P1 oraz stałą
# c linii geodezyjnej.
# Mi = a(1 − e2)
# √(
# 1 − e2 sin2 ϕi
# )3 ; Ni = a
# √
# 1 − e2 sin2 ϕi
# 3. Pierwsze przybliżenie przyrostu szerokości i azymutu:
# dϕi = dsi · cos Ai
# Mi
# , (5)
# dAi = ds sin Ai tg ϕi
# Ni
# , (6)
# 4. Obliczenie szerokości i azymutu w punkcie środkowym (m) odcinka, na podstawie
# przyrostów:
# ϕim = ϕi + 1
# 2dϕi. (7)
# Aim = Ai + 1
# 2dAi. (8)
# 5. Obliczenie promieni krzywizn w kierunkach głównych w punkcie m:
# Mim = a(1 − e2)
# √(
# 1 − e2 sin2 ϕim
# )3 ; Nim = a
# √
# 1 − e2 sin2 ϕim
# 6. Ostateczne przyrosty szerokości, długości i azymutu:
# dϕim = ds · cos Aim
# Mim
# (9)
# dλim = ds · sin Aim
# Nim cos ϕim
# (10)
# dAim = ds · sin Aim tan ϕim
# Nim
# (11)
# of 2
# Metoda Vincentego – zadanie odwrotne∗
# Maciej Grzymała
# Wydział Geodezji i Kartografii
# Politechnika Warszawska
# 1. Oznaczenia
# a, b – dłuższa i krótsza półoś elipsoidy;
# e, f – pierwszy mimośród, spłaszczenie elipsoidy;
# ϕ, λ – szerokość i długość geodezyjna;
# ∆λ – różnica długości geodezyjnej;
# s – długość linii geodezyjnej;
# AAB , ABA – azymut prosty i odwrotny;
# α – azymut linii geodezyjnej na równiku;
# U – szerokość zredukowana;
# L – różnica długości na sferze pomocniczej;
# σ – odległość kątowa pomiędzy punktami na sferze;
# σm – odległość kątowa na sferze od równika do punktu środkowego linii geodezyjnej;
# 2. Dane
# ϕA, λA – współrzędne geodezyjne punktu A;
# ϕB , λB – współrzędne geodezyjne punktu B;
# a, e2 – parametry elipsoidy;
# 3. Szukane
# sAB – długość linii geodezyjnej pomiędzy punktami A i B;
# AAB , ABA – azymut prosty i odwrotny linii geodezyjnej;
# 4. Algorytm
# 1. Wyznaczenie krótkiej półosi oraz spłaszczenia elipsoidy:
# b = a√1 − e2; f = 1 − b
# a; (1)
# 2. Różnica długości geodezyjnych:
# ∆λ = λB − λA (2)
# ∗ T. Vincenty (1975). Direct and inverse solutions of geodesics on the ellipsoid with application of
# nested equations. Survey Review XXII, 176, April 1975
# 1
# 3. Obliczenie szerokości zredukowanych:
# tan(UA) = (1 − f ) tan ϕA; tan UB = (1 − f ) tan ϕB (3)
# 4. Iteracyjne obliczenie L: równania (5) — (8).
# W pierwszym przybliżeniu przyjmujemy:
# L = ∆λ (4)
# 5. Odległość sferyczna między punktami σ:
# sin σ =
# √
# (cos UB sin L)2 + (cos UA sin UB − sin UA cos UB cos L)2; (5)
# cos σ = sin UA sin UB + cos UA cos UB cos L; (6)
# σ = arctan
# ( sin σ
# cos σ
# )
# ; (7)
# 6. Obliczenie azymutu linii geodezyjnej na równiku α:
# sin α = cos UA cos UB sin L
# sin σ ; (8)
# cos2 α = 1 − sin2 α; (9)
# 7. Odległość kątowa punktu środkowego linii geodezyjnej od równika σm:
# cos 2σm = cos σ − 2 sin UA sin UB
# cos2 α ; (10)
# 8. Obliczenie poprawionej wartości różnicy długości geodezyjnych na sferze pomocniczej
# L:
# C = f
# 16 cos2 α[4 + f (4 − 3 cos2 α)]; (11)
# L = ∆λ + (1 − C)f sin α
# {
# σ + C sin σ [
# cos 2σm + C cos σ(−1 + 2 cos2 2σm)]}
# ; (12)
# Warunkiem zakończenia iteracji jest |Li+1 − Li| < 0”.000001.
# 9. Obliczenie długości linii geodezyjnej sAB oraz azymutów AA i AB :
# u2 = a2 − b2
# b2 cos2 α; (13)
# A = 1 + u2
# 16384
# {
# 4096 + u2 [
# −768 + u2 (
# 320 − 175u2)]}
# ; (14)
# B = u2
# 1024
# {
# 256 + u2 [
# −128 + u2 (
# 74 − 47u2)]}
# ; (15)
# ∆σ = B sin σ
# {
# cos 2σm + 1
# 4B[
# cos σ(−1 + 2 cos2 2σm)
# − 1
# 6B cos 2σm(−3 + 4 sin2 σ)(−3 + 4 cos2 2σm)]}
# ; (16)
# sAB = bA(σ − ∆σ); (17)
# AAB = arctan
# ( cos UB sin L
# cos UA sin UB − sin UA cos UB cos L
# )
# ; (18)
# ABA = arctan
# ( cos UA sin L
# − sin UA cos UB + cosUA sin UB cos L
# )
# + π; (19)
# 2

# Przeniesienie współrzednych geodezyjnych na powierzchni
# elipsoidy obrotowej
# Wybrane Zagadnienia Geodezji Wyższej
# Maciej Grzymała
# maciej.grzymala@pw.edu.pl
# Wydział Geodezji i Kartografii, Politechnika Warszawska
# Warszawa, 2023
# 1 Zadanie
# Dane są współrzędne geodezyjne punktu początkowego P1:
# Dla grupy 1:
# • φ1 = 50◦00′00.00000” + nr · 15′
# • λ1 = 18◦00′00.00000” + nr · 15′
# Dla grupy 2:
# • φ1 = 54◦00′00.00000 − nr · 15′
# • λ1 = 15◦00′00.00000” + nr · 15′
# Dane są również azymuty oraz długości trzech linii geodezyjnych:
# długość s [km] azymut A [◦]
# 1 – 2 40 0◦00′00.000”
# 2 – 3 100 90◦00′00.000”
# 3 – 4 40 180◦00′00.000”
# 4 – 1* 100 270◦00′00.000”
# Zadanie
# 1. Oblicz współrzędne geodezyjne punktów: 2, 3, 4, z wykorzystaniem algorytmu Kivioja lub
# z wykorzystaniem bibliotek języka python. Polecaną biblioteką jest pyproj, z modułem
# Geod – funkcje fwd (zadanie wprost) oraz inv (zadanie odwrotne),
# 2. Czy po obliczeniu kolejnych wierzchołków ‘trapezu’, na podstawie podanych obserwacji,
# zamkniemy otrzymamy figurę zamkniętą? Jaka będzie różnica położenia punktów 1 i 1*?
# Czy spowodowana będzie otrzymana różnica?
# 3. Wyznacz właściwe obserwacje: odległość oraz azymut z punktu 4 do punktu 1 (zadanie
# odwrotne – algorytm Vincentego lub inny),
# 1
# 4. Przedstaw na mapie położenie wszystkich punktów (narysuj powstałą figurę)
# 5. Oblicz pole powierzchni powstałej figury (skorzystaj z funkcji z bibliotek języka python, np.
# geometry_area_perimeter lub polygon_area_perimeter z biblioteki pyproj,
# modułu Geod).
# Uwagi:
# • Wyniki podajemy z dokładnością 0.001 m dla współrzędnych prostokątnych i wysokości
# (oraz odległosci) i z dokładnością 0.00001′′ dla współrzędnych geodezyjnych krzywolinio-
# wych.
# • Dla każdych wartości podajemy odpowiednie jednostki.
# • Ćwiczenie oddajemy w formacie .pdf; na okładce ćwiczenia proszę podać nr grupy i nr
# do zadania.
# 2

import numpy as np
a = 6378137
e2 = 0.00669438002290

def vincenty(BA,LA,BB,LB):
    '''
    Parameters
    ----------
    BA : szerokosc geodezyjna punktu A [RADIAN]
    LA : dlugosc geodezyjna punktu A [RADIAN]
    BB : szerokosc geodezyjna punktu B [RADIAN]
    LB : dlugosc geodezyjna punktu B [RADIAN]

    Returns
    -------
    sAB : dlugosc linii geodezyjnej AB [METR]
    A_AB : azymut linii geodezyjnej AB [RADIAN]
    A_BA : azymut odwrotny linii geodezyjne [RADIAN]
    '''
    b = a * np.sqrt(1-e2)
    f = 1-b/a
    dL = LB - LA
    UA = np.arctan((1-f)*np.tan(BA))
    UB = np.arctan((1-f)*np.tan(BB))
    L = dL
    while True:
        sin_sig = np.sqrt((np.cos(UB)*np.sin(L))**2 +\
                          (np.cos(UA)*np.sin(UB) - np.sin(UA)*np.cos(UB)*np.cos(L))**2)
        cos_sig = np.sin(UA)*np.sin(UB) + np.cos(UA) * np.cos(UB) * np.cos(L)
        sig = np.arctan2(sin_sig,cos_sig)
        sin_al = (np.cos(UA)*np.cos(UB)*np.sin(L))/sin_sig
        cos2_al = 1 - sin_al**2
        cos2_sigm = cos_sig - (2 * np.sin(UA) * np.sin(UB))/cos2_al
        C = (f/16) * cos2_al * (4 + f*(4 - 3 * cos2_al))
        Lst = L
        L = dL + (1-C)*f*sin_al*(sig+C*sin_sig*(cos2_sigm+C*cos_sig*(-1 + 2*cos2_sigm**2)))
        if abs(L-Lst)<(0.000001/206265):
            break
    
    u2 = (a**2 - b**2)/(b**2) * cos2_al
    A = 1 + (u2/16384) * (4096 + u2*(-768 + u2 * (320 - 175 * u2)))
    B = u2/1024 * (256 + u2 * (-128 + u2 * (74 - 47 * u2)))
    d_sig = B*sin_sig * (cos2_sigm + 1/4*B*(cos_sig*(-1+2*cos2_sigm**2)\
            - 1/6 *B*cos2_sigm * (-3 + 4*sin_sig**2)*(-3+4*cos2_sigm**2)))
    sAB = b*A*(sig-d_sig)
    A_AB = np.arctan2((np.cos(UB) * np.sin(L)),(np.cos(UA)*np.sin(UB) - np.sin(UA)*np.cos(UB)*np.cos(L)))
    A_BA = np.arctan2((np.cos(UA) * np.sin(L)),(-np.sin(UA)*np.cos(UB) + np.cos(UA)*np.sin(UB)*np.cos(L))) + np.pi
    return sAB, A_AB, A_BA

# dane gr1 nr2
phi1 = np.radians(50+2*15)
lam1 = np.radians(18+2*15)

dl1 = 40
az1 = 0
dl2 = 100
az2 = np.deg2rad(90)
dl3 = 40
az3 = np.deg2rad(180)
dl4 = 100
az4 = np.deg2rad(270)

# Oblicz współrzędne geodezyjne punktów: 2, 3, 4, z wykorzystaniem algorytmu Kivioja lub
# z wykorzystaniem bibliotek języka python. Polecaną biblioteką jest pyproj, z modułem
# Geod – funkcje fwd (zadanie wprost) oraz inv (zadanie odwrotne)

import pyproj
geod = pyproj.Geod(ellps='GRS80')
p1 = geod.fwd(lam1,phi1,dl1,az1)
p2 = geod.fwd(p1[0],p1[1],dl2,az2)
p3 = geod.fwd(p2[0],p2[1],dl3,az3)
p4 = geod.fwd(p3[0],p3[1],dl4,az4)

# Czy po obliczeniu kolejnych wierzchołków ‘trapezu’, na podstawie podanych obserwacji,
# zamkniemy otrzymamy figurę zamkniętą? Jaka będzie różnica położenia punktów 1 i 1*?
# Czy spowodowana będzie otrzymana różnica?

r = geod.inv(p4[0],p4[1],lam1,phi1)
print('Różnica położenia punktów 1 i 1* wynosi: {:.3f} m'.format(r[2]))

# Wyznacz właściwe obserwacje: odległość oraz azymut z punktu 4 do punktu 1 (zadanie
# odwrotne – algorytm Vincentego lub inny),

sAB, A_AB, A_BA = vincenty(phi1,lam1,np.radians(50),np.radians(18))
print('Odległość z punktu 4 do punktu 1 wynosi: {:.3f} m'.format(sAB))
print('Azymut z punktu 4 do punktu 1 wynosi: {:.3f} stopni'.format(np.degrees(A_AB)))

# Przedstaw na mapie położenie wszystkich punktów (narysuj powstałą figurę)

import folium
m = folium.Map(location=[50,18],zoom_start=6)
folium.Marker([np.degrees(phi1),np.degrees(lam1)],popup='P1').add_to(m)
folium.Marker([np.degrees(p1[1]),np.degrees(p1[0])],popup='P2').add_to(m)
folium.Marker([np.degrees(p2[1]),np.degrees(p2[0])],popup='P3').add_to(m)
folium.Marker([np.degrees(p3[1]),np.degrees(p3[0])],popup='P4').add_to(m)
folium.Marker([np.degrees(p4[1]),np.degrees(p4[0])],popup='P5').add_to(m)

folium.PolyLine([[np.degrees(phi1),np.degrees(lam1)],[np.degrees(p1[1]),np.degrees(p1[0])]],color='red').add_to(m)
folium.PolyLine([[np.degrees(p1[1]),np.degrees(p1[0])],[np.degrees(p2[1]),np.degrees(p2[0])]],color='red').add_to(m)
folium.PolyLine([[np.degrees(p2[1]),np.degrees(p2[0])],[np.degrees(p3[1]),np.degrees(p3[0])]],color='red').add_to(m)
folium.PolyLine([[np.degrees(p3[1]),np.degrees(p3[0])],[np.degrees(p4[1]),np.degrees(p4[0])]],color='red').add_to(m)
folium.PolyLine([[np.degrees(p4[1]),np.degrees(p4[0])],[np.degrees(phi1),np.degrees(lam1)]],color='red').add_to(m)

m.save('mapa.html')
