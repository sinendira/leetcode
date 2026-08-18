class Solution:
    def lengthLongestPath(self, input: str) -> int:
        longest_abs_path = 0
        stack = []
        input = input.split("\n")
        input_len = len(input)
        prev_layer_len = -1
        for i in range(input_len):
            layer = input[i]
            layer = layer.split("\t")
            curr_layer_len = len(layer)
            if curr_layer_len == prev_layer_len:
                stack.pop()
            elif curr_layer_len < prev_layer_len:
                while len(stack) != curr_layer_len - 1:
                    stack.pop()
            layer = layer[-1]
            stack.append(layer)
            prev_layer_len = curr_layer_len
            if "." in layer:
                curr_abs_path = sum(len(part) for part in stack) + len(stack) - 1
                longest_abs_path = max(longest_abs_path, curr_abs_path)

        return longest_abs_path