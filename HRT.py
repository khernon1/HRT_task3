from datetime import datetime as dt

def solution(S):
  # split larger string into list by line break
  lst = [y for y in (x.strip() for x in S.splitlines()) if y]

  formatted_lst = []
  photo_city_lst = []
  # split each member of this list now
  for pht in lst:
    city_lst = []
    pht_lst = pht.split(',')

    # gets each city, extension, and date
    city_lst.append(pht_lst[0].split('.')[1])
    city_lst.append(pht_lst[1].strip())

    new_dt = pht_lst[2].strip()
    f = "%Y-%m-%d %H:%M:%S"
    d_str = dt.strptime(new_dt, f)
    
    city_lst.append(d_str)

    # adds num of times city has appeared
    if pht_lst[1].strip() not in photo_city_lst:
      city_lst.append(1)
    else:
      city_lst.append(photo_city_lst.count(pht_lst[1].strip())+1)

    photo_city_lst.append(pht_lst[1].strip())

    # creates list of list with all info
    formatted_lst.append(city_lst)

  # print formatted_lst

  for photo in formatted_lst:
    if photo[3] <= 9:
      print photo[1] + '0' + str(photo[3]) + '.' + photo[0]
    else:
      print photo[1] + str(photo[3]) + '.' + photo[0]    



S = """ photo.jpg, Warsaw, 2013-09-05 14:08:15
  john.png, London, 2015-06-20 15:13:22 
  BOB.jpg, London, 2015-08-05 00:02:03
  notredame.png, Paris, 2015-09-01 12:00:00
  me.jpg, Warsaw, 2013-09-06 15:40:22
  Eiffel.jpg, Paris, 2015-07-23 08:03:02
  pisatower.jpg, Paris, 2015-07-22 23:59:59
  BOB.jpg, London, 2015-08-05 00:02:03
  notredame.png, Paris, 2015-09-01 12:00:00
  me.jpg, Warsaw, 2013-09-06 15:40:22
  a.png, Warsaw, 2016-02-13 13:33:50
  b.jpg, Warsaw, 2016-01-02 15:12:22
  c.jpg, Warsaw, 2016-01-02 14:34:30
  d.jpg, Warsaw, 2016-01-02 15:15:01
  e.png, Warsaw, 2016-01-02 09:49:09
  f.png, Warsaw, 2016-01-02 10:55:32
  g.jpg, Warsaw, 2016-02-29 22:13:11 """

print solution(S)

