string = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel leo non nisl bibendum lacinia 
lobortis in dui. Suspendisse consectetur tortor quis nunc pellentesque, a fermentum nulla posuere. 
Aliquam erat volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere 
cubilia curae; Ut sodales, libero ut elementum scelerisque, augue ex sagittis lectus, eget aliquet 
ipsum elit vel tortor. Nam volutpat fringilla ante. Donec facilisis leo finibus volutpat consequat. 
Nulla hendrerit vel dui eget tempor. In hac habitasse platea dictumst. In hac habitasse platea 
dictumst.

Nam viverra tincidunt leo, sit amet euismod urna sagittis non. Aliquam consectetur aliquam est, et 
blandit quam ullamcorper a. Cras fringilla placerat dolor, et vulputate ex elementum eu. Aliquam 
erat volutpat. Sed nec risus justo. Cras sit amet tellus nec dui blandit ornare quis eu turpis. 
Quisque viverra nisl ac enim volutpat pretium. Nulla nisi libero, pretium sed mauris nec, malesuada 
mattis erat. Nunc pulvinar in nisl non ultricies.

Morbi bibendum, risus id lacinia efficitur, augue odio ultrices nibh, non eleifend nulla diam sit 
amet est. Donec finibus magna nec dui rhoncus, in condimentum nisl lacinia. Cras blandit nibh est, 
ut sodales ligula pellentesque non. Mauris accumsan nisl est, in egestas turpis lobortis sed. 
Aenean ut felis sit amet leo sagittis elementum in quis ligula. Nunc ligula leo, feugiat in ante 
vitae, ornare auctor lectus. Integer metus arcu, venenatis et semper sed, eleifend in lectus. Donec 
feugiat tortor volutpat tortor sodales laoreet.

Phasellus tempor quam ac quam molestie lobortis. Donec auctor quam dolor, nec accumsan arcu 
elementum et. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia 
curae; Nullam sollicitudin, odio nec lobortis sodales, est sapien efficitur purus, lacinia eleifend 
leo elit vel eros. Curabitur facilisis feugiat magna, vitae laoreet ex sollicitudin ac. Vivamus 
lacinia rutrum nisl, vel placerat turpis gravida nec. Morbi mattis efficitur mollis. Nam gravida 
viverra quam, eget dictum nulla tristique vitae. Curabitur fringilla sagittis nunc, congue suscipit 
nisi semper tristique. Proin fringilla nec quam sit amet dapibus. Nunc faucibus vel lorem non 
dapibus. Vivamus in tempor nisi. Pellentesque ipsum quam, varius ut sagittis ut, fringilla ut ante. 
In elementum dui tincidunt risus fringilla malesuada.

Morbi ut nisl nulla. Aenean ut dignissim diam. Sed pretium ornare pretium. Vestibulum ante ipsum 
primis in faucibus orci luctus et ultrices posuere cubilia curae; Vivamus metus metus, accumsan 
eleifend condimentum ut, fringilla sollicitudin nunc. Suspendisse scelerisque massa id finibus 
molestie. Sed faucibus vehicula sollicitudin. Proin et faucibus mi. Phasellus maximus nisi nec 
blandit tristique. 
"""
import time
from enigma import Enigma

start = time.time()
print("Time elapsed on working...")

mach1 = Enigma(
    start_pos=("A", "A", "A"),
    rotors=(1, 2, 3),
    reflector="B",
    ring_setting=("A", "A", "A"),
    plugboard=[],
)

mach1.encipher(string)

end = time.time()
print("Time consumed in working: ", end - start)
