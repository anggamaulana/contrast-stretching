# contrast-stretching
Penerapan Linear Contrast Stretching

L=256 (bit gambar grayscale)

r=input gray

s=output gray baru


Untuk r <= 0 < r1, maka s = r . (s1 / r1)

Untuk r1 <= r < r2, maka s = s1 + ( (r-r1) . ((s2-s1) / (r2-r1)) )

Untuk r2 <= r <=(L-1), maka s = s2 + ( (r-r2) . ((L-1)-s2) / ((L-1) - r2) )
