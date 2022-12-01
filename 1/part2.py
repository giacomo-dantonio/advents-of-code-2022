def main():
    with open("input") as f:
        max_calories = [0, 0, 0]
        current_calories = 0
        for line in f:
            try:
                current_calories += int(line.rstrip("\r\n"))
            except ValueError:
                max_calories.append(current_calories)
                max_calories.remove(min(max_calories))
                current_calories = 0

    print("Max calories:", sum(max_calories))

if __name__ == "__main__":
    main()
