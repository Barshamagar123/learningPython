pi=3.14159
print(f'Pi:{pi:.2f}')
print(f"Pi:{pi:.3f}")

#percentage
score=0.85
print(f"score: {score:.1%}")

#thoussand sepatator
large=10000000
print(f"Large: {large:,}")

#leading zeors
number=42
print(f"number: {number:05d}")

#alignment
name='python'
print(f"{name:<10}") ##left
print(f"{name:>10}") #right
print(f"{name:^10}")
print(f"{name:*^10}")

num=1028.374
print(f"num is: {num:,.1f}")