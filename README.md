# Lorem Assembly – Magyar értelmetlen mondatgenerátor

Ez a projekt értelmetlen magyar mondatokat generáló programokat tartalmaz, több programozási nyelven és platformon megvalósítva.

---

## Tartalom

| Fájl | Leírás |
|---|---|
| `hello.asm` | Klasszikus „Hello World" x86-64 assembly (Linux) |
| `lorem-1.asm` | Egyszerű lorem ipsum generátor assembly-ben (3 előre írt mondat) |
| `lorem-1.py` | Lorem ipsum generátor Pythonban (véletlenszerű szókincsből épít mondatokat) |
| `lorem-2.py` | Fejlettebb verzió: helyes magyar névelőkkel (a/az) |
| `lorem-2.exs` | Ugyanaz, Elixir szkriptként megvalósítva |

---

## Működés

Minden program megkérdezi, hány mondatot szeretnél, majd kinyomtatja a kért számú véletlenszerű (vagy előre megírt) értelmetlen magyar mondatot.

**Példa kimenet (`lorem-2.py`):**
```
Hány mondatot akarsz? 3
A kockás bagoly fut az erdőben.
Az asztal halkan gurul a csigát.
A sárga macska vidáman táncol.
```

---

## Futtatás

### Assembly (`hello.asm`, `lorem-1.asm`)

> **Követelmény:** `nasm`, `ld` (Linux x86-64)

```bash
# Hello World
nasm -f elf64 hello.asm -o hello.o
ld hello.o -o hello
./hello

# Lorem ipsum assembly
nasm -f elf64 lorem-1.asm -o lorem-1.o
ld lorem-1.o -o lorem-1
./lorem-1
```

### Python (`lorem-1.py`, `lorem-2.py`)

> **Követelmény:** Python 3

```bash
python3 lorem-1.py
python3 lorem-2.py
```

### Elixir (`lorem-2.exs`)

> **Követelmény:** Elixir

```bash
elixir lorem-2.exs
```

---

## A programok közötti különbségek

- **`lorem-1.asm`** – Assembly szinten, 3 rögzített mondat van benne, ciklikusan ismétli őket.
- **`lorem-1.py`** – Véletlenszerűen választ főneveket, igéket, mellékneveket és határozószókat egy szóbankból, de névelők nélkül. A mondatok `lorem ipsum:` előtaggal kezdődnek.
- **`lorem-2.py` / `lorem-2.exs`** – Felismeri, hogy az adott szó magánhangzóval kezdődik-e, és ennek megfelelően `a` vagy `az` névelőt illeszt be. Természetesebb, teljes mondatokat generál.

---

## Technológiák

- **x86-64 NASM Assembly** (Linux syscall interfész)
- **Python 3**
- **Elixir**
