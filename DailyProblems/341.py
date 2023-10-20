# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value):
        self.value = value

    def isInteger(self) -> bool:
        return isinstance(self.value, int)

    def getInteger(self) -> int:
        return self.value

    def getList(self):
        return self.value


class NestedIterator:
    def __init__(self, nested_list: [NestedInteger]):
        self.unnested_list = self.unnested(nested_list)
        self.unnested_list_cur_index = 0

    def unnested(self, nested_list: [NestedInteger]):
        unnested_list = []
        for element in nested_list:
            if element.isInteger():
                unnested_list.append(element.getInteger())
            else:
                unnested_list.extend(self.unnested(element.getList()))

        return unnested_list

    def next(self) -> int:
        result = self.unnested_list[self.unnested_list_cur_index]
        self.unnested_list_cur_index += 1
        return result

    def hasNext(self) -> bool:
        return self.unnested_list_cur_index < len(self.unnested_list)



