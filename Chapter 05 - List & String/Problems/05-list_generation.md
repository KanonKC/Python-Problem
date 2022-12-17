List Generation
==============

เขียน list comprehension เพื่อสร้างและแสดงลิสของลำดับเหล่านี้ออกทางหน้าจอ

1.)
<pre class="output">
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9]
</pre>
::elab:begincode language="python3"
::elab:hide --- ex1.py
print({{[i for i in range(20,8,-1)]                  }})
::elab:endcode
::elab:begintest hint="Exercise 1"
elab-split-files source.txt ---
python3 ex1.py
::elab:endtest

2.)
<pre class="output">
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100,121, 144]
</pre>
::elab:begincode language="python3"
::elab:hide --- ex2.py
print({{[i**2 for i in range(1,13)]                  }})
::elab:endcode
::elab:begintest hint="Exercise 2"
elab-split-files source.txt ---
python3 ex2.py
::elab:endtest

3.)
<pre class="output">
[-1, 3, -5, 7, -9, 11, -13, 15, -17, 19, -21, 23, -25]
</pre>
::elab:begincode language="python3"
::elab:hide --- ex3.py
print({{[(2*i+1)*((-1)**(i+1)) for i in range(13)]   }})
::elab:endcode
::elab:begintest hint="Exercise 3"
elab-split-files source.txt ---
python3 ex3.py
::elab:endtest

4.)
<pre class="output">
[1, 3, 6, 10, 15, 21, 28, 36, 45]
</pre>
::elab:begincode language="python3"
::elab:hide --- ex4.py
print({{[sum(list(range(i+1))) for i in  range(1,10)]}})
::elab:endcode
::elab:begintest hint="Exercise 4"
elab-split-files source.txt ---
python3 ex4.py
::elab:endtest

5.)
<pre class="output">
['\*', '\*\*\*', '\*\*\*\*\*', '\*\*\*\*\*\*\*', '\*\*\*\*\*\*\*\*\*']
</pre>
::elab:begincode language="python3"
::elab:hide --- ex5.py
print({{['*'*i for i in range(1,10,2)]               }})
::elab:endcode
::elab:begintest hint="Exercise 5"
elab-split-files source.txt ---
python3 ex5.py
::elab:endtest