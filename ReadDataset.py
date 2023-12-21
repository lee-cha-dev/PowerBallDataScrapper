import pickle


def loadDataSet(nameOfFile):
    pickleIn = open(nameOfFile, "rb")
    dataset = pickle.load(pickleIn)

    return dataset


newDataSet = loadDataSet("powerBallDataset_2022_hardSave")
# print(f'Oldest drawing: {newDataSet[(len(newDataSet) - 1)]}')
# print(newDataSet)
print()
print(f'Newest drawing: {newDataSet[0]}')
print(f'Oldest drawing: {newDataSet[(len(newDataSet) - 1)]}')
print()
print(f'Files in dataset: {len(newDataSet)}')


# NEWEST DRAWING IS THE 0, OLDEST IS THE LAST ONE IN THE FILE
