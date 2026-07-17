# Functions ee Python

**Function** waa qayb koodh ah oo loo sameeyo inay qabato hawl gaar ah. Halkii aan isla koodhka marar badan qori lahayn, waxaan ku qornaa function hal mar, kadibna mar kasta oo aan u baahanno waan u yeernaa (call).

Functions waxay ka dhigaan koodhka mid nadiif ah, fudud in la fahmo, isla markaana dib loo isticmaali karo.

---

# Sida Function loo Abuuro

Python wuxuu isticmaalaa erayga `def` si loo abuuro function.

```python
def greet():
    print("Asc, Soo dhawoow!")
```

Si aan u isticmaalno function-ka, waxaan u yeernaa magaca function-ka.

```python
greet()
```

**Natiijada:**

```text
Asc, Soo dhawoow!
```

---

# Function leh Parameters

Mararka qaar waxaan rabnaa inaan function-ka u gudbinno xog. Xogtaas waxaa la yiraahdaa **Parameters**.

```python
def greet(name):
    print("Asc", name)
```

Markaan u yeerno:

```python
greet("Ahmed")
```

**Natiijada:**

```text
Asc Ahmed
```

Halkan `name` waa parameter, halka `"Ahmed"` uu yahay argument-ka aan u gudbinay function-ka.

---

# Function Soo Celiya Qiime (`return`)

`return` waxaa loo isticmaalaa marka function-ku soo celinayo qiime.

```python
def add(a, b):
    return a + b

result = add(10, 5)
print(result)
```

**Natiijada:**

```text
15
```

### Sharaxaad

- `a` waa 10.
- `b` waa 5.
- Function-ku wuxuu isku darayaa labada tiro, kadibna wuxuu soo celiyaa natiijada.

---

# Faa'iidooyinka Functions

- Waxay yareeyaan ku celcelinta koodhka.
- Waxay ka dhigaan koodhka mid nadiif ah.
- Waxay fududeeyaan hagaajinta iyo fahamka barnaamijka.
- Hal function waxaa loo isticmaali karaa marar badan.

---

# Gunaanad

Functions waa qayb muhiim ah oo Python ah.

Waxyaabaha muhiimka ah waa:

- `def` → Waxaa lagu abuuraa function.
- `Parameters` → Xogta uu function-ku qaato.
- `return` → Qiimaha uu function-ku soo celiyo.

Functions waxay kaa caawinayaan inaad qorto koodh habaysan, fudud in dib loo isticmaalo, isla markaana si sahlan loo maamuli karo.
