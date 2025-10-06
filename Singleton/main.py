from Singleton.Singleton import SingletonNew

if __name__ == "__main__":
    print("=" * 50)
    print("Method 1: Using __new__")
    print("=" * 50)
    s1 = SingletonNew("First")
    s2 = SingletonNew("Second")
    print(f"s1 value: {s1.value}")
    print(f"s2 value: {s2.value}")
    print(f"s1 is s2: {s1 is s2}")
    print(f"ID s1: {id(s1)}, ID s2: {id(s2)}")

    print("\n" + "=" * 50)