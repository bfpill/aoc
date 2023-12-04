with open('input.txt', 'r') as file:
    elves = []
    nums = {
        "one": "1", "two": "2", "three" : "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight" : "8", "nine": "9"
    }

    for line in file:
        n = ""
        s = line.strip()

        for i, c in enumerate(s):
            if c.isdigit():
                n += c
            else:
                for string in nums:
                    if s[i:].startswith(string):
                        n += nums[string]

        elf = n[0] + n[-1]
        elves.append(int(elf))

    print(sum(elves))

