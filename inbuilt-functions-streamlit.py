import streamlit as st
import math
import random
import datetime

# ─────────────────────────────────────────────
# 1. BUILT-IN FUNCTIONS
# ─────────────────────────────────────────────

def demo_builtin_functions():
    st.header("🔧 Built-in Functions")

    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    st.subheader("Sample List")
    st.code(f"data = {data}")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("len()", len(data))
    col2.metric("sum()", sum(data))
    col3.metric("min()", min(data))
    col4.metric("max()", max(data))

    st.subheader("Type Conversion")
    user_input = st.text_input("Enter a number:", value="42")
    try:
        as_int   = int(user_input)
        as_float = float(user_input)
        as_str   = str(as_int)
        as_bool  = bool(as_int)
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("int()",   as_int)
        c2.metric("float()", as_float)
        c3.metric("str()",   as_str)
        c4.metric("bool()",  as_bool)
    except ValueError:
        st.error("Please enter a valid number.")

    st.subheader("Iterables & Sequences")
    rng = list(range(1, 11))
    st.write("range(1, 11) →", rng)
    st.write("sorted(data) →", sorted(data))
    st.write("reversed →",     list(reversed(data)))
    st.write("enumerate →",    list(enumerate(data[:5])))
    st.write("zip →",          list(zip(rng[:5], data[:5])))

    st.subheader("Functional Tools")
    squared  = list(map(lambda x: x ** 2, data))
    evens    = list(filter(lambda x: x % 2 == 0, data))
    st.write("map(square) →",  squared)
    st.write("filter(even) →", evens)

    st.subheader("Object Introspection")
    sample = "Hello, Python!"
    st.write("type()  →", type(sample))
    st.write("id()    →", id(sample))
    st.write("dir()   →", dir(sample)[:10], "…")

    st.subheader("abs / round / pow / divmod")
    n = st.slider("Pick a number", -20, 20, -7)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("abs()",    abs(n))
    c2.metric("round()",  round(n / 3, 2))
    c3.metric("pow(n,2)", pow(n, 2))
    c4.metric("divmod()", str(divmod(n, 3)))

    st.subheader("any() / all()")
    flags = [True, False, True, True]
    st.write("flags =", flags)
    st.write("any() →", any(flags), " | all() →", all(flags))


# ─────────────────────────────────────────────
# 2. STRING FUNCTIONS
# ─────────────────────────────────────────────

def demo_string_functions():
    st.header("📝 String Functions")

    text = st.text_input("Enter some text:", value="  Hello, Python World!  ")
    st.code(f'text = "{text}"')

    col1, col2 = st.columns(2)
    with col1:
        st.write("upper()  →", text.upper())
        st.write("lower()  →", text.lower())
        st.write("title()  →", text.title())
        st.write("strip()  →", text.strip())
        st.write("lstrip() →", text.lstrip())
        st.write("rstrip() →", text.rstrip())
    with col2:
        st.write("replace() →", text.replace("Python", "🐍"))
        st.write("split()   →", text.strip().split())
        st.write("find()    →", text.find("Python"))
        st.write("count()   →", text.count("l"))
        st.write("startswith() →", text.strip().startswith("Hello"))
        st.write("endswith()   →", text.strip().endswith("!"))

    st.subheader("Formatting")
    name = st.text_input("Your name:", value="Alice")
    age  = st.number_input("Your age:", value=25, step=1)
    st.write("f-string   →", f"Hi {name}, you are {age} years old!")
    st.write(".format()  →", "Hi {}, you are {} years old!".format(name, age))
    st.write("%-style    →", "Hi %s, you are %d years old!" % (name, age))
    st.write("zfill(10)  →", str(age).zfill(10))
    st.write("center(30) →", name.center(30, "-"))
    st.write("join()     →", " | ".join(["Python", "Streamlit", "Fun"]))


# ─────────────────────────────────────────────
# 3. LIST / DICT / SET FUNCTIONS
# ─────────────────────────────────────────────

def demo_collection_functions():
    st.header("📦 List, Dict & Set Functions")

    # Lists
    st.subheader("List Methods")
    lst = [10, 20, 30, 40, 50]
    st.code(f"lst = {lst}")
    lst_copy = lst.copy()
    lst_copy.append(60)
    lst_copy.insert(2, 99)
    lst_copy.remove(99)
    popped = lst_copy.pop()
    lst_copy.reverse()
    st.write("After append(60), insert(2,99), remove(99), pop(), reverse() →", lst_copy)
    st.write("Popped value →", popped)
    st.write("index(30) →", lst.index(30))
    st.write("count(20) →", lst.count(20))

    # Dicts
    st.subheader("Dictionary Methods")
    person = {"name": "Alice", "age": 25, "city": "Delhi"}
    st.code(f"person = {person}")
    st.write("keys()   →", list(person.keys()))
    st.write("values() →", list(person.values()))
    st.write("items()  →", list(person.items()))
    st.write("get()    →", person.get("name"), "| get(missing, default) →", person.get("job", "N/A"))
    person2 = {"job": "Engineer"}
    person.update(person2)
    st.write("After update({'job':'Engineer'}) →", person)
    st.write("pop('city') →", person.pop("city"), "| remaining →", person)

    # Sets
    st.subheader("Set Operations")
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    st.write("A =", a, " | B =", b)
    st.write("union()        →", a | b)
    st.write("intersection() →", a & b)
    st.write("difference()   →", a - b)
    st.write("symmetric_difference() →", a ^ b)
    st.write("issubset()     →", {1, 2}.issubset(a))


# ─────────────────────────────────────────────
# 4. MATH FUNCTIONS
# ─────────────────────────────────────────────

def demo_math_functions():
    st.header("🔢 Math Functions")

    n = st.slider("Select a number (n)", 1, 20, 5)
    col1, col2, col3 = st.columns(3)
    col1.metric("math.sqrt(n)",  round(math.sqrt(n), 4))
    col2.metric("math.factorial(n)", math.factorial(n))
    col3.metric("math.log(n)",   round(math.log(n), 4))

    col1, col2, col3 = st.columns(3)
    col1.metric("math.ceil(n/2)",  math.ceil(n / 2))
    col2.metric("math.floor(n/2)", math.floor(n / 2))
    col3.metric("math.gcd(n,12)",  math.gcd(n, 12))

    st.write("math.pi →", math.pi)
    st.write("math.e  →", math.e)
    st.write("math.sin(pi/2) →", math.sin(math.pi / 2))
    st.write("math.cos(0)    →", math.cos(0))
    st.write("math.pow(n,3)  →", math.pow(n, 3))
    st.write("math.isfinite(n) →", math.isfinite(n))
    st.write("math.isinf(n)   →", math.isinf(n))
    st.write("math.isnan(n)   →", math.isnan(n))


# ─────────────────────────────────────────────
# 5. RANDOM FUNCTIONS
# ─────────────────────────────────────────────

def demo_random_functions():
    st.header("🎲 Random Functions")

    if st.button("🔄 Re-roll Everything"):
        st.rerun()

    items = ["Apple", "Banana", "Cherry", "Durian", "Elderberry"]
    col1, col2 = st.columns(2)
    with col1:
        st.write("random()         →", round(random.random(), 6))
        st.write("uniform(1, 10)   →", round(random.uniform(1, 10), 4))
        st.write("randint(1, 100)  →", random.randint(1, 100))
        st.write("randrange(0,100,5) →", random.randrange(0, 100, 5))
    with col2:
        st.write("choice(items)    →", random.choice(items))
        sample = random.sample(items, 3)
        st.write("sample(items, 3) →", sample)
        shuffled = items.copy()
        random.shuffle(shuffled)
        st.write("shuffle(items)   →", shuffled)
        st.write("gauss(0, 1)      →", round(random.gauss(0, 1), 4))


# ─────────────────────────────────────────────
# 6. LAMBDA, MAP, FILTER, REDUCE
# ─────────────────────────────────────────────

def demo_functional():
    st.header("⚡ Lambda, Map, Filter & Reduce")
    from functools import reduce

    nums = list(range(1, 11))
    st.write("nums =", nums)

    st.subheader("Lambda")
    square  = lambda x: x ** 2
    cube    = lambda x: x ** 3
    is_even = lambda x: x % 2 == 0
    st.write("square(7)  →", square(7))
    st.write("cube(4)    →", cube(4))
    st.write("is_even(6) →", is_even(6))

    st.subheader("map()")
    st.write("map(square, nums)  →", list(map(square, nums)))
    st.write("map(cube, nums)    →", list(map(cube, nums)))

    st.subheader("filter()")
    st.write("filter(is_even, nums) →", list(filter(is_even, nums)))
    st.write("filter(>5, nums)      →", list(filter(lambda x: x > 5, nums)))

    st.subheader("reduce()")
    total   = reduce(lambda a, b: a + b, nums)
    product = reduce(lambda a, b: a * b, nums)
    st.write("reduce(+, nums) →", total)
    st.write("reduce(*, nums) →", product)

    st.subheader("sorted() with key")
    words = ["banana", "apple", "fig", "elderberry", "date"]
    st.write("By length →", sorted(words, key=len))
    st.write("Reverse α  →", sorted(words, reverse=True))


# ─────────────────────────────────────────────
# 7. DATE & TIME FUNCTIONS
# ─────────────────────────────────────────────

def demo_datetime_functions():
    st.header("📅 Date & Time Functions")

    now = datetime.datetime.now()
    today = datetime.date.today()

    st.subheader("Current Date & Time")
    col1, col2, col3 = st.columns(3)
    col1.metric("Year",   now.year)
    col2.metric("Month",  now.month)
    col3.metric("Day",    now.day)
    col1, col2, col3 = st.columns(3)
    col1.metric("Hour",   now.hour)
    col2.metric("Minute", now.minute)
    col3.metric("Second", now.second)

    st.subheader("Formatting & Parsing")
    fmt = now.strftime("%A, %d %B %Y — %H:%M:%S")
    st.write("strftime() →", fmt)
    parsed = datetime.datetime.strptime("2025-01-15", "%Y-%m-%d")
    st.write("strptime() →", parsed)

    st.subheader("Date Arithmetic")
    delta = datetime.timedelta(days=30)
    st.write("today + 30 days →", today + delta)
    st.write("today - 30 days →", today - delta)
    d1 = datetime.date(2024, 1, 1)
    d2 = datetime.date.today()
    st.write("Days since 2024-01-01 →", (d2 - d1).days)


# ─────────────────────────────────────────────
# 8. FILE I/O (simulated in-memory)
# ─────────────────────────────────────────────

def demo_file_functions():
    st.header("📁 File I/O Functions (In-Memory Demo)")
    import io

    st.info("Using in-memory StringIO to simulate file operations safely.")

    content = st.text_area("File content to write:", value="Hello, Python!\nLine 2\nLine 3\n")

    buf = io.StringIO()
    buf.write(content)
    buf.seek(0)

    st.subheader("read()")
    st.code(buf.read())

    buf.seek(0)
    st.subheader("readlines()")
    lines = buf.readlines()
    st.write(lines)

    buf.seek(0)
    st.subheader("readline() × 2")
    st.write("Line 1:", buf.readline())
    st.write("Line 2:", buf.readline())

    st.subheader("tell() & seek()")
    st.write("tell() after 2 readlines →", buf.tell())
    buf.seek(0)
    st.write("tell() after seek(0)     →", buf.tell())


# ─────────────────────────────────────────────
# 9. COMPREHENSIONS & GENERATORS
# ─────────────────────────────────────────────

def demo_comprehensions():
    st.header("🔄 Comprehensions & Generators")

    nums = list(range(1, 11))
    st.write("nums =", nums)

    st.subheader("List Comprehension")
    st.write("[x²]          →", [x**2 for x in nums])
    st.write("[even x²]     →", [x**2 for x in nums if x % 2 == 0])

    st.subheader("Dict Comprehension")
    st.write("{x: x²}       →", {x: x**2 for x in nums})

    st.subheader("Set Comprehension")
    st.write("{x % 4}       →", {x % 4 for x in nums})

    st.subheader("Generator Expression")
    gen = (x**2 for x in range(5))
    st.write("next() × 3   →", next(gen), next(gen), next(gen))
    st.write("list(gen)rest →", list(gen))

    st.subheader("Nested Comprehension")
    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    st.write("3×3 table →")
    st.table(matrix)


# ─────────────────────────────────────────────
# MAIN APP
# ─────────────────────────────────────────────

def main():
    st.set_page_config(
        page_title="🐍 Python Functions Explorer",
        page_icon="🐍",
        layout="wide"
    )

    st.title("🐍 Python Functions Explorer")
    st.caption("An interactive tour of Python's most important built-in & standard-library functions.")

    sections = {
        "🔧 Built-in Functions":           demo_builtin_functions,
        "📝 String Functions":             demo_string_functions,
        "📦 Collections (List/Dict/Set)":  demo_collection_functions,
        "🔢 Math Functions":               demo_math_functions,
        "🎲 Random Functions":             demo_random_functions,
        "⚡ Lambda / Map / Filter / Reduce": demo_functional,
        "📅 Date & Time Functions":        demo_datetime_functions,
        "📁 File I/O Functions":           demo_file_functions,
        "🔄 Comprehensions & Generators":  demo_comprehensions,
    }

    with st.sidebar:
        st.header("📚 Sections")
        choice = st.radio("Jump to:", list(sections.keys()))
        st.markdown("---")
        st.caption("Built with ❤️ using Streamlit")

    sections[choice]()


if __name__ == "__main__":
    main()