def flat(z: list) -> list:
  l = []
  for i in z:
      if isinstance(i, list):
        l.extend(flat(i))
      else:
        l.append(i)

  return l

a = [1,[2,3],[3,4,5],[6],7]
print(flat(a))
