def main():
    print(f("5233165554211"))
    print(f("2133"))


def f(dice):
    current_count = 1
    max_count = 1
    current_dice = dice[0]

    for i in range(1, len(dice)):
        if dice[i - 1] == dice[i]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                current_dice = dice[i - 1]
            current_count = 1
    
    if current_count > max_count:
        current_dice = dice[-1]
    
    return int(current_dice)

if __name__ == "__main__":
    main()