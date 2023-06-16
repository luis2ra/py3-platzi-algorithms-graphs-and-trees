'''
Calculo de la mediana (modo ordinario)
'''

# nums = [8, 7, 1, 5, 3, 8, 11, 6, 14]
nums = [6, 9, 3, 2, 13]     # numero impar de elementos
nums = [6, 9, 3, 2, 13, 8]  # numero par de elementos

def median(numbers):
    sorted_nums = sorted(numbers)
    middle = round(len(sorted_nums) / 2)

    if len(sorted_nums) % 2 == 0:
        return (sorted_nums[middle-1] + sorted_nums[middle]) / 2
    
    return sorted_nums[middle]


def run():
    print(median(nums))


if __name__ == "__main__":
    run()
