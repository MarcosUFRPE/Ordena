class Sorter:
    def __init__(self):
        pass

    def ordene_selection(self, valores) -> [int]:
        return [1]

    def ordene_insertion(self, valores) -> [int]:
        ordene = valores()         
        for i in range(1, len(ordene)):
            lista  = ordene[i]  
            j = i - 1
            while j >= 0 and lista < ordene[j]:
                ordene[j - 1] = ordene[j]
                j -= 1            
            ordene[j - 1] = lista
        return ordene  