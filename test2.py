h = int(input())
m = int(input())
s = int(input())
hh = int(input())
mm = int(input())
ss = int(input())
h_s = h*60*60
m_s = m*60
hh_s = hh*60*60
mm_s =mm*60
timestand_one = h_s + m_s + s
timestand_two = hh_s + mm_s + ss
duration = timestand_two - timestand_one
print(duration)