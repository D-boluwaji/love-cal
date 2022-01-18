def lovecalculator (name1, name2):
    """A love calculator script that calculates percentage of love
based on the amount of common letters in the lovers name."""
    try:
        name1 = int(name1)
        name2 = int(name2)
        return "Please enter an alphabet"
    except ValueError: 
        common_letters = [] 
        percentage = 0
        for letter in name1:
            if letter in name2:
                common_letters.append(letter)
        summed_name = len(name1)+len(name2)
        if common_letters == []:
            return "You have nothing common"
        else:
            common_letters = len(common_letters)
            percentage = (common_letters/summed_name) * 100
            result = f"Your love percentage is {percentage}%"
            return result


name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

print(lovecalculator(name1, name2))
        
