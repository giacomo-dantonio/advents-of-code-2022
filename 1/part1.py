def main():
    with open("input") as f:
        max_calories = -1
        current_calories = 0
        for line in f:
            try:
                current_calories += int(line.rstrip("\r\n"))
            except ValueError:
                max_calories = max(max_calories, current_calories)
                current_calories = 0

    print("Max calories:", max_calories)

if __name__ == "__main__":
    main()
