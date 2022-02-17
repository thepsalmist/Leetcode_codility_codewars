def unique_names(names1, names2):
    result = names1.extend(names2)
    return list(set(names1.extend(names2)))


if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2))  # should print Ava, Emma, Olivia, Sophia
