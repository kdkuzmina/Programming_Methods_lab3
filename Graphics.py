import matplotlib.pyplot as plt

x = [100, 500, 1000, 2500, 5000, 7500, 10000]
linear = [2.3126602172851562e-05, 6.985664367675781e-05, 0.0003299713134765625,
          0.0010979175567626953, 0.0017919540405273438, 0.002961874008178711, 0.004200935363769531]

binary = [6.9141387939453125e-06, 1.1205673217773438e-05, 2.5987625122070312e-05,
          1.6927719116210938e-05, 1.7881393432617188e-05, 1.8835067749023438e-05, 1.811981201171875e-05]

multimap = [3.504753112792969e-05, 0.00017786026000976562, 2.5033950805664062e-05,
               2.4080276489257812e-05, 3.504753112792969e-05, 3.0040740966796875e-05, 2.3126602172851562e-05]

hash = [8.344650268554688e-06, 9.059906005859375e-06, 1.0013580322265625e-05, 1.4066696166992188e-05,
        1.6927719116210938e-05, 1.6927719116210938e-05, 1.5735626220703125e-05]

simple_collision = [38, 175, 433, 1613, 3908, 6308, 8735]

complex_collision = [36, 185, 389, 922, 1836, 2755, 3692]

#plt.plot(x, linear, label ="linear", color ='#5451B6', linewidth = 1.5, marker ='.')
plt.plot(x, binary, label ="binary", color ='#5E8CB8', linewidth = 1.5, marker ='*')
plt.plot(x, multimap, label ="multimap", color ='#CE81AD', linewidth = 1.5, marker = '+')
plt.plot(x, hash, label ="hash", color ='#76BFBF', linewidth = 1.5, marker = 'o')

#plt.plot(x, simple_collision, label ="simple hash", color ='#C996FF', linewidth = 1.5, marker ='.')
#plt.plot(x, complex_collision, label ="complex hash", color ='#FF96CC', linewidth = 1.5, marker ='*')
plt.legend()
plt.show()
