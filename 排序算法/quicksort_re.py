def quicksort(data):
    stone  = data[0]
    i, j= 1, len(data) - 1
    if len(data) > 1:
        while j > i:
            if data[j] <= stone:
                if data[i] < stone:
                    data[i], data[j] = data[j], data[i]
                else:
                    i += 1
            else:
                j += 1
        if data[j] < stone:
            data[0], data[j] = data[j], data[0]
        return quicksort(data[:j]) + quicksort(data[j+1:])
    else:
        return data
