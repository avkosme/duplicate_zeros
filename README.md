# duplicate_zeros

```
$ python3 -m unittest discover tests
```


## Visualization algorithm

```
[0, 4, 1, 0, 0, 8, 0, 0, 3]

[0, 0, 4, 1, 0, 0, 8, 0, 0, 3]
 0  1
 0  1
 0 + 1 + 0

[0, 0, 4, 1, 0, 0, 0, 8, 0, 0, 3]
 0  1  2  3  4  5
          3     5
 1 + 1 + 3

[0, 0, 4, 1, 0, 0, 0, 0, 8, 0, 0, 3]
 0  1  2  3  4  5  6  7
             4        7
 2 + 1 + 4

[0, 0, 4, 1, 0, 0, 0, 0, 8, 0, 0, 0, 3]
 0  1  2  3  4  5  6  7  8  9  10 11
                   6              11
 3 + 1 + 6

[0, 0, 4, 1, 0, 0, 0, 0, 8, 0, 0, 0, 0, 3]
 0  1  2  3  4  5  6  7  8  9  10 11 12
                      7              12
 4 + 1 + 7


```

